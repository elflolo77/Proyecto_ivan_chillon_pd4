from expendedora.domain.repositorio_productos import RepositorioProductos


class RepositorioProductosMemoria(RepositorioProductos):
    def __init__(self):
        self._por_codigo = {}

    def guardar(self, item):
        if item.codigo in self._por_codigo:
            raise ValueError("El codigo ya existe.")
        self._por_codigo[item.codigo] = item

    def obtener(self, codigo):
        return self._por_codigo.get(codigo)

    def listar(self):
        return list(self._por_codigo.values())
