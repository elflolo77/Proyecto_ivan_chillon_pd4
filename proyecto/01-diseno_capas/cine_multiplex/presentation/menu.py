"""Presentación: Menú de consola."""

from cine_multiplex.application.servicio_cine import ServicioCine

class MenuCine:
    def __init__(self, servicio: ServicioCine):
        self.servicio = servicio

    def limpiar_pantalla(self):
        print("\n" * 50)

    def mostrar_menu(self):
        print("\n--- CINE FLOLIX ---")
        print("1. Gestión de Películas")
        print("2. Gestión de Salas")
        print("3. Gestión de Sesiones")
        print("4. Venta de Entradas")
        print("5. Estadísticas")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_peliculas()
            elif opcion == "2":
                self.menu_salas()
            elif opcion == "3":
                self.menu_sesiones()
            elif opcion == "4":
                self.menu_ventas()
            elif opcion == "5":
                self.menu_estadisticas()
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    def menu_peliculas(self):
        print("\n--- Películas ---")
        print("1. Listar películas")
        print("2. Registrar Comercial")
        print("3. Registrar Infantil")
        print("4. Registrar Clásica")
        op = input("Opción: ")
        
        if op == "1":
            try:
                lista = self.servicio.listar_peliculas()
                for p in lista:
                    print(p.mostrar_info())
            except Exception as e:
                print(f"Error: {e}")
        elif op in ["2", "3", "4"]:
            titulo = input("Título: ")
            
            try:
                duracion = int(input("Duración (min): "))
                clasif = input("Clasificación: ")
                genero = input("Género: ")
                if op == "2":
                    dist = input("Distribuidora: ")
                    self.servicio.registrar_pelicula_comercial(titulo, duracion, clasif, genero, dist)
                elif op == "3":
                    edad = int(input("Edad mínima: "))
                    self.servicio.registrar_pelicula_infantil(titulo, duracion, clasif, genero, edad)
                elif op == "4":
                    anio = int(input("Año estreno: "))
                    self.servicio.registrar_pelicula_clasica(titulo, duracion, clasif, genero, anio)
                print("Película registrada.")
            except ValueError as e:
                print(f"Error de validación: {e}")
            except Exception as e:
                print(f"Error: {e.args}")

    def menu_salas(self):
        print("\n--- Salas ---")
        print("1. Listar salas")
        print("2. Crear sala")
        op = input("Opción: ")
        
        if op == "1":
            for s in self.servicio.listar_salas():
                print(s)
        elif op == "2":
            try:
                num = int(input("Número de sala: "))
                cap = int(input("Capacidad: "))
                pantalla = input("Tipo de pantalla (2D/3D/IMAX): ")
                self.servicio.crear_sala(num, cap, pantalla)
                print("Sala creada.")
            except ValueError:
                print("Datos numéricos inválidos.")

    def menu_sesiones(self):
        print("\n--- Sesiones ---")
        print("1. Listar sesiones")
        print("2. Programar sesión")
        op = input("Opción: ")
        
        if op == "1":
            for s in self.servicio.listar_sesiones():
                estado = "LLENA" if s.capacidad_disponible == 0 else f"Libres: {s.capacidad_disponible}"
                print(f"{s} | {estado}")
        elif op == "2":
            id_ses = input("ID Sesión (único): ")
            pelicula = input("Título Película: ")
            try:
                sala = int(input("Número Sala: "))
                fecha = input("Fecha (YYYY-MM-DD HH:MM): ")
                self.servicio.programar_sesion(id_ses, pelicula, sala, fecha)
                print("Sesión programada.")
            except Exception as e:
                print(f"Error: {e}")

    def menu_ventas(self):
        print("\n--- Venta de Entradas ---")
        print("1. Vender Entrada")
        print("2. Anular Entrada")
        op = input("Opción: ")
        
        if op == "1":
            id_sesion = input("ID de Sesión: ")
            print("Tarifas: General, Reducida, Estudiante")
            tarifa = input("Tipo Tarifa: ")
            
            try:
                entrada = self.servicio.vender_entrada(id_sesion, tarifa)
                print(f"¡Entrada vendida! ID: {entrada.id} - Precio: ${entrada.tarifa}")
            except Exception as e:
                print(f"Error en venta: {e}")
        elif op == "2":
            id_entrada = input("ID de Entrada a anular: ")
            try:
                exito = self.servicio.anular_entrada(id_entrada)
                if exito:
                    print("Entrada anulada correctamente.")
                else:
                    print("No se encontró la entrada o no se pudo anular.")
            except Exception as e:
                print(f"Error al anular: {e}")

    def menu_estadisticas(self):
        stats = self.servicio.informe_ventas()
        print(f"\nTotal Recaudado: ${stats['total_recaudado']:.2f}")
        print(f"Entradas Vendidas: {stats['entradas_vendidas']}")
