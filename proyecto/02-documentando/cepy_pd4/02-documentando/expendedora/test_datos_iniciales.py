from expendedora.infrastructure.datos_iniciales import crear_items_iniciales
from expendedora.domain.maquina import MaquinaExpendedora

items = crear_items_iniciales()
maquina = MaquinaExpendedora(items)
print("Listado:", maquina.mostrar_productos())
