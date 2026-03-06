from expendedora.domain.item import Item
from expendedora.domain.maquina import MaquinaExpendedora
from expendedora.infrastructure.repositorio_memoria import RepositorioProductosMemoria

repo = RepositorioProductosMemoria()
repo.guardar(Item("A1", "Agua", 1.00, 1))
maquina = MaquinaExpendedora(repo)
maquina.seleccionar("A1")
maquina.insertar_dinero(1.00)
maquina.comprar()
repo.eliminar("A1")
print(repo.obtener("A1"))  # Esperado: None
