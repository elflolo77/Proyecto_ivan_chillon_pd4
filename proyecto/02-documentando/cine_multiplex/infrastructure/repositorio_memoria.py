"""Infraestructura: Repositorio en memoria."""
from cine_multiplex.domain.repositorio import RepositorioCine

class RepositorioMemoria(RepositorioCine):
    """Implementación en memoria del repositorio."""
    
    def __init__(self):
        """Inicializa el almacenamiento en memoria."""
        self.peliculas = {}
        self.salas = {}
        self.sesiones = {}
        self.entradas = []

    # --- Peliculas ---
    def guardar_pelicula(self, pelicula):
        """Guarda una película en memoria."""
        self.peliculas[pelicula.titulo] = pelicula

    def obtener_pelicula(self, titulo):
        """Busca una película por título."""
        return self.peliculas.get(titulo)

    def listar_peliculas(self):
        """Devuelve una lista de todas las películas."""
        return list(self.peliculas.values())

    # --- Salas ---
    def guardar_sala(self, sala):
        """Guarda una sala en memoria."""
        self.salas[sala.numero] = sala

    def obtener_sala(self, numero):
        """Busca una sala por número."""
        return self.salas.get(numero)

    def listar_salas(self):
        """Devuelve una lista de todas las salas."""
        return list(self.salas.values())

    # --- Sesiones ---
    def guardar_sesion(self, sesion):
        """Guarda una sesión en memoria."""
        self.sesiones[sesion.id] = sesion

    def obtener_sesion(self, id_sesion):
        """Busca una sesión por ID."""
        return self.sesiones.get(id_sesion)

    def listar_sesiones(self):
        """Devuelve una lista de todas las sesiones."""
        return list(self.sesiones.values())

    # --- Entradas ---
    def guardar_entrada(self, entrada):
        """Registra una entrada vendida."""
        self.entradas.append(entrada)

    def listar_entradas(self):
        """Devuelve todas las entradas vendidas."""
        return self.entradas
