# Diseño Físico de la Base de Datos — Cine Multiplex

Este documento describe el diseño de la base de datos relacional para el sistema Cine Multiplex en SQLite.

## Esquema de Tablas

La base de datos consta de 4 tablas principales: `peliculas`, `salas`, `sesiones` y `entradas`.

### 1. Tabla `peliculas`
Almacena todas las películas disponibles en el cine (tanto comerciales, infantiles como clásicas) utilizando una estrategia de **Tabla Única (Single Table Inheritance)** con una columna discriminadora.

* **Clave Primaria:** `titulo` (TEXT)
* **Columnas:**
  * `titulo` (TEXT): Clave primaria natural (título único de la película).
  * `duracion_minutos` (INTEGER): Duración de la película en minutos. No nulo.
  * `clasificacion` (TEXT): Clasificación de edad (ej. "PG-13", "R"). No nulo.
  * `genero` (TEXT): Género cinematográfico. No nulo.
  * `esta_en_cartelera` (INTEGER): Booleano (1 para activo, 0 para inactivo). No nulo, por defecto 1.
  * `tipo_pelicula` (TEXT): Discriminador de herencia. Valores: `'COMERCIAL'`, `'INFANTIL'`, `'CLASICA'`. No nulo.
  * `distribuidora` (TEXT): Distribuidora de la película. Opcional (solo aplicable a `PeliculaComercial`).
  * `edad_minima` (INTEGER): Edad mínima recomendada. Opcional (solo aplicable a `PeliculaInfantil`).
  * `anio_lanzamiento` (INTEGER): Año de estreno de la película. Opcional (solo aplicable a `PeliculaClasica`).

### 2. Tabla `salas`
Representa las distintas salas de exhibición disponibles en el multiplex.

* **Clave Primaria:** `numero` (INTEGER)
* **Columnas:**
  * `numero` (INTEGER): Identificador único de la sala.
  * `capacidad_maxima` (INTEGER): Aforo total de la sala. No nulo.
  * `tecnologia_pantalla` (TEXT): Tecnología de proyección (ej. `'2D'`, `'3D'`, `'IMAX'`). No nulo.

### 3. Tabla `sesiones`
Representa la programación de una película en una sala específica a una hora determinada.

* **Clave Primaria:** `id_sesion` (TEXT)
* **Columnas:**
  * `id_sesion` (TEXT): Identificador único alfanumérico de la sesión.
  * `pelicula_titulo` (TEXT): Clave foránea que apunta a `peliculas(titulo)`. No nulo.
  * `sala_numero` (INTEGER): Clave foránea que apunta a `salas(numero)`. No nulo.
  * `fecha_hora` (TEXT): Fecha y hora de la sesión programada (formato `'YYYY-MM-DD HH:MM'`). No nulo.
  * `numero_asientos_ocupados` (INTEGER): Número de entradas vendidas para la sesión. No nulo, por defecto 0.
  * `estado_sesion` (TEXT): Estado de disponibilidad (`'programada'`, `'completa'`, `'cancelada'`). No nulo, por defecto `'programada'`.

### 4. Tabla `entradas`
Almacena el registro de cada ticket individual vendido para las distintas sesiones.

* **Clave Primaria:** `id_entrada` (TEXT)
* **Columnas:**
  * `id_entrada` (TEXT): Código único de la entrada (UUID de 8 caracteres).
  * `sesion_id` (TEXT): Clave foránea que apunta a `sesiones(id_sesion)`. No nulo.
  * `precio_euros` (REAL): Importe cobrado por la entrada. No nulo.
  * `categoria_tarifa` (TEXT): Tarifa aplicada (`'General'`, `'Reducida'`, `'Estudiante'`). No nulo.
  * `fecha_venta` (TEXT): Timestamp de la venta en formato ISO 8601. No nulo.

---

## Relaciones e Integridad Referencial

* **Película a Sesión (1:N):** Una película puede proyectarse en múltiples sesiones.
  * Relación: `sesiones.pelicula_titulo` referencias `peliculas.titulo`.
* **Sala a Sesión (1:N):** Una sala puede albergar múltiples sesiones programadas en diferentes horarios.
  * Relación: `sesiones.sala_numero` referencias `salas.numero`.
* **Sesión a Entrada (1:N):** Una sesión puede tener múltiples entradas vendidas.
  * Relación: `entradas.sesion_id` referencias `sesiones.id_sesion`.

Para garantizar la integridad referencial, la base de datos se ejecuta con `PRAGMA foreign_keys = ON`.
