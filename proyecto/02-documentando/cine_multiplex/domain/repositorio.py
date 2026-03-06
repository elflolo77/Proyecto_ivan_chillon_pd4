"""Dominio: Interface del Repositorio."""

class RepositorioCine:
    """Interface para la persistencia de datos del cine."""

    # Peliculas
    def guardar_pelicula(self, nueva_pelicula):
        raise NotImplementedError

    def obtener_pelicula_por_titulo(self, nombre_pelicula):
        raise NotImplementedError
    
    def listar_todas_las_peliculas(self):
        raise NotImplementedError

    # Salas
    def guardar_sala(self, nueva_sala):
        raise NotImplementedError

    def obtener_sala_por_numero(self, numero_sala):
        raise NotImplementedError
    
    def listar_todas_las_salas(self):
        raise NotImplementedError

    # Sesiones
    def guardar_sesion(self, nueva_sesion):
        raise NotImplementedError
    
    def obtener_sesion_por_id(self, identificador_sesion):
        raise NotImplementedError

    def listar_todas_las_sesiones(self):
        raise NotImplementedError

    # Entradas / Ventas
    def guardar_entrada(self, nueva_entrada):
        raise NotImplementedError
    
    def listar_todas_las_entradas(self):
        raise NotImplementedError
