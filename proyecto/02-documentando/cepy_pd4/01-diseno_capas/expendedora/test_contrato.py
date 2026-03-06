from expendedora.domain.repositorio_productos import RepositorioProductos

repo = RepositorioProductos()
try:
    repo.listar()
except NotImplementedError as e:
    print(f"Excepcion capturada: {e}")
