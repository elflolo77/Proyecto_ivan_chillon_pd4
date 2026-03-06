"""Dominio: entidades de producto y descuentos."""


class Item:
    """Producto base con validaciones de codigo, nombre, precio y stock."""
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
        # Regla de negocio: el codigo identifica de forma unica un producto.
        # Normalizamos (strip + upper) para que " a1 " y "A1" representen el mismo codigo,
        # evitando duplicados por formato.
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
        # Aceptamos entradas como str (por ejemplo desde consola) y las normalizamos a float.
        # Nota: para dinero, en proyectos reales se prefiere usar céntimos (int) o Decimal
        # para evitar problemas de redondeo con float. Aquí se usa float por simplicidad.
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
        # Regla de negocio: el stock se maneja como unidades enteras (no se permiten fracciones).
        if not isinstance(valor, int):
            raise ValueError("La cantidad debe ser un entero >= 0.")
        if valor < 0:
            raise ValueError("La cantidad debe ser un entero >= 0.")
        self._cantidad = valor

    def precio_final(self):
        """Devuelve el precio base del producto."""
        return self._precio

    
    def mostrar_producto(self):
        """Devuelve un producto en formato para mostrarlo en consola."""
        precio_base = self.precio
        precio_final = self.precio_final()
        porcentaje_descuento = 0.0
        return (self.codigo, self.nombre, precio_base, precio_final, self.cantidad, porcentaje_descuento)


class ItemConDescuento(Item):
    """Producto con descuento porcentual aplicado al precio base."""
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
        # Regla de negocio: el descuento es un porcentaje en rango [0, 100].
        # 0 => sin descuento; 100 => el producto queda gratis.
        try:
            porcentaje = float(valor)
        except (TypeError, ValueError):
            raise ValueError("Descuento fuera de rango.")
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("Descuento fuera de rango.")
        self._porcentaje_descuento = porcentaje

    def precio_final(self):
        """Devuelve el precio con descuento aplicado."""
        # Aplicamos descuento porcentual sobre el precio base.
        return self.precio * (1 - self._porcentaje_descuento / 100)

    def mostrar_producto(self):
        """Devuelve un producto con descuento en formato para mostrarlo en consola."""
        precio_base = self.precio
        precio_final = self.precio_final()
        porcentaje_descuento = float(self.porcentaje_descuento)
        return (self.codigo, self.nombre, precio_base, precio_final, self.cantidad, porcentaje_descuento)
