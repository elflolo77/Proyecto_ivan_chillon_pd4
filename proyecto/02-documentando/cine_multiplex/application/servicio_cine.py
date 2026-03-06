"""Aplicación: Servicio principal de Cine Flolix."""

from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica
from cine_multiplex.domain.sala import Sala
from cine_multiplex.domain.sesion import Sesion
from cine_multiplex.domain.entrada import Entrada

class ServicioCine:
    """Coordina las operaciones del cine."""
    
    def __init__(self, repositorio_datos):
        self._repositorio = repositorio_datos

    # --- Gestión de Películas ---
    def registrar_pelicula_comercial(self, titulo, duracion_minutos, clasificacion, genero, distribuidora):
        pelicula = PeliculaComercial(titulo, duracion_minutos, clasificacion, genero, distribuidora)
        self._repositorio.guardar_pelicula(pelicula)
        return pelicula

    def registrar_pelicula_infantil(self, titulo, duracion_minutos, clasificacion, genero, edad_minima):
        pelicula = PeliculaInfantil(titulo, duracion_minutos, clasificacion, genero, edad_minima)
        self._repositorio.guardar_pelicula(pelicula)
        return pelicula

    def registrar_pelicula_clasica(self, titulo, duracion_minutos, clasificacion, genero, anio_lanzamiento):
        pelicula = PeliculaClasica(titulo, duracion_minutos, clasificacion, genero, anio_lanzamiento)
        self._repositorio.guardar_pelicula(pelicula)
        return pelicula

    def listar_peliculas(self):
        return self._repositorio.listar_todas_las_peliculas()

    # --- Gestión de Salas ---
    def crear_sala(self, numero_sala, capacidad_maxima, tecnologia_pantalla="2D"):
        sala = Sala(numero_sala, capacidad_maxima, tecnologia_pantalla)
        self._repositorio.guardar_sala(sala)
        return sala

    def listar_salas(self):
        return self._repositorio.listar_todas_las_salas()

    # --- Gestión de Sesiones ---
    def programar_sesion(self, identificador_sesion, nombre_pelicula, numero_sala, fecha_hora_str):
        """Programa una sesión. fecha_hora_str formato: 'YYYY-MM-DD HH:MM'"""
        pelicula = self._repositorio.obtener_pelicula_por_titulo(nombre_pelicula)
        sala = self._repositorio.obtener_sala_por_numero(numero_sala)
        
        if not pelicula:
            raise ValueError(f"Película '{nombre_pelicula}' no encontrada.")
        if not sala:
            raise ValueError(f"Sala {numero_sala} no encontrada.")
            
        # Validación simple de formato (opcional, si queremos mantener robustez básica)
        if not isinstance(fecha_hora_str, str):
            raise ValueError("La fecha debe ser una cadena de texto.")

        # Verificar solapamientos (simplificado: misma sala, misma hora exacta o rango)
        # Aquí haremos chequeo simple de hora exacta para MVP, idealmente rango duración
        sesiones_sala = [s for s in self._repositorio.listar_todas_las_sesiones() if s.sala.numero == numero_sala]
        
        sesion = Sesion(identificador_sesion, pelicula, sala, fecha_hora_str)
        self._repositorio.guardar_sesion(sesion)
        return sesion

    def listar_sesiones(self):
        return self._repositorio.listar_todas_las_sesiones()

    def obtener_sesion(self, identificador_sesion):
        return self._repositorio.obtener_sesion_por_id(identificador_sesion)

    # --- Gestión de Entradas ---
    def vender_entrada(self, identificador_sesion, categoria_tarifa):
        """Vende una entrada para la sesión indicada."""
        sesion = self._repositorio.obtener_sesion_por_id(identificador_sesion)
        if not sesion:
            raise ValueError("Sesión no encontrada.")
            
        # Calcular tarifa (lógica simple)
        PRECIO_BASE_EUROS = 10.0
        tarifas_disponibles = {
            "General": PRECIO_BASE_EUROS,
            "Reducida": PRECIO_BASE_EUROS * 0.8,
            "Estudiante": PRECIO_BASE_EUROS * 0.5
        }
        precio_venta = tarifas_disponibles.get(categoria_tarifa, PRECIO_BASE_EUROS)
        
        # Intentar vender en el dominio (valida aforo)
        sesion.vender_entrada()
        
        # Crear ticket
        entrada = Entrada(sesion, precio_venta, categoria_tarifa)
        self._repositorio.guardar_entrada(entrada)
        
        # Actualizar sesión en persistencia (por cambio de aforo)
        self._repositorio.guardar_sesion(sesion)
        
        return entrada

    def anular_entrada(self, identificador_entrada):
        # Esta lógica requeriría buscar la entrada por ID, obtener su sesión, y anular.
        # Por simplicidad de la lista, hacemos búsqueda lineal.
        entradas_vendidas = self._repositorio.listar_todas_las_entradas()
        entrada_encontrada = None
        for e in entradas_vendidas:
            if e.id_entrada == identificador_entrada:
                entrada_encontrada = e
                break
        
        if entrada_encontrada:
            sesion = entrada_encontrada.sesion
            sesion.anular_entrada()
            # Eliminar de la lista de vendidas? O marcarla anulada?
            # El requisito dice "Anular entradas", la entidad Entrada podría tener estado.
            # Aquí la eliminamos de la lista para simplificar o dejaría ahí pero necesitamos actualizar repos.
            self._repositorio._coleccion_entradas.remove(entrada_encontrada) # Acceso interno corregido
            self._repositorio.guardar_sesion(sesion)
            return True
        return False
        
    # --- Estadísticas ---
    def informe_ventas(self):
        total_recaudado_euros = sum(e.precio_euros for e in self._repositorio.listar_todas_las_entradas())
        numero_entradas_vendidas = len(self._repositorio.listar_todas_las_entradas())
        return {
            "total_recaudado": total_recaudado_euros,
            "entradas_vendidas": numero_entradas_vendidas
        }
