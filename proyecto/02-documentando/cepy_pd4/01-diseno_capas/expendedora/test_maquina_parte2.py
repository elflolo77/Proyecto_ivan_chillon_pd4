from expendedora.domain.item import Item
from expendedora.domain.maquina import MaquinaExpendedora

maquina = MaquinaExpendedora([Item("A1", "Agua", 1.00, 1)])

try:
    maquina.seleccionar("B9")
except ValueError as e:
    print("Error esperado:", e)

maquina.seleccionar("A1")
maquina.insertar_dinero(0.50)
try:
    maquina.comprar()
except ValueError as e:
    print("Error esperado:", e)

maquina.insertar_dinero(1.00)
cambio = maquina.comprar()
print("Cambio:", cambio)
