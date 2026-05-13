# Changelog

En este documento se incluyen los cambios por entrega/version (nuevas funcionalidades, cambios, correcciones y notas de compatibilidad):
- Added
- Changed
- Fixed
- Removed
- Security
-  Compatibility / Breaking changes (Compatibilidad)

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
