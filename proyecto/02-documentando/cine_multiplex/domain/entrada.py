"""Dominio: Entidad Entrada."""

import uuid
from cine_multiplex.domain.sesion import Sesion

class Entrada:
    """Representa una entrada vendida para una sesión."""
    def __init__(self, sesion: Sesion, precio_euros: float, categoria_tarifa: str):
        """Inicializa una entrada con su sesión, precio y tarifa."""
        self._id_entrada = str(uuid.uuid4())[:8]
        self._sesion = sesion
        self._precio_euros = precio_euros # Importe cobrado (€)
        self._categoria_tarifa = categoria_tarifa # Ej: General, Reducida...
        self._fecha_venta = None # Reservado para uso futuro

    @property
    def id_entrada(self) -> str:
        """Devuelve el identificador único."""
        return self._id_entrada

    @property
    def sesion(self) -> Sesion:
        """Devuelve la sesión asociada."""
        return self._sesion

    @property
    def precio_euros(self) -> float:
        """Devuelve el precio en euros."""
        return self._precio_euros
    
    @property
    def categoria_tarifa(self) -> str:
        """Devuelve la categoría de tarifa."""
        return self._categoria_tarifa

    def __str__(self) -> str:
        """Representación textual de la entrada."""
        return f"Entrada {self.id_entrada} | {self.sesion.pelicula.titulo} | {self._categoria_tarifa} ({self.precio_euros}€)"
