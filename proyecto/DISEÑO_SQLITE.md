# Diseño de tablas SQLite para el Cine Multiplex

Este documento es una guía paso a paso para pasar tu proyecto de persistencia en memoria (diccionarios y listas) a una base de datos SQLite. El objetivo es que al terminar tengas claro qué tablas necesitas, por qué están diseñadas así y cómo crearlas con SQL.

Como referencia, puedes consultar cómo se hizo esta misma transición en el proyecto de la expendedora: `modelo/cepy_pd4/proyecto/04-sqlite/expendedora/`.


## Fase 1: Identificar las entidades y sus atributos

El primer paso es hacer un inventario de las clases de tu dominio que almacenan datos. Cada una de estas clases se convertirá en una **tabla** de la base de datos.

Vamos a repasar tus clases y qué atributos de cada una necesitamos guardar:

**Pelicula** (`domain/pelicula.py`)

Tienes 3 tipos de película (`PeliculaComercial`, `PeliculaInfantil`, `PeliculaClasica`), y todas comparten los mismos atributos base pero añaden uno propio de su subclase:

| Atributo | Tipo en Python | Tipo en SQL | Notas |
|---|---|---|---|
| `id_pelicula` | *(nuevo)* | INTEGER | Sustituye al uso de `titulo` como clave |
| `titulo` | str | TEXT | |
| `duracion_minutos` | int | INTEGER | |
| `clasificacion` | str | TEXT | |
| `genero` | str | TEXT | |
| `esta_en_cartelera` | bool | INTEGER | SQLite no tiene booleanos: se usa 0 (False) y 1 (True) |
| `tipo` | *(nuevo)* | TEXT | Para saber qué subclase crear al leer de la BD |
| `distribuidora` | str | TEXT | Solo para `PeliculaComercial` |
| `edad_minima` | int | INTEGER | Solo para `PeliculaInfantil` |
| `anio_lanzamiento` | int | INTEGER | Solo para `PeliculaClasica` |

Las columnas específicas de cada subclase (`distribuidora`, `edad_minima`, `anio_lanzamiento`) pueden quedar como `NULL` en las filas de otros tipos de película.

**Sala** (`domain/sala.py`)

| Atributo | Tipo en Python | Tipo en SQL |
|---|---|---|
| `numero` | int | INTEGER |
| `capacidad_maxima` | int | INTEGER |
| `tecnologia_pantalla` | str | TEXT |

**Sesion** (`domain/sesion.py`)

| Atributo | Tipo en Python | Tipo en SQL | Notas |
|---|---|---|---|
| `id_sesion` | int | INTEGER | |
| `id_pelicula` | *(nuevo, FK)* | INTEGER | Sustituye al objeto `pelicula` por su ID |
| `numero_sala` | *(nuevo, FK)* | INTEGER | Sustituye al objeto `sala` por su número |
| `fecha_hora` | datetime/str | TEXT | Se guarda como texto en formato "YYYY-MM-DD HH:MM" |
| `numero_asientos_ocupados` | int | INTEGER | |
| `estado_sesion` | str | TEXT | Valores: "programada", "completa", "cancelada" |

Los atributos `pelicula` y `sala` son objetos completos en memoria. En la base de datos no se almacena el objeto entero: se guarda solo su identificador (clave foránea), y al leer la fila se reconstruye el objeto buscando en las otras tablas.

**Entrada** (`domain/entrada.py`)

| Atributo | Tipo en Python | Tipo en SQL | Notas |
|---|---|---|---|
| `id_entrada` | str (uuid) | TEXT | Se mantiene como texto porque ya es un UUID |
| `id_sesion` | *(nuevo, FK)* | INTEGER | Sustituye al objeto `sesion` por su ID |
| `precio_euros` | float | REAL | |
| `categoria_tarifa` | str | TEXT | |
| `fecha_venta` | datetime | TEXT | Formato ISO "YYYY-MM-DD HH:MM:SS" |


## Fase 2: Conceptos básicos de bases de datos

Antes de avanzar, necesitas entender algunos conceptos que vamos a usar constantemente:

**Tabla, fila y columna**

Una tabla es el equivalente al diccionario o lista donde guardas tus datos en memoria, pero con la ventaja de que persiste en disco (no se pierde al cerrar el programa). Cada **fila** de la tabla es un objeto (una película, una sala...) y cada **columna** es un atributo de ese objeto (título, capacidad...).

Por ejemplo, tu diccionario `_coleccion_peliculas` en el repositorio en memoria se convertiría en una tabla `peliculas` donde cada fila es una película.

**Clave primaria (PRIMARY KEY)**

