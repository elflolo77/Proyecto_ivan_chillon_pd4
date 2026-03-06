"""Dominio: Entidad Entrada."""

import uuid
from cine_multiplex.domain.sesion import Sesion

class Entrada:
    """Representa una entrada vendida."""
    def __init__(self, sesion: Sesion, precio_euros: float, categoria_tarifa: str):
        self._id_entrada = str(uuid.uuid4())[:8]
        self._sesion = sesion
        self._precio_euros = precio_euros
        self._categoria_tarifa = categoria_tarifa # general, reducida, etc.
        self._fecha_venta = None # Se podría establecer al momento de creación

    @property
    def id_entrada(self):
        return self._id_entrada

    @property
    def sesion(self):
        return self._sesion

    @property
    def precio_euros(self):
        return self._precio_euros
    
    @property
    def categoria_tarifa(self):
        return self._categoria_tarifa

    def __str__(self):
        return f"Entrada {self.id_entrada} | {self.sesion.pelicula.titulo} | {self._categoria_tarifa} (${self.precio_euros})"
