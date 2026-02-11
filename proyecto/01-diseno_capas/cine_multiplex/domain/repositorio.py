"""Dominio: Interface del Repositorio."""

class RepositorioCine:
    """Interface para la persistencia de datos del cine."""

    # Peliculas
    def guardar_pelicula(self, pelicula):
        raise NotImplementedError

    def obtener_pelicula(self, titulo):
        raise NotImplementedError
    
    def listar_peliculas(self):
        raise NotImplementedError

    # Salas
    def guardar_sala(self, sala):
        raise NotImplementedError

    def obtener_sala(self, numero):
        raise NotImplementedError
    
    def listar_salas(self):
        raise NotImplementedError

    # Sesiones
    def guardar_sesion(self, sesion):
        raise NotImplementedError
    
    def obtener_sesion(self, id_sesion):
        raise NotImplementedError

    def listar_sesiones(self):
        raise NotImplementedError

    # Entradas / Ventas
    def guardar_entrada(self, entrada):
        raise NotImplementedError
    
    def listar_entradas(self):
        raise NotImplementedError
