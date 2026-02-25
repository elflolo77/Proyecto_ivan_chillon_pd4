"""Dominio: Entidad Sesion."""

from cine_multiplex.domain.pelicula import Pelicula
from cine_multiplex.domain.sala import Sala

class Sesion:
    """Representa la proyección de una película en una sala y horario."""
    def __init__(self, id_sesion, pelicula: Pelicula, sala: Sala, fecha_hora):
        self._id = id_sesion
        self._pelicula = pelicula
        self._sala = sala
        self._fecha_hora = fecha_hora
        self._asientos_ocupados = 0
        self._estado = "programada" # programada, completa, cancelada

    @property
    def id(self):
        return self._id

    @property
    def pelicula(self):
        return self._pelicula

    @property
    def sala(self):
        return self._sala

    @property
    def fecha_hora(self):
        return self._fecha_hora

    @property
    def asientos_ocupados(self):
        return self._asientos_ocupados

    @property
    def capacidad_disponible(self):
        return self._sala.capacidad - self._asientos_ocupados

    def vender_entrada(self):
        """Intenta vender una entrada para esta sesión."""
        if self._estado == "cancelada":
            raise ValueError("La sesión está cancelada.")
        if self.capacidad_disponible <= 0:
            self._estado = "completa"
            raise ValueError("La sesión está completa.")
        
        self._asientos_ocupados += 1
        if self.capacidad_disponible == 0:
            self._estado = "completa"

    def anular_entrada(self):
        """Anula una entrada vendida."""
        if self._asientos_ocupados > 0:
            self._asientos_ocupados -= 1
            if self._estado == "completa" and self.capacidad_disponible > 0:
                self._estado = "programada"

    def __str__(self):
        return f"Sesion {self.id}: {self.pelicula.titulo} en Sala {self.sala.numero} a las {self.fecha_hora}"