Es la columna que identifica de forma única cada fila. En tu código actual usas el `titulo` como clave del diccionario de películas y el `numero` como clave del de salas. En la base de datos es mejor usar un ID numérico autogenerado: `INTEGER PRIMARY KEY AUTOINCREMENT` genera automáticamente un número único y creciente cada vez que insertas una nueva fila.

Para las salas, el `numero` ya es numérico y único, así que puede funcionar directamente como clave primaria (no hace falta AUTOINCREMENT). Para las entradas, mantenemos el UUID que ya generas con `uuid.uuid4()`.

**Clave foránea (FOREIGN KEY)**

Es una columna en una tabla que "apunta" a la clave primaria de otra tabla. Sirve para crear vínculos entre tablas y para que la base de datos **garantice la integridad** de esos vínculos.

Por ejemplo: si la tabla `sesiones` tiene una columna `id_pelicula` que es clave foránea de `peliculas`, la base de datos no te dejará insertar una sesión con un `id_pelicula` que no exista en la tabla `peliculas`. Esto evita datos huérfanos (sesiones que apuntan a películas inexistentes).

En SQLite, las claves foráneas se activan con `PRAGMA foreign_keys = ON` al inicio de cada conexión.


## Fase 3: Identificar las relaciones entre entidades

Cuando un objeto "pertenece a", "usa" o "contiene" otro, eso se traduce en la base de datos mediante claves foráneas. Vamos a identificar las relaciones de tu proyecto:

### Relaciones uno a muchos (1:N)

Una relación 1:N significa que **un** objeto de un tipo puede estar vinculado con **muchos** objetos de otro tipo, pero cada uno de esos "muchos" solo pertenece a **uno**.

En tu proyecto:

- **Una película puede proyectarse en muchas sesiones**, pero cada sesión proyecta una sola película. En tu código, `Sesion._pelicula` apunta a un objeto `Pelicula`.

- **Una sala puede acoger muchas sesiones**, pero cada sesión ocurre en una sola sala. En tu código, `Sesion._sala` apunta a un objeto `Sala`.

- **Una sesión puede vender muchas entradas**, pero cada entrada corresponde a una sola sesión. En tu código, `Entrada._sesion` apunta a un objeto `Sesion`.

Para representar estas relaciones en la base de datos, se añade la clave foránea en el lado de los "muchos". Por ejemplo, la tabla `sesiones` tendrá una columna `id_pelicula` que apunta a la tabla `peliculas`, y otra columna `numero_sala` que apunta a la tabla `salas`. Así, para obtener todas las sesiones de una película, basta con buscar las filas de `sesiones` donde `id_pelicula` coincida.

### Sobre la herencia de Película

Tus 3 subclases (`PeliculaComercial`, `PeliculaInfantil`, `PeliculaClasica`) comparten los atributos base y añaden cada una un atributo específico. Hay dos formas típicas de modelar esto en SQL:

1. **Una tabla por clase**: una tabla `peliculas` con los atributos comunes y tres tablas más (`peliculas_comerciales`, `peliculas_infantiles`, `peliculas_clasicas`) con los atributos específicos. Más limpio, pero requiere hacer JOIN en cada consulta.

2. **Tabla única con columna discriminadora**: una sola tabla `peliculas` con todos los atributos posibles y una columna `tipo` que indica la subclase. Los atributos específicos quedan como `NULL` para los tipos que no los usan.

Para este proyecto la opción más sencilla y directa es la **tabla única con columna `tipo`**, igual que hace el modelo de la expendedora para distinguir `Item` e `ItemConDescuento`. Cuando leas una fila, usarás el valor de `tipo` para decidir qué clase de Python instanciar.


## Fase 4: Diseño de las tablas

Ahora que tenemos claras las entidades y sus relaciones, vamos a diseñar cada tabla. Para cada una explicamos qué representa y por qué tiene esas columnas.

### Tabla `peliculas`

Corresponde a tu clase `Pelicula` y sus tres subclases. Cada fila es una película registrada en el sistema.

| Columna | Tipo | Restricciones |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT |
| `titulo` | TEXT | NOT NULL, UNIQUE |
| `duracion_minutos` | INTEGER | NOT NULL |
| `clasificacion` | TEXT | NOT NULL |
| `genero` | TEXT | NOT NULL |
| `esta_en_cartelera` | INTEGER | NOT NULL, DEFAULT 1 |
| `tipo` | TEXT | NOT NULL |
| `distribuidora` | TEXT | NULL |
| `edad_minima` | INTEGER | NULL |
| `anio_lanzamiento` | INTEGER | NULL |

