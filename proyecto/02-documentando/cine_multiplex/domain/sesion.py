"""Dominio: Entidad Sesion."""

from cine_multiplex.domain.pelicula import Pelicula
from cine_multiplex.domain.sala import Sala

class Sesion:
    """Representa la proyección de una película en una sala y horario."""
    def __init__(self, id_sesion, pelicula: Pelicula, sala: Sala, fecha_hora):
        """Inicializa una sesión.
        
        Args:
            id_sesion (str): Identificador único de la sesión.
            pelicula (Pelicula): Película a proyectar.
            sala (Sala): Sala donde se proyecta.
            fecha_hora (str): Fecha y hora de la función.
        """
        self._id = id_sesion
        self._pelicula = pelicula
        self._sala = sala
        self._fecha_hora = fecha_hora
        self._asientos_ocupados = 0
        # Estado inicial por defecto. Puede cambiar a 'completa' o 'cancelada'.
        self._estado = "programada" # programada, completa, cancelada

    @property
    def id(self):
        """Devuelve el ID de la sesión."""
        return self._id

    @property
    def pelicula(self):
        """Devuelve el objeto Pelicula de la sesión."""
        return self._pelicula

    @property
    def sala(self):
        """Devuelve el objeto Sala de la sesión."""
        return self._sala

    @property
    def fecha_hora(self):
        """Devuelve la fecha y hora de la sesión."""
        return self._fecha_hora

    @property
    def asientos_ocupados(self):
        """Devuelve el número de asientos ya vendidos."""
        return self._asientos_ocupados

    @property
    def capacidad_disponible(self):
        """Calcula cuántos asientos quedan libres."""
        return self._sala.capacidad_personas - self._asientos_ocupados

    def vender_entrada(self):
        """Intenta vender una entrada para esta sesión.
        
        Raises:
            ValueError: Si la sesión está cancelada o completa.
        """
        # Regla de negocio: No se puede vender si está cancelada.
        if self._estado == "cancelada":
            raise ValueError("La sesión está cancelada.")
        
        # Regla de negocio: No se puede vender si no hay aforo.
        if self.capacidad_disponible <= 0:
            self._estado = "completa"
            raise ValueError("La sesión está completa.")
        
        self._asientos_ocupados += 1
        
        # Actualización de estado: si se llena, pasa a completa.
        if self.capacidad_disponible == 0:
            self._estado = "completa"

    def anular_entrada(self):
        """Anula una entrada vendida y libera un asiento."""
        if self._asientos_ocupados > 0:
            self._asientos_ocupados -= 1
            # Regla de negocio: Si se libera un sitio en una sesión completa, vuelve a estar programada (disponible).
            if self._estado == "completa" and self.capacidad_disponible > 0:
                self._estado = "programada"

    def __str__(self):
        """Devuelve una descripción legible de la sesión."""
        return f"Sesion {self.id}: {self.pelicula.titulo} en Sala {self.sala.numero} a las {self.fecha_hora}"
