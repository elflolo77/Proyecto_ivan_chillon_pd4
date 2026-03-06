class Item:
    def __init__(self, codigo, nombre, precio, cantidad):
        """Inicializa un producto y valida sus datos."""
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        """Valida el codigo con formato letra + numero."""
        # DONE: validar letra + numero
        texto = (valor or "").strip().upper()
        if len(texto) < 2:
            raise ValueError("Codigo invalido.")
        if not texto[0].isalpha() or not texto[1:].isdigit():
            raise ValueError("Codigo invalido.")
        self._codigo = texto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Valida nombre no vacio y sin espacios laterales."""
        texto = valor or ""
        if not texto.strip():
            raise ValueError("El nombre no puede estar vacio.")
        if texto != texto.strip():
            raise ValueError("El nombre no puede tener espacios laterales.")
        self._nombre = texto

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        """Valida precio mayor que 0."""
        # DONE: validar precio > 0
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser mayor que 0.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self._precio = precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        """Valida cantidad entera mayor o igual que 0."""
        # DONE: validar entero >= 0
        if not isinstance(valor, int):
            raise ValueError("La cantidad debe ser un entero >= 0.")
        if valor < 0:
            raise ValueError("La cantidad debe ser un entero >= 0.")
        self._cantidad = valor

    def precio_final(self):
        """Devuelve el precio base del producto."""
        return self._precio


class ItemConDescuento(Item):
    def __init__(self, codigo, nombre, precio, cantidad, porcentaje_descuento):
        """Inicializa un item con descuento y valida el porcentaje."""
        super().__init__(codigo, nombre, precio, cantidad)
        self.porcentaje_descuento = porcentaje_descuento

    @property
    def porcentaje_descuento(self):
        return self._porcentaje_descuento

    @porcentaje_descuento.setter
    def porcentaje_descuento(self, valor):
        """Valida descuento entre 0 y 100."""
        # DONE: validar 0 <= valor <= 100
        try:
            porcentaje = float(valor)
        except (TypeError, ValueError):
            raise ValueError("Descuento fuera de rango.")
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("Descuento fuera de rango.")
        self._porcentaje_descuento = porcentaje

    def precio_final(self):
        """Devuelve el precio con descuento aplicado."""
        # DONE: aplicar descuento
        return self.precio * (1 - self._porcentaje_descuento / 100)
