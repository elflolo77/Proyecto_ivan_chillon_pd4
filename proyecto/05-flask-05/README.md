
# Fase 02: Documentación y Refactorización del Diseño en Capas

## Descripción General
Este directorio (`02-documentando`) contiene la evolución del proyecto base originado en la fase 01. En esta fase se ha garantizado la correcta estructuración del código orientándose en Patrones de Diseño, aplicando convenciones de código (PEP-8) y ampliando exhaustivamente la documentación teórica.

## Documentación del Proyecto
Toda la documentación arquitectónica, funcional y de reglas de negocio reside encapsulada en la carpeta `docs/`.

Por favor, comienza tu lectura en el índice global:
👉 **[Acceder a docs/README.md](docs/README.md)**

## Instrucciones Rápidas

Para probar la lógica implementada asilada de Base de Datos en memoria:

1. Abre tu terminal y cerciórate de que te encuentras sobre la raíz de la fase actual:
```powershell
cd proyecto/02-documentando
```

2. Ejecuta el programa:
```powershell
python main.py
```

<details open>
  <summary>Fase 02 - documentando</summary>

- [x] Copiado en subcarpeta `02-documentando` el contenido actual de la carpeta `01-diseno_capas` o se crea una nueva rama para la nueva etapa (antes crear la rama 01-diseno-capas).
- [x] Renombrar todos los identificadores de modulos, clases, métodos y variables que no cumplan con los [criterios de los apuntes](https://ichigar.codeberg.page/pd4/ut1/recursos/poo_ut1_6_documentacion/#eligiendo-nombres)
- [x] Añadir docstring a los módulos, clases y métodos públicos del proyecto siguiendo los [criterios de los apuntes](https://ichigar.codeberg.page/pd4/ut1/recursos/poo_ut1_6_documentacion/#eligiendo-nombres).
- [x] Comentar las reglas de negocio de las clases del dominio.
- [x] Comentar los bloques de código que no expresen claramente para qué se usan.
- [x] Eliminar comentarios evidentes.
#### Usando como referencia los [documentos del proyecto model](https://codeberg.org/ichigar/cepy_pd4/src/branch/main/proyecto/02-documentando/expendedora) añadir los siguientes ficheros:
- [x] README.md
- [x] CHANGELOG.md
- [x] `docs/README.md`
- [x] `docs/DESCRIPCION_Y_ALCANCE.md`
- [x] `docs/EJECUCION.md`
- [x] `docs/ARQUITECTURA_POR_CAPAS.md`
- [x] `docs/CASOS_DE_USO.md`
- [x] `docs/REGLAS_DE_NEGOCIO.md`
- [x] `docs/MODELO_DE_DOMINIO.md`
- [x] `docs/CONTRATO_REPOSITORIO.md`
- [x] `docs/DATOS_INICIALES.md`
- [x] `docs/TESTS_Y_PASOS.md`
- [x] `docs/TROUBLESHOOTING.md`
</details>

# FASE III. TESTING
## Instrucciones

Para probar la lógica y las pruebas unitarias en esta fase del proyecto:

1. Abre tu terminal en la raíz de la fase actual:
```powershell
cd proyecto/03-testing
```

2. Ejecutar la aplicación:
```powershell
python main.py
```

3. Ejecutar las pruebas unitarias:
```powershell
python -m unittest discover cine_multiplex/tests
```

4. Ejecutar reporte de cobertura:
```powershell
coverage run -m unittest discover cine_multiplex/tests; coverage report
```

### Ejecución Fase 05 (Flask Web App)

1. Abre tu terminal en la raíz de la fase actual:
```powershell
cd proyecto/05-flask-01
```

2. Instala dependencias necesarias:
```powershell
pip install -r requirements.txt
```

3. Ejecuta la aplicación Flask:
```powershell
python -m cine_multiplex.presentation.app
```
La aplicación web quedará expuesta en `http://127.0.0.1:5000/`.

<details>
  <summary>Fase 03 - testing</summary>

- [x] Copiar en `03-testing` el estado base de `02-documentando` (o crear rama especifica para la fase 03).
- [x] Reorganizar las pruebas en la subcarpeta `tests/`.
- [x] Crear y mantener test para, al menos, dos clases del dominio.
- [x] Verificar que todos los test pasan con `python -m unittest`.
- [x] Anadir `coverage` como dependencia de fase (en `requirements.txt`).
- [x] Ejecutar cobertura con `coverage run -m unittest` y revisar reporte con `coverage report`.
- [x] Documentar la ejecucion de tests y coverage en `docs/TESTS_Y_PASOS.md`.
- [x] Actualizar `docs/EJECUCION.md` con pasos completos desde clonado hasta ejecucion.
- [x] Revisar y corregir documentos desactualizados de `docs/` para reflejar la fase 03.
- [x] Registrar los cambios de fase en `CHANGELOG.md` (version `0.3.0`).
- [x] Actualizar `README.md` para reflejar estructura y comandos actuales.

</details>

<details open>
  <summary>Fase 04 - persistencia con SQLite</summary>

### Diseño e implementación del esquema de base de datos

- [x] Copiar en `04-sqlite` el estado base de `03-testing` (o crear rama específica para la fase 04).
- [x] Diseñar las tablas SQL mapeando cada entidad de dominio a tablas con sus columnas, tipos y restricciones (`PRIMARY KEY`, `NOT NULL`, `FOREIGN KEY`).
- [x] Usar nombres de columnas en snake_case.

### Script de inicialización de base de datos

- [x] Crear script que cree el esquema de la BD e inserte datos iniciales de prueba
  - Debe poder ejecutarse varias veces sin error
  - Crea todas las tablas respetando dependencias de claves foráneas
  - Inserta datos iniciales para probar la aplicación

### Excepciones de dominio para persistencia

- [x] (*opcional*) Crear fichero de excepciones (`infrastructure/errores.py`) con las excepciones que el repositorio SQLite lanza al usuario
  - Clase base para todas las excepciones de persistencia
  - Excepciones por cada tipo de error que puede ocurrir (duplicado, no encontrado, etc.)

### Implementación del repositorio SQLite

- [x] Crear clase(s) de repositorio que implementen persistencia en SQLite (realizando las mismas operaciones que el repositorio en memoria: guardar, obtener, actualizar, eliminar, etc.)
- [x] Usar consultas SQL parametrizadas (parámetros `?`) para prevenir inyección SQL
- [x] Capturar excepciones SQLite (`sqlite3.IntegrityError`, `sqlite3.OperationalError`, etc.) y transformarlas en excepciones de dominio
- [x] Activar `PRAGMA foreign_keys = ON` al conectar para garantizar integridad referencial
- [x] **El flujo principal de la aplicación (menú) debe usar SOLO el repositorio SQLite para persistencia** (no usar en memoria)

### Repositorio en memoria (referencia, no en uso)

- [x] (**opcional**) Mantener el código del repositorio en memoria como referencia de implementación y contrato
- [x] (**opcional**) Modificar `infrastructure/repositorio_memoria.py` para lanzar las **mismas excepciones de dominio** que el repositorio SQLite (útil para tests sin persistencia)

### Integración con SQLite en la capa de presentación

- [x] Modificar la capa de presentación para cargar datos iniciales desde la BD en lugar de desde memoria (al iniciar la aplicación)
- [x] Capturar excepciones de dominio, no excepciones de `sqlite3`
- [x] (*opcional*) Mostrar mensajes amigables al usuario cuando ocurran errores de persistencia
- [x] No hacer imports de `sqlite3` directamente en la presentación.

### Actualización de los tests

- [x] *(opcional)* Actualizar tests existentes para esperar excepciones de dominio en lugar de excepciones genéricas de Python
- [x] Verificar que `python -m unittest` pasa con todos los tests en verde
- [x] *(opcional)* Crear tests específicos para el repositorio SQLite

### Documentación

- [x] Actualizar `CHANGELOG.md` (versión `0.4.0`) con los cambios principales
- [x] Actualizar `README.md` con instrucciones de cómo ejecutar el script de inicialización
- [x] Documentar el diseño de la BD en `docs/DISEÑO_BD.md`
- [x] (*opcional*) Documentar el contrato de excepciones en `docs/CONTRATO_EXCEPCIONES.md`

### Verificación final

- [x] La aplicación funciona igual desde el punto de vista del usuario (mismo menú, mismas operaciones)
- [x] Los datos persisten entre ejecuciones (cierra y reabre la app, verifica que los datos están)
- [x] Los tests pasan todos sin cambios de lógica de dominio

</details>

# FASE 05: Flask Web Application

## Instrucciones

1. Abre tu terminal en la raíz de la fase actual:
```powershell
cd proyecto/05-flask-01
```

2. Instala dependencias necesarias:
```powershell
pip install -r requirements.txt
```

3. Inicializar la base de datos (opcional — se autocrea al arrancar si no existe):
```powershell
python crear_bd.py
```

4. Ejecuta la aplicación Flask:
```powershell
python -m cine_multiplex.presentation.app
```
La aplicación web quedará expuesta en `http://127.0.0.1:5000/`.

5. Ejecutar el menú por consola (retrocompatibilidad):
```powershell
python main.py
```

6. Ejecutar pruebas unitarias:
```powershell
python -m unittest discover cine_multiplex/tests -v
```

<details open>
  <summary>Fase 05 - Flask Web App</summary>

- [x] Carpeta `05-flask-01/` creada con el contenido de `04-sqlite/` como base.
- [x] `requirements.txt` incluye `flask`.
- [x] `presentation/app.py` ejecutable con `python -m {paquete}.presentation.app`.
- [x] Route `/` con mensaje de bienvenida y enlaces a las rutas principales.
- [x] Todas las operaciones del menú de consola expuestas como routes, incluyendo:
  - Consultas (listados, detalles por identificador, búsquedas).
  - Acciones que modifican datos (altas, bajas, ediciones, reposiciones, reservas, cambios de estado…).
  - Operaciones transaccionales o con estado intermedio.
- [x] Los routes usan `<codigo>`, `<int:id>`, `<float:precio>…` para los parámetros tipados.
- [x] Los routes que modifican datos redirigen con `redirect(url_for(...))` tras la acción (patrón "actúa → redirige").
- [x] Todas las excepciones de dominio capturadas en `menu.py` están también capturadas en los routes correspondientes con el código HTTP apropiado (404 para "no encontrado", 409 para conflicto de estado como duplicado, 400 para datos inválidos).
- [x] `presentation/menu.py` sigue funcionando sin cambios.
- [x] CHANGELOG.md con entrada nueva.
- [x] README.md y `docs/EJECUCION.md` actualizados con el comando de arranque y las rutas expuestas.

</details>
  <summary>Fase 05-2 - Observabilidad: manejadores de error, introspección y logging</summary>

# FASE 05b: UT4E2 — Observabilidad: manejadores de error, introspección y logging

Esta es la segunda actividad de la serie en la que se amplía el `app.py` del proyecto personal con Flask. En la entrega anterior (`ut4e1`) se crearon rutas para todas las operaciones del menú de consola; en esta entrega se añade una capa de observabilidad global que no depende del dominio: manejadores de error 404 y 500, una ruta `/ayuda` que se autoactualiza listando todas las rutas registradas, y registro de cada petición en un fichero `.log`. Se aplican los patrones trabajados en el lab a3 de la expendedora.

En esta entrega los manejadores de error y la página `/ayuda` devuelven HTML construido a mano: cuando se introduzcan las plantillas, se refactorizará para generar desde ahí el HTML.

## Instrucciones

1. Abre tu terminal en la raíz de la fase actual:
```powershell
cd proyecto/05-flask-02
```

2. Instala dependencias necesarias:
```powershell
pip install -r requirements.txt
```

3. Inicializar la base de datos (opcional — se autocrea al arrancar si no existe):
```powershell
python crear_bd.py
```

4. Ejecuta la aplicación Flask:
```powershell
python -m cine_multiplex.presentation.app
```
La aplicación web quedará expuesta en `http://127.0.0.1:5000/`.

5. Consultar rutas disponibles en: `http://127.0.0.1:5000/ayuda`

6. El fichero de log se genera automáticamente en `cine_multiplex.log` al hacer peticiones.
   Para desactivar temporalmente el logging, comenta el bloque `logging.basicConfig(...)`
   y el hook `@app.before_request` en `cine_multiplex/presentation/app.py`.
   Para reconfigurarlo, cambia `filename`, `level` o `format` en `logging.basicConfig(...)`.

7. Ejecutar el menú por consola (retrocompatibilidad):
```powershell
python main.py
```

8. Ejecutar pruebas unitarias:
```powershell
python -m unittest discover cine_multiplex/tests -v
```

<details open>
  <summary>Fase 05b — UT4E2: Observabilidad Flask</summary>

- [x] Carpeta `05-flask-02/` creada con el contenido de `05-flask-01/` como base.
- [x] `@app.errorhandler(404)` registrado y devuelve HTML personalizado al visitar una URL inexistente.
- [x] `@app.errorhandler(500)` registrado y devuelve HTML personalizado. Probado provocando una excepción no controlada (puede crearse una ruta temporal `/error` para la prueba y eliminarla después).
- [x] Ruta `/ayuda` que itera `app.url_map.iter_rules()`, filtra `static` y muestra todas las rutas registradas. Al añadir o quitar rutas, `/ayuda` refleja el cambio sin tocar su código.
- [x] `logging.basicConfig(...)` configurado al inicio de `app.py` con nombre de fichero `cine_multiplex.log`.
- [x] Hook `@app.before_request` registra cada petición con método y ruta.
- [x] El fichero `.log` aparece en disco al hacer peticiones, con timestamp y una línea por petición.
- [x] `.gitignore` incluye `*.log` y el fichero de log no se versiona.
- [x] Coexistencia menú↔web verificada: un alta hecha desde la web aparece en el menú y viceversa. Verificación anotada en la documentación.
- [x] `domain/` e `infrastructure/` sin cambios; `application/` solo con métodos de delegación pura si los hay.
- [x] `presentation/menu.py` sigue funcionando sin cambios.
- [x] `CHANGELOG.md` con entrada nueva siguiendo SemVer (incremento menor: añade observabilidad sin romper la API existente).
- [x] `README.md` y `docs/EJECUCION.md` actualizados (mencionan `/ayuda`, el fichero `.log` y cómo desactivar o reconfigurar el logging si hace falta).




# UT4e3 - Plantillas Jinja2

Esta es la tercera actividad de la serie en la que se amplia el `app.py` del proyecto personal con Flask. En las entregas anteriores (`ut4e1` y `ut4e2`) se expusieron como rutas todas las operaciones del menu de consola y se anadio la capa de observabilidad (manejadores de error, `/ayuda` y logging). En esta entrega se introducen plantillas Jinja2 para sacar el HTML inline de `app.py` y unificar la presentacion. Las plantillas residen en `cine_multiplex/presentation/templates/`. Se usa una plantilla base `base.html` con cabecera y navegacion comunes, y plantillas hijas que extienden de ella para cada vista.

En esta entrega solo se crean plantillas para las rutas que devuelven informacion (listados, detalles, busqueda, ayuda, errores). Las rutas que requieren que el usuario introduzca datos manualmente quedan tal como estan; esas se veran al trabajar los formularios HTML, donde se integraran de forma natural en plantillas con sus propios campos de entrada. Lo que se sustituye ahora es el HTML construido a mano en los routes de lectura y en los manejadores de error.

## Pasos

1. Crear en la carpeta de inicio del proyecto (sincronizada en Codeberg/GitHub) una carpeta (o una rama) de nombre `05-flask-03`, copiando el contenido de `05-flask-02` (resultado de la entrega `ut4e2`).

2. Estudiar como referencia el lab a4 de la expendedora y los apuntes de la Fase 4. En esta entrega no hay guia personal: los patrones son universales y se aplican igual al dominio que sea.

3. Aplicar al proyecto personal los aspectos trabajados en el lab a4, adaptandolos al dominio. Se trata de trasladar lo aprendido sin reinventar nada; el lab y los apuntes ya explican el como. Aspectos a cubrir:

- Plantilla base `base.html` con la estructura comun y bloques.
- Plantillas hijas para las vistas de lectura, extendiendo de `base.html`.
- Sintaxis Jinja2: inyeccion de valores, iteracion, condicionales y filtros (incluido el formato de numeros con separador decimal local si tu dominio lo necesita).
- Conversion tupla -> diccionario en el route cuando el servicio devuelva tuplas.
- `url_for` en plantillas para los enlaces.
- Plantilla comun `error.html` reutilizada por los manejadores `@app.errorhandler(404)` y `@app.errorhandler(500)` de `ut4e2`.
- Verificar que la cabecera con navegacion aparece en todas las paginas, incluidas las de error 404 y 500. Si una pagina la pierde, suele ser porque la plantilla hija no extiende de `base.html` o porque algun route sigue devolviendo HTML inline en lugar de `render_template`.

4. Hacer commits periodicos y sincronizar en la nube (`push`) el repositorio para que el profesor pueda revisar esta fase del proyecto.

5. Actualizar la documentacion con los cambios aplicados en esta fase. Al menos los siguientes ficheros se ven afectados:

```text
CHANGELOG.md
README.md
docs/EJECUCION.md  <- nota sobre la nueva carpeta de plantillas
```

## Checklist para esta fase

- [x] Carpeta `05-flask-03/` creada con el contenido de `05-flask-02/` como base.
- [x] Aspectos del lab a4 aplicados al proyecto personal: plantilla base, plantillas hijas extendiendo de `base.html`, sintaxis Jinja2 (filtros incluidos), conversion tupla -> dict cuando aplique, `url_for` en plantillas, plantilla comun para errores 404/500.
- [x] Se han generado plantillas para todas las rutas que muestran informacion del proyecto.
- [x] Los routes de lectura usan `render_template` en lugar de devolver texto o HTML inline.
- [x] La cabecera con navegacion es visible en todas las paginas, incluidas las de error 404 y 500.
- [x] `domain/` e `infrastructure/` sin cambios. `application/` solo anade metodos de delegacion pura si hace falta.
- [x] `presentation/menu.py` sigue funcionando sin cambios.
- [x] `CHANGELOG.md` con entrada nueva siguiendo SemVer (incremento menor: anade plantillas sin romper la API existente).
- [x] `README.md` y `docs/EJECUCION.md` actualizados (mencionan la carpeta `presentation/templates/` y el patron de herencia con `base.html`).


</details>

# UT4e4 — Formularios HTML y método POST
Esta es la cuarta actividad de la serie en la que se amplía el app.py del proyecto personal con Flask. En las entregas anteriores (ut4e1, ut4e2, ut4e3) se expusieron como rutas todas las operaciones del menú de consola, se añadió la capa de observabilidad (manejadores de error, /ayuda y logging) y se introdujeron las plantillas Jinja2 para sacar el HTML inline de los routes de lectura. En esta entrega se convierten las operaciones de escritura del proyecto en formularios HTML con método POST, validación con re-render y patrón Post/Redirect/Get. Aplica los patrones trabajados en el lab a5 de la expendedora.

En ut4e1 se expusieron como rutas todas las operaciones del menú, incluidas las que modifican estado (altas, bajas, ediciones, cambios…), con los datos viajando en la propia URL (/operacion/<param1>/<param2>/...). Eso funciona como ejercicio pero tiene varios problemas: la URL queda visible en el historial, F5 repite la acción sin avisar, una vista previa de chat o una precarga del navegador puede dispararla, y el tamaño está limitado. La solución estándar es mover esos datos al cuerpo de una petición POST a través de un formulario HTML. Esta entrega aplica ese cambio a todas las operaciones de escritura del proyecto personal.

Pasos
Crear en la carpeta de inicio del proyecto (sincronizada en Codeberg/GitHub) una carpeta (o una rama) de nombre 05-flask-04, copiando el contenido de 05-flask-03 (resultado de la entrega ut4e3).

Estudiar como referencia el lab a5 de la expendedora y los apuntes de la Fase 5. En esta entrega no hay guía personal: los patrones son universales y se aplican igual al dominio que sea.

Para cada operación de escritura del proyecto (alta, modificación, baja, y cualquier otra que cambie estado en el dominio), aplicar los siguientes elementos:

Una plantilla HTML del formulario en presentation/templates/, que extienda de base.html y muestre los campos necesarios (<input>, <select>, <textarea>...). Cada campo con su name, el <form> con method="post" y action="{{ url_for(...) }}".
Un route con methods=['GET', 'POST'] sobre la misma URL: el GET renderiza el formulario vacío (o con los datos actuales si es una edición); el POST procesa los datos, llama al servicio del dominio y actúa según el resultado.
Manejo de errores con re-render: si el dominio lanza una excepción (formato incorrecto, regla de negocio, conflicto, recurso no encontrado), capturarla y volver a renderizar el formulario con los datos tecleados conservados y un mensaje de error visible. Devolver el código HTTP adecuado (400 para validación de tipo/negocio, 404 para no encontrado, 409 para conflicto).
Tras éxito, patrón Post/Redirect/Get: devolver redirect(url_for(...)) a una ruta de lectura coherente (ficha del recurso, listado, etc.). Nunca devolver HTML directamente tras un POST con éxito.
Para las eliminaciones, patrón de confirmación: el GET muestra una página "¿seguro que quieres eliminar X?" con los datos del recurso para que el usuario sepa qué va a borrar; el POST sobre la misma URL ejecuta la baja y redirige.
Para las acciones de escritura sin pantalla previa (un botón que se pulsa desde otra pantalla, sin formulario propio), un route que solo acepte methods=['POST']. Acceder a esa URL con GET responderá 405 Method Not Allowed automáticamente — es justo lo que queremos.
Reestructurar las rutas de escritura siguiendo el patrón del lab a5. Lo importante es que ninguna acción de escritura se dispare por GET; cómo quede el path de cada URL es secundario. En el lab a5 vimos varias formas de hacerlo (formulario único en /insertar, /eliminar/<codigo> con confirmación GET + acción POST, /cancelar solo POST sin pantalla previa…). Aplica el patrón que mejor encaje a cada operación de tu dominio mirando esos casos como referencia.

Verificar que ninguna acción de escritura del proyecto queda accesible por GET. Recorre todas las rutas de la app y comprueba que cualquier URL que modifique estado requiere POST. Si quedara un GET con efectos secundarios, F5 lo repetiría sin avisar.

Hacer commits periódicos y sincronizar en la nube (push) el repositorio para que el profesor pueda revisar esta fase del proyecto.

Actualizar la documentación con los cambios aplicados en esta fase. Al menos los siguientes ficheros se ven afectados:

├── CHANGELOG.md
├── README.md
└── docs
    └── EJECUCION.md                ← lista actualizada de rutas con sus verbos HTTP
## Ejecucion Fase 05d

1. Abre tu terminal en la raiz de esta fase:

```powershell
cd proyecto/05-flask-04
```

2. Instala dependencias:

```powershell
pip install -r requirements.txt
```

3. Ejecuta la aplicacion Flask:

```powershell
python -m cine_multiplex.presentation.app
```

La aplicacion queda disponible en:

```text
http://127.0.0.1:5000/
```

## Rutas y verbos HTTP

- `GET /`: inicio.
- `GET /ayuda`: rutas registradas.
- `GET /peliculas`: listado de peliculas.
- `GET, POST /peliculas/registrar_comercial`: formulario y alta de pelicula comercial.
- `GET, POST /peliculas/registrar_infantil`: formulario y alta de pelicula infantil.
- `GET, POST /peliculas/registrar_clasica`: formulario y alta de pelicula clasica.
- `GET /salas`: listado de salas.
- `GET, POST /salas/crear`: formulario y alta de sala.
- `GET /sesiones`: listado de sesiones.
- `GET, POST /sesiones/programar`: formulario y programacion de sesion.
- `GET, POST /entradas/vender`: formulario y venta de entrada.
- `GET, POST /entradas/anular`: formulario para buscar la entrada a anular.
- `GET, POST /entradas/anular/<identificador_entrada>`: confirmacion y anulacion de entrada.
- `GET /informe`: informe de ventas.

## Checklist para esta fase

- [x] Carpeta `05-flask-04/` creada con el contenido de `05-flask-03/` como base.
- [x] Cada operacion de escritura del proyecto tiene su propia plantilla HTML de formulario en `presentation/templates/`, extendiendo de `base.html`.
- [x] Las routes correspondientes aceptan `methods=['GET', 'POST']` (o solo `['POST']` si la accion no necesita pantalla previa) y separan claramente las dos ramas con `if request.method == 'POST'`.
- [x] Tras un POST con exito, patron Post/Redirect/Get aplicado: `return redirect(url_for(...))` a una ruta de lectura. Ninguna respuesta de exito devuelve HTML directamente.
- [x] Tras un POST con error, el formulario se re-renderiza con los datos tecleados conservados y un mensaje de error visible. El codigo HTTP devuelto es coherente (400, 404, 409).
- [x] Las eliminaciones requieren confirmacion: GET muestra la pantalla "seguro?" con los datos del recurso, POST sobre la misma URL ejecuta la baja y redirige.
- [x] Las rutas viejas de escritura (las que en ut4e1 aceptaban GET con los datos en la URL) se han reestructurado siguiendo los patrones del lab a5: formulario propio, confirmacion GET + accion POST, o ruta solo-POST segun corresponda.
- [x] Verificacion final recorriendo la app: ninguna URL accesible por GET modifica estado del dominio.
- [x] `domain/` e `infrastructure/` sin cambios; `application/` solo con metodos de delegacion pura si los hay.
- [x] `presentation/menu.py` sigue funcionando sin cambios.
- [x] `CHANGELOG.md` con entrada nueva `0.8.0`.
- [x] `README.md` y `docs/EJECUCION.md` actualizados con la lista de rutas y los verbos HTTP que acepta cada una.
