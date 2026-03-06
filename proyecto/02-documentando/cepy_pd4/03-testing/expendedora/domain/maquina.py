"""Dominio: logica de la maquina expendedora."""

from expendedora.domain.item import Item


class MaquinaExpendedora:
    """Coordina la venta de productos y el saldo del usuario."""
    def __init__(self, repositorio):
        """Inicializa la maquina con un repositorio de productos."""
        # El repositorio es un adaptador de infraestructura. El dominio solo necesita el contrato
        # (guardar/obtener/listar/eliminar) para poder vender y mantener el catálogo.
        self._repo = repositorio
        self._saldo = 0.0
        self._seleccion = None

    @property
    def saldo(self):
        """Devuelve el saldo actual insertado en la maquina."""
        return self._saldo

    def agregar_item(self, item):
        """Agrega un Item al repositorio, validando tipo y codigo."""
        if not isinstance(item, Item):
            raise ValueError("Solo se permiten objetos Item.")
        if self._repo.obtener(item.codigo) is not None:
            raise ValueError("El codigo ya existe.")
        # En este punto el Item ya normalizó/validó su código, y comprobamos unicidad en repositorio.
        self._repo.guardar(item)

    def agregar_producto(self, codigo, nombre, precio, cantidad):
        """Crea un Item y lo agrega al repositorio."""
        item = Item(codigo, nombre, precio, cantidad)
        self.agregar_item(item)

    def mostrar_productos(self):
        """Devuelve una lista de productos (codigo, nombre, precio, stock)."""
        return [
            item.mostrar_producto()
            for item in self._repo.listar()
        ]

    def seleccionar(self, codigo):
        """Selecciona un producto por codigo para futuras operaciones."""
        item = self._repo.obtener(codigo)
        if item is None:
            raise ValueError("El codigo no existe.")
        # Guardamos la seleccion para que el resto de operaciones trabajen sobre ella.
        self._seleccion = item

    def insertar_dinero(self, cantidad):
        """Inserta dinero en la maquina; la cantidad debe ser positiva."""
        if cantidad <= 0:
            # No permitimos valores negativos o cero para evitar "retirar saldo" o estados incoherentes.
            raise ValueError("La cantidad debe ser positiva.")
        self._saldo += cantidad

    def _obtener_seleccion(self):
        """Devuelve el item seleccionado o lanza error si no hay seleccion."""
        if self._seleccion is None:
            raise ValueError("No hay producto seleccionado.")
        return self._seleccion

    def _validar_stock(self, item):
        """Valida que el item tenga stock disponible."""
        if item.cantidad <= 0:
            raise ValueError("No hay stock disponible.")

    def _validar_saldo(self, precio):
        """Valida que el saldo sea suficiente para el precio dado."""
        if self._saldo < precio:
            falta = precio - self._saldo
            raise ValueError(f"Saldo insuficiente. Faltan {falta:.2f} EUR.")

    def comprar(self):
        """Realiza la compra del item seleccionado y devuelve el cambio."""
        item = self._obtener_seleccion()
        self._validar_stock(item)
        precio = item.precio_final()
        self._validar_saldo(precio)
        # Regla de negocio: una compra reduce el stock en 1 unidad.
        item.cantidad = item.cantidad - 1
        if item.cantidad == 0:
            # Eliminamos el item sin stock para que no se muestre en el catalogo.
            self._repo.eliminar(item.codigo)
        cambio = self._saldo - precio
        # Reiniciamos el estado para evitar compras encadenadas con saldo residual.
        self._saldo = 0.0
        self._seleccion = None
        return cambio

    def cancelar(self):
        """Cancela la operacion y devuelve el saldo actual."""
        devuelto = self._saldo
        # Al cancelar, restablecemos el estado completo.
        self._saldo = 0.0
        self._seleccion = None
        return devuelto

    def reponer(self, codigo, unidades):
        """Repone unidades de un producto existente."""
        if unidades < 0:
            # Reponer con negativo equivaldría a "quitar stock"; esa operación no está soportada aquí.
            raise ValueError("Las unidades deben ser >= 0.")
        item = self._repo.obtener(codigo)
        if item is None:
            raise ValueError("El codigo no existe.")
        item.cantidad = item.cantidad + unidades
