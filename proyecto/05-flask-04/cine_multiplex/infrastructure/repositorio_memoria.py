"""Infraestructura: Repositorio en memoria."""
from cine_multiplex.domain.repositorio import RepositorioCine
from cine_multiplex.infrastructure.errores import EntidadNoEncontradaError, EntidadDuplicadaError

class RepositorioMemoria(RepositorioCine):
    """Implementación en memoria del repositorio."""
    
    def __init__(self):
        """Inicializa las colecciones en memoria."""
        self._coleccion_peliculas = {}
        self._coleccion_salas = {}
        self._coleccion_sesiones = {}
        self._coleccion_entradas = []

    def guardar_pelicula(self, nueva_pelicula):
        """Almacena una película por título."""
        self._coleccion_peliculas[nueva_pelicula.titulo] = nueva_pelicula

    def obtener_pelicula_por_titulo(self, nombre_pelicula):
        """Busca una película."""
        return self._coleccion_peliculas.get(nombre_pelicula)

    def listar_todas_las_peliculas(self):
        """Lista todas las películas."""
        return list(self._coleccion_peliculas.values())

    def guardar_sala(self, nueva_sala):
        """Almacena una sala por número."""
        self._coleccion_salas[nueva_sala.numero] = nueva_sala

    def obtener_sala_por_numero(self, numero_sala):
        """Busca una sala."""
        return self._coleccion_salas.get(numero_sala)

    def listar_todas_las_salas(self):
        """Lista todas las salas."""
        return list(self._coleccion_salas.values())

    def guardar_sesion(self, nueva_sesion):
        """Almacena una sesión por ID."""
        self._coleccion_sesiones[nueva_sesion.id_sesion] = nueva_sesion

    def obtener_sesion_por_id(self, identificador_sesion):
        """Busca una sesión."""
        return self._coleccion_sesiones.get(identificador_sesion)

    def listar_todas_las_sesiones(self):
        """Lista todas las sesiones."""
        return list(self._coleccion_sesiones.values())

    def guardar_entrada(self, nueva_entrada):
        """Añade una entrada al historial."""
        # Check if already exists to match domain exception expectation if any
        if any(e.id_entrada == nueva_entrada.id_entrada for e in self._coleccion_entradas):
            raise EntidadDuplicadaError(f"La entrada {nueva_entrada.id_entrada} ya existe.")
        self._coleccion_entradas.append(nueva_entrada)

    def listar_todas_las_entradas(self):
        """Lista todas las ventas."""
        return self._coleccion_entradas

    def eliminar_entrada(self, identificador_entrada):
        """Elimina una entrada por su identificador."""
        entrada_a_eliminar = next((entrada for entrada in self._coleccion_entradas if entrada.id_entrada == identificador_entrada), None)
        if entrada_a_eliminar:
            self._coleccion_entradas.remove(entrada_a_eliminar)
        return entrada_a_eliminar
