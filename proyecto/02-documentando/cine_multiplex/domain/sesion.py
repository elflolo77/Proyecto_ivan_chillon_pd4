"""Dominio: Entidad Sesion."""

from cine_multiplex.domain.pelicula import Pelicula
from cine_multiplex.domain.sala import Sala

class Sesion:
    """Representa la proyección de una película en una sala."""
    def __init__(self, id_sesion: str, pelicula: Pelicula, sala: Sala, fecha_hora: str):
        """Inicializa una sesión con película, sala y horario."""
        self._id_sesion = id_sesion
        self._pelicula = pelicula
        self._sala = sala
        self._fecha_hora = fecha_hora
        self._numero_asientos_ocupados = 0
        self._estado_sesion = "programada" # Estados: programada, completa, cancelada

    @property
    def id_sesion(self) -> str:
        """Devuelve el identificador de la sesión."""
        return self._id_sesion

    @property
    def pelicula(self) -> Pelicula:
        """Devuelve la película asociada."""
        return self._pelicula

    @property
    def sala(self) -> Sala:
        """Devuelve la sala asignada."""
        return self._sala

    @property
    def fecha_hora(self) -> str:
        """Devuelve el horario de la sesión."""
        return self._fecha_hora

    @property
    def numero_asientos_ocupados(self) -> int:
        """Devuelve el número de asientos vendidos."""
        return self._numero_asientos_ocupados

    @property
    def numero_asientos_libres(self) -> int:
        """Calcula las butacas disponibles (Capacidad - Ocupación)."""
        return self._sala.capacidad_maxima - self._numero_asientos_ocupados

    def vender_entrada(self):
        """Registra una venta e incrementa la ocupación."""
        # Regla: no vender si está cancelada o llena
        if self._estado_sesion == "cancelada":
            raise ValueError("La sesión está cancelada.")
        if self.numero_asientos_libres <= 0:
            self._estado_sesion = "completa"
            raise ValueError("La sesión está completa.")
        
        self._numero_asientos_ocupados += 1
        if self.numero_asientos_libres == 0:
            self._estado_sesion = "completa"

    def anular_entrada(self):
        """Libera un asiento tras anulación."""
        if self._numero_asientos_ocupados > 0:
            self._numero_asientos_ocupados -= 1
            if self._estado_sesion == "completa" and self.numero_asientos_libres > 0:
                self._estado_sesion = "programada"

    def __str__(self) -> str:
        """Representación textual de la sesión."""
        return f"Sesion {self.id_sesion}: {self.pelicula.titulo} en Sala {self.sala.numero} a las {self.fecha_hora}"