Se pone `UNIQUE` en `titulo` porque tu código actual usa el título como clave del diccionario `_coleccion_peliculas` (lo que ya evita duplicados). Así la base de datos también lo garantiza.

El valor de `tipo` será uno de: `"comercial"`, `"infantil"`, `"clasica"`. Las columnas `distribuidora`, `edad_minima` y `anio_lanzamiento` solo tendrán valor en las filas del tipo correspondiente; en las demás serán `NULL`.

### Tabla `salas`

Corresponde directamente a tu clase `Sala`. Cada fila es una sala de proyección.

| Columna | Tipo | Restricciones |
|---|---|---|
| `numero` | INTEGER | PRIMARY KEY |
| `capacidad_maxima` | INTEGER | NOT NULL |
| `tecnologia_pantalla` | TEXT | NOT NULL, DEFAULT '2D' |

Aquí `numero` es la clave primaria directamente, sin AUTOINCREMENT, porque el número de sala lo asignas tú al crearla (no lo genera la base de datos) y ya es único por diseño.

### Tabla `sesiones`

Corresponde a tu clase `Sesion`. Cada fila es la proyección de una película en una sala a una hora concreta.

| Columna | Tipo | Restricciones |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT |
| `id_pelicula` | INTEGER | NOT NULL, FOREIGN KEY → peliculas(id) |
| `numero_sala` | INTEGER | NOT NULL, FOREIGN KEY → salas(numero) |
| `fecha_hora` | TEXT | NOT NULL |
| `numero_asientos_ocupados` | INTEGER | NOT NULL, DEFAULT 0 |
| `estado_sesion` | TEXT | NOT NULL, DEFAULT 'programada' |

Las dos claves foráneas crean los vínculos: `id_pelicula` dice qué película se proyecta, y `numero_sala` dice en qué sala ocurre. La fecha/hora se guarda como texto en formato ISO `"YYYY-MM-DD HH:MM"` para que se pueda ordenar alfabéticamente y siga siendo cronológico.

El `estado_sesion` es un texto que solo debería tomar los valores `"programada"`, `"completa"` o `"cancelada"`. SQLite no tiene un tipo enum, así que la validación queda en tu código (en el método `vender_entrada()`).

### Tabla `entradas`

Corresponde a tu clase `Entrada`. Cada fila es una entrada vendida.

| Columna | Tipo | Restricciones |
|---|---|---|
| `id` | TEXT | PRIMARY KEY |
| `id_sesion` | INTEGER | NOT NULL, FOREIGN KEY → sesiones(id) |
| `precio_euros` | REAL | NOT NULL |
| `categoria_tarifa` | TEXT | NOT NULL |
| `fecha_venta` | TEXT | NOT NULL |

Aquí la clave primaria es `TEXT` porque tu código ya genera el identificador con `uuid.uuid4()`, y es más sencillo mantener ese patrón que cambiarlo ahora a un entero autogenerado. `precio_euros` se guarda como `REAL` (número con decimales). `fecha_venta` se guarda como texto en formato ISO `"YYYY-MM-DD HH:MM:SS"`.

El `id_sesion` es la clave foránea que vincula la entrada con su sesión. Si la sesión se borra, la base de datos te protegerá de borrar entradas huérfanas (si activas las FK).

### Diagrama relacional

```
 peliculas (id) ─────┐
                     │
                     ▼
                  sesiones (id) ──────► entradas
                     ▲
                     │
 salas (numero) ─────┘
```

- Una película tiene muchas sesiones (1:N).
- Una sala tiene muchas sesiones (1:N).
- Una sesión tiene muchas entradas vendidas (1:N).


## Fase 5: Sentencias SQL para crear las tablas

Aquí tienes las sentencias SQL completas. El orden importa: las tablas que son referenciadas por otras (con FK) deben crearse primero.

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS peliculas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL UNIQUE,
    duracion_minutos INTEGER NOT NULL,
    clasificacion TEXT NOT NULL,
    genero TEXT NOT NULL,
    esta_en_cartelera INTEGER NOT NULL DEFAULT 1,
    tipo TEXT NOT NULL,
    distribuidora TEXT,
    edad_minima INTEGER,
    anio_lanzamiento INTEGER
);

CREATE TABLE IF NOT EXISTS salas (
    numero INTEGER PRIMARY KEY,
    capacidad_maxima INTEGER NOT NULL,
    tecnologia_pantalla TEXT NOT NULL DEFAULT '2D'
);

