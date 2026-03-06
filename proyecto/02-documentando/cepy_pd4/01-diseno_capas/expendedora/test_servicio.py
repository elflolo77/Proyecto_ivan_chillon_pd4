from expendedora.domain.item import Item
from expendedora.domain.maquina import MaquinaExpendedora
from expendedora.application.servicios import ServicioExpendedora

maquina = MaquinaExpendedora([Item("A1", "Agua", 1.00, 2)])
servicio = ServicioExpendedora(maquina)

print("Productos:", servicio.listar_productos())
servicio.seleccionar("A1")
servicio.insertar_dinero(1.00)
print("Cambio:", servicio.comprar())
