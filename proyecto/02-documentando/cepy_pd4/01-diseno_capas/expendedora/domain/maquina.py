"""Dominio: logica de la maquina expendedora."""

from expendedora.domain.item import Item


class MaquinaExpendedora:
    """Coordina la venta de productos y el saldo del usuario."""
    def __init__(self, repositorio):
        self._repo = repositorio
        self._saldo = 0.0
        self._seleccion = None

    @property
    def saldo(self):
        return self._saldo

    def agregar_item(self, item):
        if not isinstance(item, Item):
            raise ValueError("Solo se permiten objetos Item.")
        if self._repo.obtener(item.codigo) is not None:
            raise ValueError("El codigo ya existe.")
        self._repo.guardar(item)

    def agregar_producto(self, codigo, nombre, precio, cantidad):
        item = Item(codigo, nombre, precio, cantidad)
        self.agregar_item(item)

    def mostrar_productos(self):
        return [
            (item.codigo, item.nombre, item.precio_final(), item.cantidad)
            for item in self._repo.listar()
        ]

    def seleccionar(self, codigo):
        item = self._repo.obtener(codigo)
        if item is None:
            raise ValueError("El codigo no existe.")
        self._seleccion = item

    def insertar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        self._saldo += cantidad

    def _obtener_seleccion(self):
        if self._seleccion is None:
            raise ValueError("No hay producto seleccionado.")
        return self._seleccion

    def _validar_stock(self, item):
        if item.cantidad <= 0:
            raise ValueError("No hay stock disponible.")

    def _validar_saldo(self, precio):
        if self._saldo < precio:
            falta = precio - self._saldo
            raise ValueError(f"Saldo insuficiente. Faltan {falta:.2f} EUR.")

    def comprar(self):
        item = self._obtener_seleccion()
        self._validar_stock(item)
        precio = item.precio_final()
        self._validar_saldo(precio)
        item.cantidad = item.cantidad - 1
        if item.cantidad == 0:
            self._repo.eliminar(item.codigo)
        cambio = self._saldo - precio
        self._saldo = 0.0
        self._seleccion = None
        return cambio

    def cancelar(self):
        devuelto = self._saldo
        self._saldo = 0.0
        self._seleccion = None
        return devuelto

    def reponer(self, codigo, unidades):
        if unidades < 0:
            raise ValueError("Las unidades deben ser >= 0.")
        item = self._repo.obtener(codigo)
        if item is None:
            raise ValueError("El codigo no existe.")
        item.cantidad = item.cantidad + unidades
