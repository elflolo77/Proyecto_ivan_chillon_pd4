"""Infraestructura: Repositorio en memoria."""
from cineflolix.domain.repositorio import RepositorioCine

class RepositorioMemoria(RepositorioCine):
    """Implementación en memoria del repositorio."""
    
    def __init__(self):
        self.peliculas = {}
        self.salas = {}
        self.sesiones = {}
        self.entradas = []

    # --- Peliculas ---
    def guardar_pelicula(self, pelicula):
        self.peliculas[pelicula.titulo] = pelicula

    def obtener_pelicula(self, titulo):
        return self.peliculas.get(titulo)

    def listar_peliculas(self):
        return list(self.peliculas.values())

    # --- Salas ---
    def guardar_sala(self, sala):
        self.salas[sala.numero] = sala

    def obtener_sala(self, numero):
        return self.salas.get(numero)

    def listar_salas(self):
        return list(self.salas.values())

    # --- Sesiones ---
    def guardar_sesion(self, sesion):
        self.sesiones[sesion.id] = sesion

    def obtener_sesion(self, id_sesion):
        return self.sesiones.get(id_sesion)

    def listar_sesiones(self):
        return list(self.sesiones.values())

    # --- Entradas ---
    def guardar_entrada(self, entrada):
        self.entradas.append(entrada)

    def listar_entradas(self):
        return self.entradas
