# Guia de Ejecucion - Fase 05b (Flask Observabilidad)

Esta guia describe como inicializar, ejecutar y probar la aplicacion "Cine Flolix" en su version web con Flask y su version tradicional de consola, ambas persistiendo en SQLite.

## Requisitos previos

- Python 3.9 o superior.
- Dependencias instaladas desde `requirements.txt`:

```powershell
pip install -r requirements.txt
```

---

## Inicializacion de la base de datos

Antes de ejecutar la aplicacion por primera vez, puedes inicializar manualmente la base de datos `cine.db` con el esquema fisico y los datos iniciales de prueba.

Ubica tu terminal en la raiz de esta fase del proyecto (`proyecto/05-flask-02`) y ejecuta:

```powershell
python crear_bd.py
```

Este paso es opcional, ya que tanto la aplicacion de consola (`main.py`) como la web con Flask (`app.py`) autocrean la base de datos `cine.db` si detectan que no existe al arrancar.

---

## Ejecucion de la aplicacion web Flask

Para arrancar el servidor web de Flask, ubica tu terminal en la raiz de esta fase del proyecto (`proyecto/05-flask-02`) y ejecuta:

```powershell
python -m cine_multiplex.presentation.app
```

La aplicacion se sirve localmente en:

```text
http://127.0.0.1:5000/
```

## Rutas web disponibles

- Pagina de inicio: `/`
- Ayuda: `/ayuda` lista dinamicamente todas las rutas registradas, excepto `static`.
- Peliculas:
  - Ver catalogo: `/peliculas`
  - Registrar comercial: `/peliculas/registrar_comercial/<titulo>/<duracion>/<clasificacion>/<genero>/<distribuidora>`
  - Registrar infantil: `/peliculas/registrar_infantil/<titulo>/<duracion>/<clasificacion>/<genero>/<edad_minima>`
  - Registrar clasica: `/peliculas/registrar_clasica/<titulo>/<duracion>/<clasificacion>/<genero>/<anio>`
- Salas:
  - Ver salas: `/salas`
  - Crear sala: `/salas/crear/<numero_sala>/<capacidad_maxima>/<tecnologia_pantalla>`
- Sesiones:
  - Ver sesiones: `/sesiones`
  - Programar sesion: `/sesiones/programar/<identificador>/<titulo_pelicula>/<int:numero_sala>/<fecha_hora>`
- Entradas:
  - Vender entrada: `/entradas/vender/<identificador_sesion>/<categoria_tarifa>`
  - Anular entrada: `/entradas/anular/<identificador_entrada>`
- Informes:
  - Informe de ventas: `/informe`

---

## Observabilidad y logging

La aplicacion registra cada peticion HTTP con metodo y ruta mediante el hook `@app.before_request`.

El fichero se genera automaticamente en la raiz de la fase:

```text
cine_multiplex.log
```

Cada linea incluye timestamp, nivel de log y peticion:

```text
2026-05-22 20:33:09,768 [INFO] GET /
2026-05-22 20:33:09,769 [INFO] GET /ayuda
```

Para desactivar temporalmente el logging, comenta el bloque `logging.basicConfig(...)` y el hook `@app.before_request` en `cine_multiplex/presentation/app.py`.

Para reconfigurarlo, cambia los parametros del bloque `logging.basicConfig(...)`, por ejemplo `filename`, `level` o `format`.

---

## Ejecucion de la aplicacion de consola

Puedes seguir ejecutando la interfaz de consola interactiva. Para ello, ubica tu terminal en `proyecto/05-flask-02` y ejecuta:

```powershell
python main.py
```

---

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
