"""Dominio: Entidad Entrada."""

import uuid
from cine_multiplex.domain.sesion import Sesion

class Entrada:
    """Representa una entrada vendida."""
    def __init__(self, sesion: Sesion, precio_euros: float, tipo_tarifa: str):
        """Inicializa una entrada.
        
        Args:
            sesion (Sesion): Sesión para la que es válida la entrada.
            precio_euros (float): Precio final pagado.
            tipo_tarifa (str): Categoría de la tarifa (General, Reducida, etc.).
        """
        # Regla de negocio: ID único generado automáticamente.
        self._id = str(uuid.uuid4())[:8]
        self._sesion = sesion
        self._precio_euros = precio_euros
        self._tipo_tarifa = tipo_tarifa # general, reducida, etc.
        self._fecha_venta = None # Se podría establecer al momento de creación

    @property
    def id(self):
        """Devuelve el ID único de la entrada."""
        return self._id

    @property
    def sesion(self):
        """Devuelve la sesión asociada."""
        return self._sesion

    @property
    def precio_euros(self):
        """Devuelve el precio en euros."""
        return self._precio_euros
    
    @property
    def tipo_tarifa(self):
        """Devuelve el tipo de tarifa aplicada."""
        return self._tipo_tarifa

    def __str__(self):
        """Devuelve una cadena con los detalles de la entrada."""
        return f"Entrada {self.id} | {self.sesion.pelicula.titulo} | {self._tipo_tarifa} (${self.precio_euros})"
