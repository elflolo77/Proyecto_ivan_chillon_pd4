# Guía de rutas Flask — alejandro (cine multiplex)

## El dominio en una línea

Cine Flolix gestiona películas con tres subtipos (Comercial, Infantil, Clásica), salas de
proyección y sesiones; permite vender y anular entradas con tres tarifas (General, Reducida,
Estudiante) y consultar un informe de recaudación.

---

## Inventario completo del menú

El menú tiene dos niveles: un menú principal con 5 secciones y submenús dentro de cada sección.
En total son **11 operaciones** sobre el dominio.

| # | Sección | Opción del menú | Método del servicio |
|---|---------|-----------------|---------------------|
| 1.1 | Películas | Listar películas | `listar_peliculas()` |
| 1.2 | Películas | Registrar película Comercial | `registrar_pelicula_comercial(titulo, duracion_minutos, clasificacion, genero, distribuidora)` |
| 1.3 | Películas | Registrar película Infantil | `registrar_pelicula_infantil(titulo, duracion_minutos, clasificacion, genero, edad_minima)` |
| 1.4 | Películas | Registrar película Clásica | `registrar_pelicula_clasica(titulo, duracion_minutos, clasificacion, genero, anio_lanzamiento)` |
| 2.1 | Salas | Listar salas | `listar_salas()` |
| 2.2 | Salas | Crear sala | `crear_sala(numero_sala, capacidad_maxima, tecnologia_pantalla)` |
| 3.1 | Sesiones | Listar sesiones | `listar_sesiones()` |
| 3.2 | Sesiones | Programar sesión | `programar_sesion(identificador_sesion, nombre_pelicula, numero_sala, fecha_hora_str)` |
| 4.1 | Ventas | Vender entrada | `vender_entrada(identificador_sesion, categoria_tarifa)` |
| 4.2 | Ventas | Anular entrada | `anular_entrada(identificador_entrada)` |
| 5.1 | Estadísticas | Informe de ventas | `informe_ventas()` |

> **Nota sobre estado de sesión:** la entidad `Sesion` gestiona internamente tres estados
> (`programada`, `completa`, `cancelada`). El estado se almacena en `sesion._estado_sesion`
> (atributo protegido). Las transiciones ocurren automáticamente dentro de `vender_entrada()` y
> `anular_entrada()` de la propia entidad. El servicio no expone un método `cancelar_sesion()`
> por el momento.

---

## Rutas sugeridas (toda la API)

La tabla cubre las 11 operaciones del menú más las rutas de detalle individual. Se agrupan por
recurso. Los parámetros de creación/modificación se pasan como segmentos de URL.

### Raíz

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/` | — | Texto de bienvenida con enlaces a las secciones |

### Películas

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/peliculas` | `listar_peliculas()` | Una línea por película con `obtener_resumen_pelicula()` |
| `/pelicula/<titulo>` | `obtener_pelicula(titulo)` *(añadir)* | Todos los atributos del subtipo; 404 si no existe |
| `/pelicula/nueva/comercial/<titulo>/<int:duracion>/<clasificacion>/<genero>/<distribuidora>` | `registrar_pelicula_comercial(...)` | Confirmación o redirect a `/pelicula/<titulo>`; 409 si ya existe |
| `/pelicula/nueva/infantil/<titulo>/<int:duracion>/<clasificacion>/<genero>/<int:edad_minima>` | `registrar_pelicula_infantil(...)` | Confirmación o redirect a `/pelicula/<titulo>`; 409 si ya existe |
| `/pelicula/nueva/clasica/<titulo>/<int:duracion>/<clasificacion>/<genero>/<int:anio_lanzamiento>` | `registrar_pelicula_clasica(...)` | Confirmación o redirect a `/pelicula/<titulo>`; 409 si ya existe |

