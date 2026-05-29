"""Dominio: Entidad Sesion."""

from cine_multiplex.domain.pelicula import Pelicula
from cine_multiplex.domain.sala import Sala

class Sesion:
    """Representa la proyección de una película en una sala."""
    def __init__(self, id_sesion, pelicula, sala, fecha_hora,
                 numero_asientos_ocupados=0, estado_sesion="programada"):
        """Inicializa una sesión con película, sala y horario."""
        self._id_sesion = id_sesion
        self._pelicula = pelicula
        self._sala = sala
        self._fecha_hora = fecha_hora
        if numero_asientos_ocupados < 0 or numero_asientos_ocupados > sala.capacidad_maxima:
            raise ValueError("Ocupación inválida.")
        if estado_sesion not in ("programada", "completa", "cancelada"):
            raise ValueError("Estado inválido.")
        self._numero_asientos_ocupados = numero_asientos_ocupados
        self._estado_sesion = estado_sesion # Estados: programada, completa, cancelada

    @property
    def estado_sesion(self):
        """Devuelve el estado actual de la sesión."""
        return self._estado_sesion

    @property
    def id_sesion(self):
        """Devuelve el identificador de la sesión."""
        return self._id_sesion

    @property
    def pelicula(self):
        """Devuelve la película asociada."""
        return self._pelicula

    @property
    def sala(self):
        """Devuelve la sala asignada."""
        return self._sala

    @property
    def fecha_hora(self):
        """Devuelve el horario de la sesión."""
        return self._fecha_hora

    @property
    def numero_asientos_ocupados(self):
        """Devuelve el número de asientos vendidos."""
        return self._numero_asientos_ocupados

    @property
    def numero_asientos_libres(self):
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

    def to_dict(self):
        """Devuelve una representación en diccionario de la sesión."""
        return {
            "id_sesion": self.id_sesion,
            "pelicula": self.pelicula.to_dict() if self.pelicula else None,
            "sala": self.sala.to_dict() if self.sala else None,
            "fecha_hora": self.fecha_hora,
            "numero_asientos_ocupados": self.numero_asientos_ocupados,
            "numero_asientos_libres": self.numero_asientos_libres,
            "estado_sesion": self.estado_sesion
        }

    def __str__(self):
        """Representación textual de la sesión."""
        return f"Sesion {self.id_sesion}: {self.pelicula.titulo} en Sala {self.sala.numero} a las {self.fecha_hora}"
