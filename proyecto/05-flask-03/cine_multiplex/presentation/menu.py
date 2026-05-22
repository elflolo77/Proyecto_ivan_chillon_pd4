"""Presentación: Menú de consola."""

from cine_multiplex.application.servicio_cine import ServicioCine
from cine_multiplex.infrastructure.errores import (
    EntidadNoEncontradaError,
    EntidadDuplicadaError,
    ErrorIntegridadDatos,
    ErrorPersistencia
)
class MenuCine:
    """Clase para la interfaz de usuario en consola."""
    def __init__(self, servicio_cine):
        """Inicializa el menú con el servicio de cine."""
        self._servicio_cine = servicio_cine

    def mostrar_menu_principal(self):
        """Visualiza el menú principal."""
        print("\n--- CINE FLOLIX ---")
        print("1. Gestión de Películas")
        print("2. Gestión de Salas")
        print("3. Gestión de Sesiones")
        print("4. Venta de Entradas")
        print("5. Informe de Ventas")
        print("0. Salir")

    def ejecutar(self):
        """Bucle principal de ejecución."""
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.mostrar_menu_peliculas()
            elif opcion == "2":
                self.mostrar_menu_salas()
            elif opcion == "3":
                self.mostrar_menu_sesiones()
            elif opcion == "4":
                self.mostrar_menu_ventas()
            elif opcion == "5":
                self.mostrar_menu_estadisticas()
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    def mostrar_menu_peliculas(self):
        """Submenú de gestión de películas."""
        print("\n--- Películas ---")
        print("1. Listar películas")
        print("2. Registrar Comercial")
        print("3. Registrar Infantil")
        print("4. Registrar Clásica")
        opcion_seleccionada = input("Opción: ")
        
        if opcion_seleccionada == "1":
            try:
                lista_peliculas = self._servicio_cine.listar_peliculas()
                for pelicula in lista_peliculas:
                    print(pelicula.obtener_resumen_pelicula())
            except ErrorPersistencia as error:
                print(f"Error de base de datos: {error}")
            except Exception as error:
                print(f"Error inesperado: {error}")
        elif opcion_seleccionada in ["2", "3", "4"]:
            titulo = input("Título: ")
            try:
                duracion_minutos = int(input("Duración (min): "))
                clasificacion = input("Clasificación: ")
                genero = input("Género: ")

                if opcion_seleccionada == "2":
                    distribuidora = input("Distribuidora: ")
                    self._servicio_cine.registrar_pelicula_comercial(titulo, duracion_minutos, clasificacion, genero, distribuidora)
                elif opcion_seleccionada == "3":
                    edad_minima = int(input("Edad mínima: "))
                    self._servicio_cine.registrar_pelicula_infantil(titulo, duracion_minutos, clasificacion, genero, edad_minima)
                elif opcion_seleccionada == "4":
                    anio_lanzamiento = int(input("Año estreno: "))
                    self._servicio_cine.registrar_pelicula_clasica(titulo, duracion_minutos, clasificacion, genero, anio_lanzamiento)
                print("Película registrada.")
            except ValueError as error:
                print(f"Error de validación: {error}")
            except EntidadDuplicadaError as error:
                print(f"Error: La película ya está registrada. ({error})")
            except ErrorPersistencia as error:
                print(f"Error de persistencia: {error}")
            except Exception as error:
                print(f"Error inesperado: {error}")
        else:
            print("Opción no válida.")

    def mostrar_menu_salas(self):
        """Submenú de gestión de salas."""
        print("\n--- Salas ---")
        print("1. Listar salas")
        print("2. Crear sala")
        opcion_seleccionada = input("Opción: ")
        
        if opcion_seleccionada == "1":
            try:
                for sala in self._servicio_cine.listar_salas():
                    print(sala)
            except ErrorPersistencia as error:
                print(f"Error de base de datos: {error}")
            except Exception as error:
                print(f"Error inesperado: {error}")
        elif opcion_seleccionada == "2":
            try:
                numero_sala = int(input("Número de sala: "))
                capacidad_maxima = int(input("Capacidad: "))
                tecnologia_pantalla = input("Tipo de pantalla (2D/3D/IMAX): ")
                self._servicio_cine.crear_sala(numero_sala, capacidad_maxima, tecnologia_pantalla)
                print("Sala creada.")
            except ValueError:
                print("Datos numéricos inválidos.")
            except EntidadDuplicadaError as error:
                print(f"Error: La sala ya existe. ({error})")
            except ErrorPersistencia as error:
                print(f"Error de persistencia: {error}")
            except Exception as error:
                print(f"Error inesperado: {error}")
        else:
            print("Opción no válida.")

    def mostrar_menu_sesiones(self):
        """Submenú de gestión de sesiones."""
        print("\n--- Sesiones ---")
        print("1. Listar sesiones")
        print("2. Programar sesión")
        opcion_seleccionada = input("Opción: ")
        
        if opcion_seleccionada == "1":
            try:
                for sesion in self._servicio_cine.listar_sesiones():
                    estado_disponibilidad = "LLENA" if sesion.numero_asientos_libres == 0 else f"Libres: {sesion.numero_asientos_libres}"
                    print(f"{sesion} | {estado_disponibilidad}")
            except ErrorPersistencia as error:
                print(f"Error de base de datos: {error}")
            except Exception as error:
                print(f"Error inesperado: {error}")
        elif opcion_seleccionada == "2":
            identificador_sesion = input("ID Sesión (único): ")
            nombre_pelicula = input("Título Película: ")
            try:
                numero_sala = int(input("Número Sala: "))
                fecha_hora = input("Fecha (YYYY-MM-DD HH:MM): ")
                self._servicio_cine.programar_sesion(identificador_sesion, nombre_pelicula, numero_sala, fecha_hora)
                print("Sesión programada.")
            except ValueError:
                print("Número de sala inválido.")
            except EntidadDuplicadaError as error:
                print(f"Error: La sesión ya existe. ({error})")
            except EntidadNoEncontradaError as error:
                print(f"Error: Película o Sala no encontrada. ({error})")
            except ErrorIntegridadDatos as error:
                print(f"Error de integridad: {error}")
            except ErrorPersistencia as error:
                print(f"Error de persistencia: {error}")
            except Exception as error:
                print(f"Error inesperado: {error}")
        else:
            print("Opción no válida.")

    def mostrar_menu_ventas(self):
        """Submenú de venta de entradas."""
        print("\n--- Venta de Entradas ---")
        print("1. Vender entrada")
        print("2. Anular entrada")
        opcion_seleccionada = input("Opción: ")

        if opcion_seleccionada == "1":
            identificador_sesion = input("ID de Sesión: ")
            print("Tarifas: General, Reducida, Estudiante")
            categoria_tarifa = input("Tipo Tarifa: ")
            try:
                entrada = self._servicio_cine.vender_entrada(identificador_sesion, categoria_tarifa)
                print(f"¡Entrada vendida! ID: {entrada.id_entrada} - Precio: {entrada.precio_euros} €")
            except EntidadNoEncontradaError as error:
                print(f"Error: No se encontró la sesión. ({error})")
            except ValueError as error:
                print(f"Error de validación: {error}")
            except ErrorPersistencia as error:
                print(f"Error de persistencia: {error}")
            except Exception as error:
                print(f"Error inesperado: {error}")
        elif opcion_seleccionada == "2":
            identificador_entrada = input("ID de Entrada: ")
            try:
                anulada = self._servicio_cine.anular_entrada(identificador_entrada)
                if anulada:
                    print("Entrada anulada correctamente.")
                else:
                    print("Entrada no encontrada.")
            except ErrorPersistencia as error:
                print(f"Error de persistencia: {error}")
            except Exception as error:
                print(f"Error inesperado en anulación: {error}")
        else:
            print("Opción no válida.")

    def mostrar_menu_estadisticas(self):
        """Visualiza informe de ventas."""
        try:
            estadisticas_ventas = self._servicio_cine.informe_ventas()
            print(f"\nTotal Recaudado: {estadisticas_ventas['total_recaudado']:.2f} €")
            print(f"Entradas Vendidas: {estadisticas_ventas['entradas_vendidas']}")
        except ErrorPersistencia as error:
            print(f"Error de base de datos: {error}")
        except Exception as error:
            print(f"Error inesperado: {error}")
