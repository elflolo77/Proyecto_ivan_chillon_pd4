"""Aplicación: Servicio principal de Cine Flolix."""

from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica
from cine_multiplex.domain.sala import Sala
from cine_multiplex.domain.sesion import Sesion
from cine_multiplex.domain.entrada import Entrada
from cine_multiplex.infrastructure.errores import EntidadNoEncontradaError, EntidadDuplicadaError

class ServicioCine:
    """Coordina las operaciones del cine."""
    
    def __init__(self, repositorio_datos):
        """Inicializa el servicio con su repositorio."""
        self._repositorio = repositorio_datos

    def registrar_pelicula_comercial(self, titulo, duracion_minutos, clasificacion, genero, distribuidora):
        """Registra una película comercial."""
        if self._repositorio.obtener_pelicula_por_titulo(titulo):
            raise EntidadDuplicadaError(f"La película '{titulo}' ya existe.")
        pelicula = PeliculaComercial(titulo, duracion_minutos, clasificacion, genero, distribuidora)
        self._repositorio.guardar_pelicula(pelicula)
        return pelicula

    def registrar_pelicula_infantil(self, titulo, duracion_minutos, clasificacion, genero, edad_minima):
        """Registra una película infantil."""
        if self._repositorio.obtener_pelicula_por_titulo(titulo):
            raise EntidadDuplicadaError(f"La película '{titulo}' ya existe.")
        pelicula = PeliculaInfantil(titulo, duracion_minutos, clasificacion, genero, edad_minima)
        self._repositorio.guardar_pelicula(pelicula)
        return pelicula

    def registrar_pelicula_clasica(self, titulo, duracion_minutos, clasificacion, genero, anio_lanzamiento):
        """Registra una película clásica."""
        if self._repositorio.obtener_pelicula_por_titulo(titulo):
            raise EntidadDuplicadaError(f"La película '{titulo}' ya existe.")
        pelicula = PeliculaClasica(titulo, duracion_minutos, clasificacion, genero, anio_lanzamiento)
        self._repositorio.guardar_pelicula(pelicula)
        return pelicula

    def listar_peliculas(self):
        """Lista todas las películas."""
        return self._repositorio.listar_todas_las_peliculas()

    def crear_sala(self, numero_sala, capacidad_maxima, tecnologia_pantalla="2D"):
        """Crea una sala de cine."""
        if self._repositorio.obtener_sala_por_numero(numero_sala):
            raise EntidadDuplicadaError(f"La sala {numero_sala} ya existe.")
        sala = Sala(numero_sala, capacidad_maxima, tecnologia_pantalla)
        self._repositorio.guardar_sala(sala)
        return sala

    def listar_salas(self):
        """Lista todas las salas."""
        return self._repositorio.listar_todas_las_salas()

    def programar_sesion(self, identificador_sesion, nombre_pelicula, numero_sala, fecha_hora_str):
        """Programa una sesión (Formato: 'YYYY-MM-DD HH:MM')."""
        pelicula = self._repositorio.obtener_pelicula_por_titulo(nombre_pelicula)
        sala = self._repositorio.obtener_sala_por_numero(numero_sala)
        
        if not pelicula:
            raise EntidadNoEncontradaError(f"Película '{nombre_pelicula}' no encontrada.")
        if not sala:
            raise EntidadNoEncontradaError(f"Sala {numero_sala} no encontrada.")
            


        if self._repositorio.obtener_sesion_por_id(identificador_sesion):
            raise EntidadDuplicadaError(f"ID de sesión '{identificador_sesion}' ya existe.")

        for sesion_existente in self._repositorio.listar_todas_las_sesiones():
            if sesion_existente.sala.numero == numero_sala and sesion_existente.fecha_hora == fecha_hora_str:
                raise EntidadDuplicadaError(f"Ya existe una sesión en la sala {numero_sala} a las {fecha_hora_str}.")

        sesion = Sesion(identificador_sesion, pelicula, sala, fecha_hora_str)
        self._repositorio.guardar_sesion(sesion)
        return sesion

    def listar_sesiones(self):
        """Lista todas las sesiones."""
        return self._repositorio.listar_todas_las_sesiones()

    def obtener_sesion(self, identificador_sesion):
        """Recupera una sesión por ID."""
        sesion = self._repositorio.obtener_sesion_por_id(identificador_sesion)
        if not sesion:
            raise EntidadNoEncontradaError(f"Sesión '{identificador_sesion}' no encontrada.")
        return sesion

    def obtener_pelicula(self, titulo):
        """Recupera una película por título."""
        pelicula = self._repositorio.obtener_pelicula_por_titulo(titulo)
        if not pelicula:
            raise EntidadNoEncontradaError(f"Película '{titulo}' no encontrada.")
        return pelicula

    def vender_entrada(self, identificador_sesion, categoria_tarifa):
        """Vende una entrada aplicando la política de precios."""
        sesion = self._repositorio.obtener_sesion_por_id(identificador_sesion)
        if not sesion:
            raise EntidadNoEncontradaError("Sesión no encontrada.")
            
        # Regla de negocio: precios según categoría
        PRECIO_BASE_EUROS = 10.0
        tarifas_disponibles = {
            "General": PRECIO_BASE_EUROS,
            "Reducida": PRECIO_BASE_EUROS * 0.8,
            "Estudiante": PRECIO_BASE_EUROS * 0.5
        }
        if categoria_tarifa not in tarifas_disponibles:
            raise ValueError(f"Tarifa '{categoria_tarifa}' no válida. Opciones: {list(tarifas_disponibles.keys())}")
        precio_venta = tarifas_disponibles[categoria_tarifa]
        
        sesion.vender_entrada()
        
        entrada = Entrada(sesion, precio_venta, categoria_tarifa)
        self._repositorio.guardar_entrada(entrada)
        self._repositorio.guardar_sesion(sesion)
        
        return entrada

    def anular_entrada(self, identificador_entrada):
        """Anula una entrada y libera el asiento."""
        entrada_encontrada = self._repositorio.eliminar_entrada(identificador_entrada)
        if entrada_encontrada:
            sesion = entrada_encontrada.sesion
            sesion.anular_entrada()
            self._repositorio.guardar_sesion(sesion)
            return True
        return False

    def informe_ventas(self):
        """Calcula el total recaudado y entradas vendidas."""
        total_recaudado_euros = sum(e.precio_euros for e in self._repositorio.listar_todas_las_entradas())
        numero_entradas_vendidas = len(self._repositorio.listar_todas_las_entradas())
        return {
            "total_recaudado": total_recaudado_euros,
            "entradas_vendidas": numero_entradas_vendidas
        }