### Salas

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/salas` | `listar_salas()` | Una sala por línea con `str(sala)` |
| `/sala/<int:numero>` | `obtener_sala(numero)` *(añadir)* | Número, capacidad y tecnología; 404 si no existe |
| `/sala/nueva/<int:numero>/<int:capacidad>/<tecnologia>` | `crear_sala(numero, capacidad, tecnologia)` | Confirmación o redirect a `/sala/<numero>`; 409 si ya existe |

### Sesiones

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/sesiones` | `listar_sesiones()` | Una sesión por línea con estado y asientos libres |
| `/sesion/<id_sesion>` | `obtener_sesion(id_sesion)` | Todos los datos de la sesión; 404 si no existe |
| `/sesion/nueva/<id_sesion>/<titulo_pelicula>/<int:numero_sala>/<fecha_hora>` | `programar_sesion(...)` | Confirmación o redirect a `/sesion/<id_sesion>`; 400 o 409 según el error |

### Entradas

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/entrada/vender/<id_sesion>/<tarifa>` | `vender_entrada(id_sesion, tarifa)` | ID de entrada, precio y tarifa; 404 si sesión no existe; 409 si completa/cancelada |
| `/entrada/anular/<id_entrada>` | `anular_entrada(id_entrada)` | Confirmación; 404 si la entrada no existe |

### Estadísticas

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/informe` | `informe_ventas()` | Total recaudado y entradas vendidas |

> Los nombres de segmento pueden ajustarse. Lo importante es cubrir las 11 operaciones del menú
> más las rutas de detalle individual.

### Ejemplo: cómo quedaría `app.py` con una ruta completa ya hecha

El siguiente fragmento muestra la estructura mínima de `app.py` con dos rutas implementadas de
ejemplo — la bienvenida y el listado de películas — para que puedas tomar el patrón y aplicarlo
al resto:

```python
from flask import Flask, redirect, url_for
from cine_multiplex.infrastructure.datos_iniciales import inicializar_repositorio
from cine_multiplex.application.servicio_cine import ServicioCine

app = Flask(__name__)

repositorio = inicializar_repositorio()
servicio = ServicioCine(repositorio)


@app.route("/")
def bienvenida():
    return (
        "Bienvenido a Cine Flolix\n"
        "  /peliculas          → listar películas\n"
        "  /salas              → listar salas\n"
        "  /sesiones           → listar sesiones\n"
        "  /informe            → informe de ventas\n"
    )


@app.route("/peliculas")
def listar_peliculas():
    try:
        peliculas = servicio.listar_peliculas()
    except Exception as e:
        return f"Error al obtener películas: {e}", 500

    if not peliculas:
        return "No hay películas registradas."

    lineas = [pelicula.obtener_resumen_pelicula() for pelicula in peliculas]
    return "\n".join(lineas)


if __name__ == "__main__":
    app.run(debug=True)
```

**Lo que hace cada parte:**

- `RepositorioMemoria()` y `ServicioCine(repositorio)` se crean **una sola vez** fuera de las
  vistas, al arrancar la aplicación. Así todas las rutas comparten el mismo estado en memoria.
- Cada función de vista llama al método del servicio correspondiente, gestiona el error con
  `try/except` cuando procede y devuelve texto plano como respuesta.
- Para rutas con `ValueError` devuelve una tupla `(mensaje, código)`: `return "No encontrado", 404`
  o `return "Ya existe", 409`. Después de una acción (alta, programar sesión) redirige con
  `redirect(url_for('nombre_funcion', param=valor))` en lugar de devolver texto directo.

> **Fecha/hora en la URL:** el segmento `<fecha_hora>` en la ruta de programar sesión puede
> requerir codificación especial si contiene espacios o dos puntos. Una opción sencilla para
> `ut4e1` es separar con guión bajo (`2025-06-15_20:30`) y reemplazarlo en la función vista
> antes de llamar al servicio.

---

## Métodos del servicio que hay que añadir

Los siguientes métodos **no existen** en `application/servicio_cine.py` y son necesarios para
exponer todas las operaciones como rutas individuales. Se implementan como delegación pura al
repositorio (sin lógica adicional):

