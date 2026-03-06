"""Dominio: Entidad Sesion."""

from cine_multiplex.domain.pelicula import Pelicula
from cine_multiplex.domain.sala import Sala

class Sesion:
    """Representa la proyección de una película en una sala y horario."""
    def __init__(self, id_sesion, pelicula: Pelicula, sala: Sala, fecha_hora):
        self._id_sesion = id_sesion
        self._pelicula = pelicula
        self._sala = sala
        self._fecha_hora = fecha_hora
        self._numero_asientos_ocupados = 0
        self._estado_sesion = "programada" # programada, completa, cancelada

    @property
    def id_sesion(self):
        return self._id_sesion

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
    def numero_asientos_ocupados(self):
        return self._numero_asientos_ocupados

    @property
    def numero_asientos_libres(self):
        return self._sala.capacidad_maxima - self._numero_asientos_ocupados

    def vender_entrada(self):
        """Intenta vender una entrada para esta sesión."""
        if self._estado_sesion == "cancelada":
            raise ValueError("La sesión está cancelada.")
        if self.numero_asientos_libres <= 0:
            self._estado_sesion = "completa"
            raise ValueError("La sesión está completa.")
        
        self._numero_asientos_ocupados += 1
        if self.numero_asientos_libres == 0:
            self._estado_sesion = "completa"

    def anular_entrada(self):
        """Anula una entrada vendida."""
        if self._numero_asientos_ocupados > 0:
            self._numero_asientos_ocupados -= 1
            if self._estado_sesion == "completa" and self.numero_asientos_libres > 0:
                self._estado_sesion = "programada"

    def __str__(self):
        return f"Sesion {self.id_sesion}: {self.pelicula.titulo} en Sala {self.sala.numero} a las {self.fecha_hora}"