CREATE TABLE IF NOT EXISTS sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pelicula INTEGER NOT NULL,
    numero_sala INTEGER NOT NULL,
    fecha_hora TEXT NOT NULL,
    numero_asientos_ocupados INTEGER NOT NULL DEFAULT 0,
    estado_sesion TEXT NOT NULL DEFAULT 'programada',
    FOREIGN KEY (id_pelicula) REFERENCES peliculas(id),
    FOREIGN KEY (numero_sala) REFERENCES salas(numero)
);

CREATE TABLE IF NOT EXISTS entradas (
    id TEXT PRIMARY KEY,
    id_sesion INTEGER NOT NULL,
    precio_euros REAL NOT NULL,
    categoria_tarifa TEXT NOT NULL,
    fecha_venta TEXT NOT NULL,
    FOREIGN KEY (id_sesion) REFERENCES sesiones(id)
);
```


## Fase 6: Script de ejemplo para crear la base de datos

Este script crea la base de datos e inserta los datos iniciales que actualmente cargas en `infrastructure/datos_iniciales.py`. Sigue el mismo patrón que `modelo/cepy_pd4/proyecto/04-sqlite/expendedora/crear_bd.py`.

```python
"""Script para crear la base de datos del cine multiplex con datos iniciales."""

import sqlite3
from pathlib import Path

# Eliminar la base de datos si ya existe (para recrearla limpia)
ruta_bd = Path("cine.db")
if ruta_bd.exists():
    ruta_bd.unlink()

conn = sqlite3.connect("cine.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# Crear tablas (copiar aquí las sentencias CREATE TABLE de la Fase 5)
# ...

# Insertar datos iniciales

# Películas
cursor.execute("""
    INSERT INTO peliculas (titulo, duracion_minutos, clasificacion, genero,
                           esta_en_cartelera, tipo, distribuidora)
    VALUES ('Dune: Parte Dos', 166, 'PG-13', 'Ciencia Ficción',
            1, 'comercial', 'Warner Bros')
""")

cursor.execute("""
    INSERT INTO peliculas (titulo, duracion_minutos, clasificacion, genero,
                           esta_en_cartelera, tipo, edad_minima)
    VALUES ('Kung Fu Panda 4', 94, 'PG', 'Animación',
            1, 'infantil', 5)
""")

cursor.execute("""
    INSERT INTO peliculas (titulo, duracion_minutos, clasificacion, genero,
                           esta_en_cartelera, tipo, anio_lanzamiento)
    VALUES ('El Padrino', 175, 'R', 'Crimen',
            1, 'clasica', 1972)
""")

# Salas
cursor.execute("INSERT INTO salas (numero, capacidad_maxima, tecnologia_pantalla) VALUES (1, 100, '2D')")
cursor.execute("INSERT INTO salas (numero, capacidad_maxima, tecnologia_pantalla) VALUES (2, 50, '3D')")
cursor.execute("INSERT INTO salas (numero, capacidad_maxima, tecnologia_pantalla) VALUES (3, 30, 'IMAX')")

conn.commit()

# Mostrar contenido
print("Base de datos creada con datos iniciales.\n")

print("--- Películas ---")
cursor.execute("SELECT id, titulo, tipo, duracion_minutos FROM peliculas")
for fila in cursor.fetchall():
    print(f"  [{fila[0]}] {fila[1]} ({fila[3]} min) - tipo: {fila[2]}")

print("\n--- Salas ---")
cursor.execute("SELECT numero, capacidad_maxima, tecnologia_pantalla FROM salas")
for fila in cursor.fetchall():
    print(f"  Sala {fila[0]}: {fila[1]} pax, {fila[2]}")

conn.close()
print("\nBase de datos guardada en cine.db")
```


## Resumen: de memoria a SQLite

| En memoria (ahora) | En SQLite (nuevo) |
|---|---|
| `_coleccion_peliculas = {}` (clave: título) | Tabla `peliculas` con `titulo UNIQUE` |
| `_coleccion_salas = {}` (clave: número) | Tabla `salas` con `numero` como PK |
| `_coleccion_sesiones = {}` (clave: id_sesion) | Tabla `sesiones` + FK a peliculas y salas |
| `_coleccion_entradas = []` | Tabla `entradas` + FK a sesiones |
| `Sesion._pelicula` (objeto) | Columna `id_pelicula` (FK) |
| `Sesion._sala` (objeto) | Columna `numero_sala` (FK) |
| `Entrada._sesion` (objeto) | Columna `id_sesion` (FK) |
| Herencia `PeliculaComercial/Infantil/Clasica` | Columna `tipo` + columnas específicas nullables |
| `uuid.uuid4()` para Entrada | `id TEXT PRIMARY KEY` (se mantiene) |
| ID manual para Sesion | `INTEGER PRIMARY KEY AUTOINCREMENT` |
