"""Dominio: Interfaz del Repositorio."""

class RepositorioCine:
    """Interfaz para la persistencia de datos del cine."""

    def guardar_pelicula(self, nueva_pelicula):
        """Persiste una película en el sistema."""
        raise NotImplementedError

    def obtener_pelicula_por_titulo(self, nombre_pelicula):
        """Busca una película por su título."""
        raise NotImplementedError
    
    def listar_todas_las_peliculas(self):
        """Recupera todas las películas registradas."""
        raise NotImplementedError

    def guardar_sala(self, nueva_sala):
        """Persiste una sala de cine."""
        raise NotImplementedError

    def obtener_sala_por_numero(self, numero_sala):
        """Busca una sala por su número."""
        raise NotImplementedError
    
    def listar_todas_las_salas(self):
        """Recupera todas las salas configuradas."""
        raise NotImplementedError

    def guardar_sesion(self, nueva_sesion):
        """Persiste una sesión de proyección."""
        raise NotImplementedError
    
    def obtener_sesion_por_id(self, identificador_sesion):
        """Busca una sesión por su ID."""
        raise NotImplementedError

    def listar_todas_las_sesiones(self):
        """Recupera todas las sesiones programadas."""
        raise NotImplementedError

    def guardar_entrada(self, nueva_entrada):
        """Registra la venta de una entrada."""
        raise NotImplementedError
    
    def listar_todas_las_entradas(self):
        """Recupera el historial de entradas vendidas."""
        raise NotImplementedError

    def eliminar_entrada(self, identificador_entrada):
        """Elimina una entrada por su ID."""
        raise NotImplementedError
