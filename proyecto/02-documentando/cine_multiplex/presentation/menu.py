"""Presentación: Menú de consola."""

from cine_multiplex.application.servicio_cine import ServicioCine

class MenuCine:
    """Clase principal para la interfaz de consola del usuario."""
    def __init__(self, servicio: ServicioCine):
        """Inicializa el menú con el servicio de cine."""
        self.servicio = servicio

    def limpiar_pantalla(self):
        """Limpia la consola (simulada)."""
        print("\n" * 50)

    def mostrar_menu(self):
        """Muestra las opciones principales del menú."""
        print("\n--- CINE FLOLIX ---")
        print("1. Gestión de Películas")
        print("2. Gestión de Salas")
        print("3. Gestión de Sesiones")
        print("4. Venta de Entradas")
        print("5. Estadísticas")
        print("0. Salir")

    def ejecutar(self):
        """Bucle principal de ejecución del menú."""
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
        """Submenú para gestión de películas."""
        print("\n--- Películas ---")
        print("1. Listar películas")
        print("2. Registrar Comercial")
        print("3. Registrar Infantil")
        print("4. Registrar Clásica")
        opcion_seleccionada = input("Opción: ")
        
        if opcion_seleccionada == "1":
            try:
                lista = self.servicio.listar_peliculas()
                for pelicula in lista:
                    print(pelicula.mostrar_info())
            except Exception as e:
                print(f"Error: {e}")
        elif opcion_seleccionada in ["2", "3", "4"]:
            titulo = input("Título: ")
            duracion_minutos = int(input("Duración (min): "))
            clasificacion = input("Clasificación: ")
            genero = input("Género: ")
            
            try:
                if opcion_seleccionada == "2":
                    distribuidora = input("Distribuidora: ")
                    self.servicio.registrar_pelicula_comercial(titulo, duracion_minutos, clasificacion, genero, distribuidora)
                elif opcion_seleccionada == "3":
                    edad_anios = int(input("Edad mínima (años): "))
                    self.servicio.registrar_pelicula_infantil(titulo, duracion_minutos, clasificacion, genero, edad_anios)
                elif opcion_seleccionada == "4":
                    anio_estreno = int(input("Año estreno: "))
                    self.servicio.registrar_pelicula_clasica(titulo, duracion_minutos, clasificacion, genero, anio_estreno)
                print("Película registrada.")
            except ValueError as e:
                print(f"Error de validación: {e}")
            except Exception as e:
                print(f"Error: {e.args}")

    def menu_salas(self):
        """Submenú para gestión de salas."""
        print("\n--- Salas ---")
        print("1. Listar salas")
        print("2. Crear sala")
        opcion_seleccionada = input("Opción: ")
        
        if opcion_seleccionada == "1":
            for sala in self.servicio.listar_salas():
                print(sala)
        elif opcion_seleccionada == "2":
            try:
                numero_sala = int(input("Número de sala: "))
                cap_personas = int(input("Capacidad (personas): "))
                pantalla = input("Tipo de pantalla (2D/3D/IMAX): ")
                self.servicio.crear_sala(numero_sala, cap_personas, pantalla)
                print("Sala creada.")
            except ValueError:
                print("Datos numéricos inválidos.")

    def menu_sesiones(self):
        """Submenú para gestión de sesiones."""
        print("\n--- Sesiones ---")
        print("1. Listar sesiones")
        print("2. Programar sesión")
        opcion_seleccionada = input("Opción: ")
        
        if opcion_seleccionada == "1":
            for sesion in self.servicio.listar_sesiones():
                estado = "LLENA" if sesion.capacidad_disponible == 0 else f"Libres: {sesion.capacidad_disponible}"
                print(f"{sesion} | {estado}")
        elif opcion_seleccionada == "2":
            id_sesion = input("ID Sesión (único): ")
            pelicula = input("Título Película: ")
            sala = int(input("Número Sala: "))
            fecha = input("Fecha (YYYY-MM-DD HH:MM): ")
            try:
                self.servicio.programar_sesion(id_sesion, pelicula, sala, fecha)
                print("Sesión programada.")
            except Exception as e:
                print(f"Error: {e}")

    def menu_ventas(self):
        """Submenú para venta de entradas."""
        print("\n--- Venta de Entradas ---")
        id_sesion = input("ID de Sesión: ")
        print("Tarifas: General, Reducida, Estudiante")
        tarifa = input("Tipo Tarifa: ")
        
        try:
            entrada = self.servicio.vender_entrada(id_sesion, tarifa)
            print(f"¡Entrada vendida! ID: {entrada.id} - Precio: ${entrada.precio_euros}")
        except Exception as e:
            print(f"Error en venta: {e}")

    def menu_estadisticas(self):
        """Muestra estadísticas de ventas."""
        stats = self.servicio.informe_ventas()
        print(f"\nTotal Recaudado: ${stats['total_recaudado']:.2f}")
        print(f"Entradas Vendidas: {stats['entradas_vendidas']}")
