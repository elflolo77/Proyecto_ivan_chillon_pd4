"""Infraestructura: Repositorio en SQLite."""
import sqlite3
from datetime import datetime
from cine_multiplex.domain.repositorio import RepositorioCine
from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica
from cine_multiplex.domain.sala import Sala
from cine_multiplex.domain.sesion import Sesion
from cine_multiplex.domain.entrada import Entrada
from cine_multiplex.infrastructure.errores import (
    ErrorPersistencia,
    EntidadNoEncontradaError,
    EntidadDuplicadaError,
    ErrorIntegridadDatos
)

class RepositorioSQLite(RepositorioCine):
    """Implementación en SQLite del repositorio."""
    
    def __init__(self, ruta_bd="cine.db"):
        self.ruta_bd = ruta_bd

    _TIPOS_PELICULA = {
        "COMERCIAL": (PeliculaComercial, 6),
        "INFANTIL": (PeliculaInfantil, 7),
        "CLASICA": (PeliculaClasica, 8),
    }

    def _ejecutar_consulta(self, query, parametros=(), fetch_one=False, fetch_all=False, commit=False):
        """Ejecuta una consulta SQL genérica y maneja excepciones."""
        from contextlib import closing
        try:
            with closing(sqlite3.connect(self.ruta_bd)) as conn:
                conn.execute("PRAGMA foreign_keys = ON")
                cursor = conn.cursor()
                with conn:
                    cursor.execute(query, parametros)
                    if fetch_one:
                        return cursor.fetchone()
                    if fetch_all:
                        return cursor.fetchall()
                    return cursor.rowcount
        except sqlite3.IntegrityError as e:
            if "UNIQUE" in str(e):
                raise EntidadDuplicadaError(f"Entidad duplicada: {e}")
            elif "FOREIGN KEY" in str(e):
                raise ErrorIntegridadDatos(f"Error de integridad referencial: {e}")
            else:
                raise ErrorIntegridadDatos(f"Error de integridad: {e}")
        except sqlite3.OperationalError as e:
            raise ErrorPersistencia(f"Error operacional de base de datos: {e}")
        except sqlite3.Error as e:
            raise ErrorPersistencia(f"Error de base de datos: {e}")

    # --- PELICULAS ---
    def guardar_pelicula(self, p):
        query = """
            INSERT INTO peliculas (titulo, duracion_minutos, clasificacion, genero, esta_en_cartelera, tipo_pelicula, distribuidora, edad_minima, anio_lanzamiento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        campos = p.campos_extra()
        parametros = (
            p.titulo, p.duracion_minutos, p.clasificacion, p.genero,
            1 if p.esta_en_cartelera else 0, p.tipo,
            campos.get("distribuidora"), campos.get("edad_minima"), campos.get("anio_lanzamiento")
        )
        self._ejecutar_consulta(query, parametros, commit=True)

    def _mapear_pelicula(self, fila):
        if not fila:
            return None
        titulo, duracion, clasif, genero, cartelera, tipo, dist, edad, anio = fila
        
        clase_pelicula, idx_extra = self._TIPOS_PELICULA.get(tipo, (PeliculaComercial, 6))
        campo_extra = fila[idx_extra]
        
        p = clase_pelicula(titulo, duracion, clasif, genero, campo_extra)
        p.esta_en_cartelera = bool(cartelera)
        return p

    def obtener_pelicula_por_titulo(self, titulo):
        fila = self._ejecutar_consulta("SELECT * FROM peliculas WHERE titulo = ?", (titulo,), fetch_one=True)
        return self._mapear_pelicula(fila)

    def listar_todas_las_peliculas(self):
        filas = self._ejecutar_consulta("SELECT * FROM peliculas", fetch_all=True)
        return [self._mapear_pelicula(f) for f in filas]

    # --- SALAS ---
    def guardar_sala(self, s):
        query = """
            INSERT INTO salas (numero, capacidad_maxima, tecnologia_pantalla)
            VALUES (?, ?, ?)
        """
        self._ejecutar_consulta(query, (s.numero, s.capacidad_maxima, s.tecnologia_pantalla), commit=True)

    def _mapear_sala(self, fila):
        if not fila:
            return None
        return Sala(fila[0], fila[1], fila[2])

    def obtener_sala_por_numero(self, numero):
        fila = self._ejecutar_consulta("SELECT * FROM salas WHERE numero = ?", (numero,), fetch_one=True)
        return self._mapear_sala(fila)

    def listar_todas_las_salas(self):
        filas = self._ejecutar_consulta("SELECT * FROM salas", fetch_all=True)
        return [self._mapear_sala(f) for f in filas]

    # --- SESIONES ---
    def guardar_sesion(self, s):
        existe = self._ejecutar_consulta("SELECT 1 FROM sesiones WHERE id_sesion = ?", (s.id_sesion,), fetch_one=True)
        if existe:
            query = """
                UPDATE sesiones SET
                    pelicula_titulo = ?,
                    sala_numero = ?,
                    fecha_hora = ?,
                    numero_asientos_ocupados = ?,
                    estado_sesion = ?
                WHERE id_sesion = ?
            """
            self._ejecutar_consulta(query, (
                s.pelicula.titulo, s.sala.numero, s.fecha_hora,
                s.numero_asientos_ocupados, s.estado_sesion, s.id_sesion
            ), commit=True)
        else:
            query = """
                INSERT INTO sesiones (id_sesion, pelicula_titulo, sala_numero, fecha_hora, numero_asientos_ocupados, estado_sesion)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            self._ejecutar_consulta(query, (
                s.id_sesion, s.pelicula.titulo, s.sala.numero, s.fecha_hora,
                s.numero_asientos_ocupados, s.estado_sesion
            ), commit=True)

    def _mapear_sesion(self, fila):
        if not fila:
            return None
        id_sesion, pel_titulo, sala_num, fecha_hora, ocupados, estado = fila
        
        pelicula = self.obtener_pelicula_por_titulo(pel_titulo)
        sala = self.obtener_sala_por_numero(sala_num)
        
        if not pelicula or not sala:
            return None
            
        return Sesion(id_sesion, pelicula, sala, fecha_hora,
                      numero_asientos_ocupados=ocupados, estado_sesion=estado)

    def obtener_sesion_por_id(self, id_sesion):
        fila = self._ejecutar_consulta("SELECT * FROM sesiones WHERE id_sesion = ?", (id_sesion,), fetch_one=True)
        return self._mapear_sesion(fila)

    def listar_todas_las_sesiones(self):
        filas = self._ejecutar_consulta("SELECT * FROM sesiones", fetch_all=True)
        return [self._mapear_sesion(f) for f in filas]

    # --- ENTRADAS ---
    def guardar_entrada(self, e):
        query = """
            INSERT INTO entradas (id_entrada, sesion_id, precio_euros, categoria_tarifa, fecha_venta)
            VALUES (?, ?, ?, ?, ?)
        """
        fecha_str = e.fecha_venta.strftime("%Y-%m-%d %H:%M:%S") if isinstance(e.fecha_venta, datetime) else str(e.fecha_venta)
        self._ejecutar_consulta(query, (
            e.id_entrada, e.sesion.id_sesion, e.precio_euros, e.categoria_tarifa, fecha_str
        ), commit=True)

    def _mapear_entrada(self, fila):
        if not fila:
            return None
        id_entrada, sesion_id, precio, categoria, fecha_venta = fila
        
        sesion = self.obtener_sesion_por_id(sesion_id)
        if not sesion:
            return None
        
        try:
            fecha_dt = datetime.strptime(fecha_venta, "%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            fecha_dt = fecha_venta
            
        return Entrada(sesion, precio, categoria, id_entrada=id_entrada, fecha_venta=fecha_dt)

    def listar_todas_las_entradas(self):
        filas = self._ejecutar_consulta("SELECT * FROM entradas", fetch_all=True)
        return [self._mapear_entrada(f) for f in filas]

    def eliminar_entrada(self, id_entrada):
        fila = self._ejecutar_consulta("SELECT * FROM entradas WHERE id_entrada = ?", (id_entrada,), fetch_one=True)
        entrada = self._mapear_entrada(fila)
        if entrada:
            self._ejecutar_consulta("DELETE FROM entradas WHERE id_entrada = ?", (id_entrada,), commit=True)
            return entrada
        return None
