"""Dominio: contrato de repositorio para productos."""


class RepositorioProductos:
    """Define la interfaz minima que requiere el dominio."""
    def guardar(self, item):
        """Guarda un item en el repositorio."""
        raise NotImplementedError

    def eliminar(self, codigo):
        """Elimina un item por su codigo (por ejemplo, cuando se queda sin stock)."""
        raise NotImplementedError

    def obtener(self, codigo):
        """Recupera un item por su codigo."""
        raise NotImplementedError

    def listar(self):
        """Devuelve una lista de items."""
        raise NotImplementedError
