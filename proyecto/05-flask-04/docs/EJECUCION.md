# Guia de Ejecucion - Fase 05d (Formularios HTML)

Esta guia describe como inicializar, ejecutar y probar la aplicacion "Cine Flolix" en su version web con Flask y su version tradicional de consola, ambas persistiendo en SQLite.

## Requisitos previos

- Python 3.9 o superior.
- Dependencias instaladas desde `requirements.txt`:

```powershell
pip install -r requirements.txt
```

## Inicializacion de la base de datos

Antes de ejecutar la aplicacion por primera vez, puedes inicializar manualmente la base de datos `cine.db` con el esquema fisico y los datos iniciales de prueba.

Ubica tu terminal en la raiz de esta fase del proyecto (`proyecto/05-flask-04`) y ejecuta:

```powershell
python crear_bd.py
```

Este paso es opcional, ya que tanto la aplicacion de consola (`main.py`) como la web con Flask (`app.py`) autocrean la base de datos `cine.db` si detectan que no existe al arrancar.

## Ejecucion de la aplicacion web Flask

Para arrancar el servidor web de Flask, ubica tu terminal en la raiz de esta fase del proyecto (`proyecto/05-flask-04`) y ejecuta:

```powershell
python -m cine_multiplex.presentation.app
```

La aplicacion se sirve localmente en:

```text
http://127.0.0.1:5000/
```

## Rutas web disponibles

- `GET /`: pagina de inicio.
- `GET /ayuda`: lista dinamicamente todas las rutas registradas, excepto `static`.
- `GET /peliculas`: catalogo de peliculas.
- `GET, POST /peliculas/registrar_comercial`: formulario y alta de pelicula comercial.
- `GET, POST /peliculas/registrar_infantil`: formulario y alta de pelicula infantil.
- `GET, POST /peliculas/registrar_clasica`: formulario y alta de pelicula clasica.
- `GET /salas`: listado de salas.
- `GET, POST /salas/crear`: formulario y alta de sala.
- `GET /sesiones`: listado de sesiones.
- `GET, POST /sesiones/programar`: formulario y programacion de sesion.
- `GET, POST /entradas/vender`: formulario y venta de entrada.
- `GET, POST /entradas/anular`: formulario para localizar la entrada a anular.
- `GET, POST /entradas/anular/<identificador_entrada>`: confirmacion y anulacion de entrada.
- `GET /informe`: informe de ventas.

Las rutas `GET` solo muestran informacion, formularios o confirmaciones. Las escrituras se ejecutan por `POST` y, si terminan correctamente, redirigen a una ruta de lectura.

## Formularios HTML

Las plantillas de formulario estan en `cine_multiplex/presentation/templates/` y todas extienden de `base.html`:

- `form_pelicula.html`
- `form_sala.html`
- `form_sesion.html`
- `form_vender_entrada.html`
- `form_anular_entrada.html`
- `confirmar_anular_entrada.html`

Cuando un `POST` falla, el formulario se vuelve a mostrar con los datos introducidos y un mensaje de error. Cuando un `POST` tiene exito, se aplica Post/Redirect/Get con `redirect(url_for(...))`.

## Observabilidad y logging

La aplicacion registra cada peticion HTTP con metodo y ruta mediante el hook `@app.before_request`.

El fichero se genera automaticamente en la raiz de la fase:

```text
cine_multiplex.log
```

Para desactivar temporalmente el logging, comenta el bloque `logging.basicConfig(...)` y el hook `@app.before_request` en `cine_multiplex/presentation/app.py`.

## Ejecucion de la aplicacion de consola

Puedes seguir ejecutando la interfaz de consola interactiva. Para ello, ubica tu terminal en `proyecto/05-flask-04` y ejecuta:

```powershell
python main.py
```

## Ejecucion de pruebas unitarias

Para ejecutar las pruebas unitarias:

```powershell
python -m unittest discover cine_multiplex/tests -v
```

## Cobertura de codigo

```powershell
coverage run -m unittest discover cine_multiplex/tests
coverage report
```
