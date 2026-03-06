from expendedora.infrastructure.datos_iniciales import crear_repositorio_con_datos
from expendedora.domain.maquina import MaquinaExpendedora
from expendedora.application.servicios import ServicioExpendedora


def mostrar_menu():
    """Muestra las opciones de la maquina."""
    print("\n=== MAQUINA EXPENDEDORA ===")
    print("1. Mostrar productos")
    print("2. Seleccionar producto")
    print("3. Insertar dinero")
    print("4. Comprar")
    print("5. Cancelar")
    print("6. Reponer")
    print("7. Agregar producto")
    print("8. Agregar producto con descuento")
    print("9. Salir")


def opcion_mostrar(servicio):
    productos = servicio.listar_productos()
    if not productos:
        print("(No hay productos)")
    else:
        for codigo, nombre, precio, cantidad in productos:
            print(f"{codigo} - {nombre} - {precio:.2f} EUR - stock {cantidad}")


def opcion_seleccionar(servicio):
    codigo = input("Codigo: ").strip().upper()
    servicio.seleccionar(codigo)
    print("Producto seleccionado.")


def opcion_insertar(servicio):
    cantidad = float(input("Cantidad a insertar: ").strip())
    servicio.insertar_dinero(cantidad)
    print("Saldo actualizado.")


def opcion_comprar(servicio):
    cambio = servicio.comprar()
    print(f"Compra realizada. Cambio: {cambio:.2f} EUR")


def opcion_cancelar(servicio):
    devuelto = servicio.cancelar()
    print(f"Operacion cancelada. Devuelto: {devuelto:.2f} EUR")


def opcion_reponer(servicio):
    codigo = input("Codigo: ").strip().upper()
    unidades = int(input("Unidades a reponer: ").strip())
    servicio.reponer(codigo, unidades)
    print("Stock actualizado.")


def opcion_agregar_producto(servicio):
    codigo = input("Codigo: ").strip().upper()
    nombre = input("Nombre: ").strip()
    precio = float(input("Precio: ").strip())
    cantidad = int(input("Cantidad: ").strip())
    servicio.agregar_producto(codigo, nombre, precio, cantidad)
    print("Producto agregado.")


def opcion_agregar_producto_con_descuento(servicio):
    # Pide datos y agrega un producto con descuento
    codigo = input("Codigo: ").strip().upper()
    nombre = input("Nombre: ").strip()
    precio = float(input("Precio: ").strip())
    cantidad = int(input("Cantidad: ").strip())
    porcentaje = float(input("Porcentaje descuento: ").strip())
    servicio.agregar_producto_con_descuento(codigo, nombre, precio, cantidad, porcentaje)
    print("Producto con descuento agregado.")


def main():
    repo = crear_repositorio_con_datos()
    maquina = MaquinaExpendedora(repo)
    servicio = ServicioExpendedora(maquina)
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()
        try:
            if opcion == "1":
                opcion_mostrar(servicio)
            elif opcion == "2":
                opcion_seleccionar(servicio)
            elif opcion == "3":
                opcion_insertar(servicio)
            elif opcion == "4":
                opcion_comprar(servicio)
            elif opcion == "5":
                opcion_cancelar(servicio)
            elif opcion == "6":
                opcion_reponer(servicio)
            elif opcion == "7":
                opcion_agregar_producto(servicio)
            elif opcion == "8":
                opcion_agregar_producto_con_descuento(servicio)
            elif opcion == "9":
                print("Hasta luego.")
                break
            else:
                print("Opcion no valida.")
        except ValueError as e:
            print("X " + str(e))


if __name__ == "__main__":
    main()
