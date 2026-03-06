from expendedora.domain.item import Item

print("Caso valido")
item_ok = Item("A1", "Agua", 1.00, 5)
print("Creado:", item_ok.codigo, item_ok.nombre, item_ok.precio, item_ok.cantidad)

print("Codigo invalido")
try:
    Item("AA", "Agua", 1.00, 5)
except ValueError as e:
    print("Error esperado:", e)

print("Nombre invalido (vacio)")
try:
    Item("A1", "", 1.00, 5)
except ValueError as e:
    print("Error esperado:", e)

print("Nombre invalido (espacios)")
try:
    Item("A1", "  Agua  ", 1.00, 5)
except ValueError as e:
    print("Error esperado:", e)

print("Precio invalido (0)")
try:
    Item("A1", "Agua", 0, 5)
except ValueError as e:
    print("Error esperado:", e)

print("Cantidad invalida (-1)")
try:
    Item("A1", "Agua", 1.00, -1)
except ValueError as e:
    print("Error esperado:", e)

print("Metodo precio_final")
print("Precio final:", item_ok.precio_final())
