from expendedora.domain.item import Item
from expendedora.infrastructure.repositorio_memoria import RepositorioProductosMemoria

repo = RepositorioProductosMemoria()
repo.guardar(Item("A1", "Agua", 1.00, 1))
try:
    repo.guardar(Item("A1", "Agua", 1.00, 1))
except ValueError as e:
    print("Error esperado:", e)
