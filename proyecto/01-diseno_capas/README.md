# Cine Flolix

Bienvenido a **Cine Flolix**, un sistema completo de gestión de cines desarrollado en Python. Este proyecto implementa una arquitectura por capas para facilitar el mantenimiento y la escalabilidad, permitiendo administrar películas, salas, sesiones y ventas de entradas.

## Características

-   **Gestión de Películas**: Registro y listado de películas de diferentes tipos (Comerciales, Infantiles, Clásicas), manejando atributos específicos como distribuidora, edad mínima y año de estreno.
-   **Gestión de Salas**: Creación y visualización de salas de cine con diferentes capacidades y tipos de pantalla (2D, 3D, IMAX).
-   **Programación de Sesiones**: Asignación de películas a salas en horarios específicos, controlando la capacidad disponible.
-   **Venta de Entradas**: Sistema de venta de tickets con diferentes tarifas (General, Reducida, Estudiante), validando la disponibilidad de asientos.
-   **Estadísticas y Reportes**: Visualización del total recaudado y número de entradas vendidas.


## Checklist del proyecto

- [x] Crear cuenta en Github/codeberg
- [x] Crear repositorio para alojar/enlazar materiales de clase
- [x] Compartir repositorio con el usuario del profesor (ichigar)
- [x] Instalar y configurar GIT en ordenador de clase y en ordenador de casa.
- [x] Crear claves ssh en ordenador de casa y en ordenador de clase. Añadir claves públicas a las cuentas de github/codeberg
- [x] Clonar repositorio en clase y en casa
- [x] Probar a hacer cambios en clase y en casa y aprender a mantener actualizados los cambios realizados (clase/casa/repositorio)
- [x] Crear subcarpeta `proyecto` en repositorio.
- [x] Incluir en `README.md` descripción del proyecto
- [x] Crear en `proyecto` subcarpeta `01-capas` e incluir en la misma el código para dicha fase de tu proyecto

## Instalación

1. Clona el repositorio o descarga los archivos del proyecto.
2. Abre una terminal y navega hasta el directorio del proyecto:
   ```powershell
   cd d:\Users\Alejandro\Documents\proyecto\Proyecto_ivan_chillon_pd4\proyecto\01-diseno_capas
   ```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando desde el directorio `01-diseno_capas`:

```powershell
python main.py
```

## Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación.
- `cine_multiplex/`:
    - `domain/`: Contiene las entidades y la lógica de negocio (Peliculas, Salas, Sesiones, Entradas).
    - `application/`: Servicios que coordinan las operaciones de la aplicación.
    - `infrastructure/`: Implementaciones de persistencia (memoria) y datos iniciales.
    - `presentation/`: Interfaz de usuario por consola (menú).
