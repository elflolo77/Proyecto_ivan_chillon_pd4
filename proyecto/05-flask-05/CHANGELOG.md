# Changelog

En este documento se incluyen los cambios por entrega/version (nuevas funcionalidades, cambios, correcciones y notas de compatibilidad):
- Added
- Changed
- Fixed
- Removed
- Security
-  Compatibility / Breaking changes (Compatibilidad)

---
## [0.10.0] - 2026-05-28 (Fase 05e: Mensajes Flash y API REST Mínima)

Versión disponible en la subcarpeta `05-flask-05`.

### Added
- Configuración de `app.secret_key` para firmar cookies de sesión para los mensajes flash.
- Mensajes flash de confirmación/éxito integrados en los flujos de escritura: registrar películas (comercial, infantil, clásica), crear sala, programar sesión, vender entrada y anular entrada.
- Bloque de visualización de mensajes flash por categoría en `base.html`.
- API REST mínima con endpoints en formato JSON que comparten la misma capa de aplicación (`ServicioCine`):
  - `GET /api/peliculas` — lista todas las películas.
  - `GET /api/peliculas/<titulo>` — detalle de una película por título (404 si no existe).
  - `GET /api/sesiones` — lista todas las sesiones.
  - `GET /api/sesiones/<id>` — detalle de una sesión por identificador (404 si no existe).
- Nuevas plantillas específicas separadas para formularios de película por tipo (`form_pelicula_comercial.html`, `form_pelicula_infantil.html`, `form_pelicula_clasica.html`), de acuerdo con los estándares y simplificación de la unidad.

### Changed
- El repositorio SQLite (`RepositorioSQLite`) ahora usa gestión directa de conexión/cursor estándar (`try/finally`), eliminando el uso de `closing` de `contextlib` y la abstracción genérica de ejecución SQL que no se correspondía con lo enseñado en clase.
- Modificado el mapeo de películas en el repositorio SQLite usando diccionarios polimórficos de creación en lugar de cadenas complejas de `isinstance` y discriminación por tipo en el guardado.
- Reconstrucción de entidades de dominio en el repositorio respetando la encapsulación de la orientación a objetos, pasando los parámetros al constructor en lugar de asignar directamente sus atributos protegidos (`_id_entrada`, `_fecha_venta`, `_numero_asientos_ocupados`, `_estado_sesion`).
- Eliminadas las comprobaciones defensivas innecesarias de tipos en la capa de aplicación.

---
## [0.8.0] - 2026-05-25 (Fase 05d: Formularios HTML y POST)

Version disponible en la subcarpeta `05-flask-04`.

### Added
- Formularios HTML en `cine_multiplex/presentation/templates/` para las operaciones de escritura.
- Rutas `GET`/`POST` para registrar peliculas, crear salas, programar sesiones, vender entradas y anular entradas.
- Pantalla de confirmacion para anular entradas antes de ejecutar la baja.

### Changed
- Las rutas de escritura ya no modifican estado mediante `GET` con datos en la URL.
- Las operaciones con `POST` correcto aplican Post/Redirect/Get hacia rutas de lectura.
- Los formularios con error se vuelven a renderizar conservando los datos introducidos y mostrando un mensaje.
- Actualizados `README.md` y `docs/EJECUCION.md` con rutas y verbos HTTP.

### Compatibility
- `domain/`, `infrastructure/` y `presentation/menu.py` sin cambios.

---
## [0.7.0] - 2026-05-25 (Fase 05c: Plantillas Jinja2)

Versión disponible en la subcarpeta `05-flask-03`

### Added
- Plantillas Jinja2 en `cine_multiplex/presentation/templates/`.
- Plantilla base `base.html` con la estructura común, cabecera de navegación y bloques reutilizables.
- Plantillas hijas extendiendo de `base.html` para las rutas de lectura, la página `/ayuda` y los errores 404/500.
- Uso de `render_template` en las rutas que muestran información, evitando HTML inline.
- Conversión de colecciones/tuplas a diccionarios cuando fue necesario para simplificar la inyección de datos.

### Changed
- Actualizado `README.md` y `docs/EJECUCION.md` para documentar la nueva carpeta de templates y el patrón de herencia con `base.html`.

### Compatibility
- `domain/` e `infrastructure/` sin cambios; `presentation/menu.py` sigue funcionando sin cambios.

---
## [0.6.0] - 2026-05-22 (Fase 05b: Observabilidad Flask)

Version disponible en la subcarpeta `05-flask-02`

