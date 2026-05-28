"""Módulo para los tickets o entradas del cine."""

import uuid
from datetime import datetime
from cine_multiplex.domain.sesion import Sesion

class Entrada:
    """Ticket de compra para ver una película."""
    def __init__(self, sesion, precio_euros, categoria_tarifa, id_entrada=None, fecha_venta=None):
        """Guarda la sesión elegida y a cuánto se ha vendido.

        Los parámetros opcionales id_entrada y fecha_venta permiten reconstruir
        una entrada ya persistida en BD sin acceder a atributos protegidos.
        """
        self._id_entrada = id_entrada if id_entrada is not None else str(uuid.uuid4())[:8]
        self._sesion = sesion
        self._precio_euros = precio_euros
        self._categoria_tarifa = categoria_tarifa
        self._fecha_venta = fecha_venta if fecha_venta is not None else datetime.now()

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

    @property
    def fecha_venta(self):
        """Fecha y hora en que se vendió la entrada."""
        return self._fecha_venta

    def __str__(self):
        """Texto para imprimir los datos de la entrada por pantalla."""
        return f"Entrada {self.id_entrada} | {self.sesion.pelicula.titulo} | {self._categoria_tarifa} ({self.precio_euros}€)"
