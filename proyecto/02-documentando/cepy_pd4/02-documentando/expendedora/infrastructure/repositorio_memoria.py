"""Infraestructura: repositorio en memoria para productos."""

from expendedora.domain.repositorio_productos import RepositorioProductos


class RepositorioProductosMemoria(RepositorioProductos):
    """Repositorio simple basado en diccionario en memoria."""
    def __init__(self):
        """Inicializa el almacenamiento por codigo."""
        self._por_codigo = {}

    def guardar(self, item):
        """Guarda un item; evita sobrescrituras por codigo."""
        if item.codigo in self._por_codigo:
            raise ValueError("El codigo ya existe.")
        self._por_codigo[item.codigo] = item

    def obtener(self, codigo):
        """Devuelve un item o None si no existe."""
        return self._por_codigo.get(codigo)

    def listar(self):
        """Devuelve una lista de items almacenados."""
        # Nota: se devuelve en el orden de inserción del dict.
        # Si se requiere un orden estable por código, ordenar aquí.
        return list(self._por_codigo.values())
