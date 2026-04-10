"""Módulo para los tickets o entradas del cine."""

import uuid
from datetime import datetime
from cine_multiplex.domain.sesion import Sesion

class Entrada:
    """Ticket de compra para ver una película."""
    def __init__(self, sesion, precio_euros, categoria_tarifa):
        """Guarda la sesión elegida y a cuánto se ha vendido."""
        self._id_entrada = str(uuid.uuid4())[:8]
        self._sesion = sesion
        self._precio_euros = precio_euros
        self._categoria_tarifa = categoria_tarifa
        self._fecha_venta = datetime.now()

    @property
    def id_entrada(self):
        """Devuelve el código único del ticket."""
        return self._id_entrada

    @property
    def sesion(self):
        """Sesión a la que pertenece."""
        return self._sesion

    @property
    def precio_euros(self):
        """Lo que costó la entrada."""
        return self._precio_euros
    
    @property
    def categoria_tarifa(self):
        """El tipo de descuento o tarifa aplicada al vender."""
        return self._categoria_tarifa

    def __str__(self):
        """Texto para imprimir los datos de la entrada por pantalla."""
        return f"Entrada {self.id_entrada} | {self.sesion.pelicula.titulo} | {self._categoria_tarifa} ({self.precio_euros}€)"
