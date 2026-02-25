"""Dominio: Entidad Entrada."""

import uuid
from cine_multiplex.domain.sesion import Sesion

class Entrada:
    """Representa una entrada vendida."""
    def __init__(self, sesion: Sesion, tarifa: float, tipo_tarifa: str):
        self._id = str(uuid.uuid4())[:8]
        self._sesion = sesion
        self._tarifa = tarifa
        self._tipo_tarifa = tipo_tarifa # general, reducida, etc.
        self._fecha_venta = None # Se podría establecer al momento de creación

    @property
    def id(self):
        return self._id

    @property
    def sesion(self):
        return self._sesion

    @property
    def tarifa(self):
        return self._tarifa
    
    @property
    def tipo_tarifa(self):
        return self._tipo_tarifa

    def __str__(self):
        return f"Entrada {self.id} | {self.sesion.pelicula.titulo} | {self._tipo_tarifa} (${self.tarifa})"
