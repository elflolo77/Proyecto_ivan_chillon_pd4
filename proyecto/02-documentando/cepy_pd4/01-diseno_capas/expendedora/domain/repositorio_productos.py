class RepositorioProductos:
    def guardar(self, item):
        """Guarda un item en el repositorio."""
        raise NotImplementedError

    def obtener(self, codigo):
        """Recupera un item por su codigo."""
        raise NotImplementedError

    def listar(self):
        """Devuelve una lista de items."""
        raise NotImplementedError

