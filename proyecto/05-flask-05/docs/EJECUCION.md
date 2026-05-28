# Guía de Ejecución - Fase 05e (Flash y API REST Mínima)

Esta guía describe cómo inicializar, ejecutar y probar la aplicación "Cine Flolix" en su versión web con Flask y su versión tradicional de consola, ambas persistiendo en SQLite.

## Requisitos previos

- Python 3.9 o superior.
- Dependencias instaladas desde `requirements.txt`:

```powershell
pip install -r requirements.txt
```

## Inicialización de la base de datos

Antes de ejecutar la aplicación por primera vez, puedes inicializar manualmente la base de datos `cine.db` con el esquema físico y los datos iniciales de prueba.

Ubica tu terminal en la raíz de esta fase del proyecto (`proyecto/05-flask-05`) y ejecuta:

```powershell
python crear_bd.py
```

Este paso es opcional, ya que tanto la aplicación de consola (`main.py`) como la web con Flask (`app.py`) autocrean la base de datos `cine.db` si detectan que no existe al arrancar.

## Ejecución de la aplicación web Flask

Para arrancar el servidor web de Flask, ubica tu terminal en la raíz de esta fase del proyecto (`proyecto/05-flask-05`) y ejecuta:

```powershell
python -m cine_multiplex.presentation.app
```

La aplicación se sirve localmente en:

```text
http://127.0.0.1:5000/
```

## Rutas web disponibles

- `GET /`: página de inicio.
- `GET /ayuda`: lista dinámicamente todas las rutas registradas, excepto `static`.
- `GET /peliculas`: catálogo de películas.
- `GET, POST /peliculas/registrar_comercial`: formulario y alta de película comercial.
- `GET, POST /peliculas/registrar_infantil`: formulario y alta de película infantil.
- `GET, POST /peliculas/registrar_clasica`: formulario y alta de película clásica.
- `GET /salas`: listado de salas.
- `GET, POST /salas/crear`: formulario y alta de sala.
- `GET /sesiones`: listado de sesiones.
- `GET, POST /sesiones/programar`: formulario y programación de sesión.
- `GET, POST /entradas/vender`: formulario y venta de entrada.
- `GET, POST /entradas/anular`: formulario para localizar la entrada a anular.
- `GET, POST /entradas/anular/<identificador_entrada>`: confirmación y anulación de entrada.
- `GET /informe`: informe de ventas.

Las rutas `GET` solo muestran información, formularios o confirmaciones. Las escrituras se ejecutan por `POST` y, si terminan correctamente, redirigen a una ruta de lectura mostrando un mensaje flash de éxito.

## Mensajes flash

Tras cualquier operación de escritura exitosa (registrar película, crear sala, programar sesión, vender entrada, anular entrada) la aplicación muestra un mensaje de confirmación en la página de destino del redirect. El mensaje desaparece al recargar la página (comportamiento estándar del patrón PRG + flash).

## API REST

La aplicación expone una API REST mínima en JSON bajo `/api/`. Los endpoints consumen exactamente la misma capa de servicio que la interfaz web y devuelven JSON puro sin paginación ni filtros adicionales.

| Método | URL | Descripción |
|--------|-----|-------------|
| GET | `/api/peliculas` | Lista completa de películas |
| GET | `/api/peliculas/<titulo>` | Detalle de película; 404 si no existe |
| GET | `/api/sesiones` | Lista completa de sesiones |
| GET | `/api/sesiones/<id>` | Detalle de sesión; 404 si no existe |

### Cómo invocar la API desde otra terminal

Con la aplicación corriendo en una terminal, abre una segunda terminal y usa `curl`:

```bash
# Listar todas las películas
curl http://127.0.0.1:5000/api/peliculas

# Detalle de una película (sustituye Inception por el título real)
curl "http://127.0.0.1:5000/api/peliculas/Inception"

# Listar todas las sesiones
curl http://127.0.0.1:5000/api/sesiones

# Detalle de una sesión (sustituye s1 por el identificador real)
curl http://127.0.0.1:5000/api/sesiones/s1

# Recurso no encontrado -> JSON {"error": "..."} con HTTP 404
curl -i http://127.0.0.1:5000/api/peliculas/NoExiste
```

## Formularios HTML

Las plantillas de formulario están en `cine_multiplex/presentation/templates/` y todas extienden de `base.html`:

- `form_pelicula_comercial.html`
- `form_pelicula_infantil.html`
- `form_pelicula_clasica.html`
- `form_sala.html`
- `form_sesion.html`
- `form_vender_entrada.html`
- `form_anular_entrada.html`
- `confirmar_anular_entrada.html`

Cuando un `POST` falla, el formulario se vuelve a mostrar con los datos introducidos y un mensaje de error. Cuando un `POST` tiene éxito, se aplica Post/Redirect/Get con `redirect(url_for(...))` y se muestra un mensaje flash en la página de destino.

## Observabilidad y logging

La aplicación registra cada petición HTTP con método y ruta mediante el hook `@app.before_request`.

El fichero se genera automáticamente en la raíz de la fase:

```text
cine_multiplex.log
```

Para desactivar temporalmente el logging, comenta el bloque `logging.basicConfig(...)` y el hook `@app.before_request` en `cine_multiplex/presentation/app.py`.

## Ejecución de la aplicación de consola

Puedes seguir ejecutando la interfaz de consola interactiva. Para ello, ubica tu terminal en `proyecto/05-flask-05` y ejecuta:

```powershell
python main.py
```

## Ejecución de pruebas unitarias

Para ejecutar las pruebas unitarias:

```powershell
python -m unittest discover cine_multiplex/tests -v
```

## Cobertura de código

```powershell
coverage run -m unittest discover cine_multiplex/tests
coverage report
```