### `obtener_pelicula(titulo: str) -> Pelicula | None`

No existe. Actualmente solo se puede listar todas las películas. Añadir en `servicio_cine.py`:

```python
def obtener_pelicula(self, titulo):
    """Recupera una película por título."""
    return self._repositorio.obtener_pelicula_por_titulo(titulo)
```

Si devuelve `None`, el route devuelve `return "Película no encontrada", 404`.

### `obtener_sala(numero: int) -> Sala | None`

No existe. El repositorio sí tiene `obtener_sala_por_numero()`. Añadir:

```python
def obtener_sala(self, numero_sala):
    """Recupera una sala por número."""
    return self._repositorio.obtener_sala_por_numero(numero_sala)
```

> El método `obtener_sesion(id_sesion)` **ya existe** en el servicio (línea 81 de
> `servicio_cine.py`), por lo que no es necesario añadirlo.

---

## Puntos de atención específicos

### Herencia Pelicula → Comercial / Infantil / Clásica

Cada subtipo implementa `obtener_resumen_pelicula()` con texto diferente y expone atributos
propios:

- `PeliculaComercial` → `distribuidora` (atributo público directo).
- `PeliculaInfantil` → `edad_minima` (atributo público directo).
- `PeliculaClasica` → `anio_lanzamiento` (atributo público directo).

En la ruta de detalle `/pelicula/<titulo>`, usar `isinstance()` para mostrar los atributos
específicos según el subtipo. Ejemplo mínimo en la vista:

```python
from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica

pelicula = servicio.obtener_pelicula(titulo)
if isinstance(pelicula, PeliculaComercial):
    extra = f"Distribuidora: {pelicula.distribuidora}"
elif isinstance(pelicula, PeliculaInfantil):
    extra = f"Edad mínima: {pelicula.edad_minima}"
elif isinstance(pelicula, PeliculaClasica):
    extra = f"Año estreno: {pelicula.anio_lanzamiento}"
```

### Excepciones: solo `ValueError` estándar

El proyecto no tiene un módulo de excepciones propias. El servicio lanza `ValueError` en todos
los casos de error. En las vistas Flask distinguir el significado por contexto:

- Recurso no encontrado (película, sala, sesión, entrada) → `return str(e), 404`.
- Recurso ya existe (película o sesión duplicada) → `return str(e), 409`.
- Datos inválidos (número de sala no entero, etc.) → `return str(e), 400`.

### Estado de sesión (atributo protegido)

`Sesion._estado_sesion` es un atributo protegido con tres valores posibles: `"programada"`,
`"completa"`, `"cancelada"`. Es relevante mostrarlo en `/sesiones` y `/sesion/<id>`. Acceder
mediante `sesion._estado_sesion` es funcional para `ut4e1`; en actividades posteriores se puede
exponer como `@property`.

### Venta de entradas: flujo en dos pasos

Para vender una entrada hace falta saber dos cosas: el identificador de la sesión y la tarifa.
En una web con formulario el usuario los elegiría en pantalla; aquí, como todo va por URL, los
dos datos se pasan directamente en la misma llamada:

```
/entrada/vender/SES01/General
```

Las tarifas válidas son `General`, `Reducida` y `Estudiante` — exactamente con esa capitalización.
Si se pasa una cadena desconocida (p.ej. `general` en minúsculas), el servicio aplica el precio
base sin lanzar error, por lo que la venta se realizará sin avisar del error ortográfico.

### Anulación de entrada: el servicio devuelve `True` o `False`

`anular_entrada()` devuelve `True` si la entrada existía y se eliminó, `False` si no se
encontró. La vista debe tratar el `False` como 404, no como excepción.

### Informe de ventas: dict simple

`informe_ventas()` devuelve `{"total_recaudado": float, "entradas_vendidas": int}`. No lanza
excepciones. Si no hay ventas, devuelve `{"total_recaudado": 0.0, "entradas_vendidas": 0}`.