### Added
- Manejadores globales `@app.errorhandler(404)` y `@app.errorhandler(500)` con respuestas HTML personalizadas.
- Ruta `/ayuda` generada mediante `app.url_map.iter_rules()` para listar automaticamente las rutas registradas.
- Configuracion de logging en `presentation/app.py` con salida a `cine_multiplex.log`.
- Hook `@app.before_request` para registrar cada peticion con metodo HTTP y ruta.
- `.gitignore` con `*.log` para evitar versionar ficheros de log.

### Changed
- Actualizados `README.md` y `docs/EJECUCION.md` con instrucciones de observabilidad, ruta `/ayuda` y notas sobre logging.

### Compatibility
- No hay cambios incompatibles: la API web existente, el menu de consola y las capas `domain/`, `application/` e `infrastructure/` mantienen su comportamiento.

---
## [0.5.0] - 2026-05-13 (Fase 05: Flask Web Application)

Versión disponible en la subcarpeta `05-flask-01`

### Added
- Nueva aplicación web con Flask en `presentation/app.py`.
- Rutas expuestas para consultar y modificar entidades del dominio (Películas, Salas, Sesiones, Entradas, Informes).
- Redireccionamiento con patrón PRG (Post/Actúa -> Redirect -> Get) en rutas de acción.
- Captura de excepciones de dominio en cada ruta, traduciéndolas a códigos de estado HTTP pertinentes (404, 400, 409, 500).

### Changed
- Actualización de `requirements.txt` añadiendo la dependencia `flask`.
- Actualización de `README.md` y `docs/EJECUCION.md` con las instrucciones para arrancar Flask.

---
## [0.4.0] - 2026-05-05 (Fase 04: persistencia SQLite)

Versión disponible en la subcarpeta `04-sqlite`

### Added
- Script `crear_bd.py` para crear el esquema de la base de datos e insertar datos iniciales.
- Implementación de `RepositorioSQLite` que persiste entidades (Películas, Salas, Sesiones, Entradas).
- Excepciones de dominio en `infrastructure/errores.py`.
- Documentación de BD (`docs/DISEÑO_BD.md`) y contrato de excepciones (`docs/CONTRATO_EXCEPCIONES.md`).
- Tests específicos para el repositorio SQLite (`tests/test_repositorio_sqlite.py`).

### Changed
- El menú de consola ahora utiliza `RepositorioSQLite` de manera exclusiva y maneja excepciones de dominio.
- `RepositorioMemoria` actualizado para lanzar las mismas excepciones de dominio que el de SQLite.

---
## [0.3.0] - 2026-04-15 (Fase 03: testing)

Versión disponible en la subcarpeta `03-testing`

### Added
- Infraestructura de pruebas unitarias con el framework `unittest`.
- Paquete `cine_multiplex/tests/` para organizar las pruebas.
- Pruebas unitarias para la clase `Pelicula` y sus subclases (`PeliculaComercial`, `PeliculaInfantil`, `PeliculaClasica`).
- Pruebas unitarias para la clase `Sala`.
- Dependencia `coverage` en `requirements.txt` para medir la cobertura del código.

### Changed
- Actualizada la documentación para reflejar el proceso de ejecución de tests y reporte de cobertura.
- Modificado `README.md` con la estructura de la fase 03 y comandos actualizados.

---

## [0.2.0] - 2026-02-27 (Fase 02: documentación)

Versión disponible en la subcarpeta `02-documentando`

### Added
- Documentación de la fase en `docs/` (descripción y alcance, ejecución, arquitectura por capas, casos de uso, reglas de negocio, modelo de dominio, contrato de repositorio, datos iniciales, tests/pasos y troubleshooting).
- Comentarios en el código centrados en el **por qué** (reglas de negocio, normalización, supuestos y efectos laterales) para aclarar segmentos no obvios.
- `CHANGELOG.md` para registrar la evolución por entregas.

### Changed
- Modificado `README.md` para incluir los aspectos recogidos en los apuntes sobre documentación

## [0.1.0]  - 2026-03-03
 (Fase 01: versión inicial)

Versión disponible en la subcarpeta `01-diseno_capas`

### Added
- Aplicación base de máquina expendedora por capas:
  - Menú de consola en `presentation/`.
  - Servicios/casos de uso en `application/`.
  - Entidades y reglas de negocio en `domain/` (items, descuentos, compra/cancelación, stock).
  - Repositorio en memoria y datos iniciales en `infrastructure/`.
- Tests `test_*.py` para validar el comportamiento principal por pasos.

