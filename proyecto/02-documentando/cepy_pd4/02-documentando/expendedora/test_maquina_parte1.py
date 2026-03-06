"""Pruebas manuales: alta de items y listado en maquina."""

from expendedora.domain.item import Item
from expendedora.domain.maquina import MaquinaExpendedora

maquina = MaquinaExpendedora()
maquina.agregar_item(Item("A1", "Agua", 1.00, 3))
maquina.agregar_producto("A2", "Patatas", 1.50, 2)

print("Listado:", maquina.mostrar_productos())

print("Duplicado")
try:
    maquina.agregar_item(Item("A1", "Agua", 1.00, 3))
except ValueError as e:
    print("Error esperado:", e)

print("Tipo invalido")
try:
    maquina.agregar_item("no es un item")
except ValueError as e:
    print("Error esperado:", e)
