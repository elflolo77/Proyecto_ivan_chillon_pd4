"""Dominio: Interfaz del Repositorio."""

class RepositorioCine:
    """Interfaz para la persistencia de datos del cine."""

    # Peliculas
    # Peliculas
    def guardar_pelicula(self, pelicula):
        """Guarda una película en el repositorio."""
        raise NotImplementedError

    def obtener_pelicula(self, titulo):
        """Obtiene una película por su título."""
        raise NotImplementedError
    
    def listar_peliculas(self):
        """Lista todas las películas registradas."""
        raise NotImplementedError

    # Salas
    # Salas
    def guardar_sala(self, sala):
        """Guarda una sala en el repositorio."""
        raise NotImplementedError

    def obtener_sala(self, numero):
        """Obtiene una sala por su número."""
        raise NotImplementedError
    
    def listar_salas(self):
        """Lista todas las salas."""
        raise NotImplementedError

    # Sesiones
    # Sesiones
    def guardar_sesion(self, sesion):
        """Guarda una sesión."""
        raise NotImplementedError
    
    def obtener_sesion(self, id_sesion):
        """Obtiene una sesión por su ID."""
        raise NotImplementedError

    def listar_sesiones(self):
        """Lista todas las sesiones."""
        raise NotImplementedError

    # Entradas / Ventas
    # Entradas / Ventas
    def guardar_entrada(self, entrada):
        """Guarda una entrada vendida."""
        raise NotImplementedError
    
    def listar_entradas(self):
        """Lista todas las entradas vendidas."""
        raise NotImplementedError
