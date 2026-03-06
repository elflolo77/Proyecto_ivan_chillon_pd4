from expendedora.domain.item import Item, ItemConDescuento
from expendedora.infrastructure.repositorio_memoria import RepositorioProductosMemoria


def crear_repositorio_con_datos():
    repo = RepositorioProductosMemoria()
    repo.guardar(Item("A1", "Agua", 1.00, 10))
    repo.guardar(Item("A2", "Papas", 1.50, 8))
    repo.guardar(ItemConDescuento("D1", "Refresco", 2.50, 5, 20))
    return repo
