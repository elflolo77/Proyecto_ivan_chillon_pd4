"""Pruebas manuales de validacion para ItemConDescuento."""

from expendedora.domain.item import ItemConDescuento

print("Caso valido")
item = ItemConDescuento("D1", "Refresco", 2.50, 5, 20)
print("Precio base:", item.precio)
print("Precio final:", item.precio_final())

print("Porcentaje invalido (-1)")
try:
    ItemConDescuento("D2", "Refresco", 2.50, 5, -1)
except ValueError as e:
    print("Error esperado:", e)

print("Porcentaje invalido (120)")
try:
    ItemConDescuento("D3", "Refresco", 2.50, 5, 120)
except ValueError as e:
    print("Error esperado:", e)
