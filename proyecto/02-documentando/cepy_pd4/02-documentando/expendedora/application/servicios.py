from expendedora.domain.item import ItemConDescuento
from expendedora.domain.maquina import MaquinaExpendedora


class ServicioExpendedora:
    def __init__(self, maquina):
        """Inicializa el servicio con la maquina a coordinar."""
        if not isinstance(maquina, MaquinaExpendedora):
            raise ValueError("Se requiere una MaquinaExpendedora.")
        self._maquina = maquina

    def listar_productos(self):
        """Devuelve el listado de productos."""
        return self._maquina.mostrar_productos()

    def seleccionar(self, codigo):
        """Selecciona un producto por codigo."""
        self._maquina.seleccionar(codigo)

    def insertar_dinero(self, cantidad):
        """Inserta dinero en la maquina."""
        self._maquina.insertar_dinero(cantidad)

    def comprar(self):
        """Realiza la compra y devuelve el cambio."""
        return self._maquina.comprar()

    def cancelar(self):
        """Cancela la operacion y devuelve el saldo."""
        return self._maquina.cancelar()

    def reponer(self, codigo, unidades):
        """Repone stock de un producto."""
        self._maquina.reponer(codigo, unidades)

    def agregar_producto(self, codigo, nombre, precio, cantidad):
        """Agrega un producto normal (sin descuento) a la maquina."""
        self._maquina.agregar_producto(codigo, nombre, precio, cantidad)

    def agregar_producto_con_descuento(self, codigo, nombre, precio, cantidad, porcentaje):
        """Agrega un producto con descuento a la maquina."""
        item = ItemConDescuento(codigo, nombre, precio, cantidad, porcentaje)
        self._maquina.agregar_item(item)
