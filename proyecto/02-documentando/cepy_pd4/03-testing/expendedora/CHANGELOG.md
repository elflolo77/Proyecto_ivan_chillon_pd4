# Changelog

## [0.3.0] - 2026-02-13 (Fase 03: testing)

Version disponible en la subcarpeta `03-testing`

### Added
- Paquete de pruebas `tests/` con `tests/test_item.py` y `tests/test_maquina.py` usando `unittest` y descubrimiento de pruebas.
- Archivo `.gitignore` para excluir el entorno virtual local (`.venv/`).
- Guia en `docs/TESTS_Y_PASOS.md` para ejecutar pruebas con `python -m unittest` y medir cobertura con `coverage`.

### Changed
- `README.md` actualizado con flujo de entorno virtual para preparar y ejecutar el proyecto.
- `docs/EJECUCION.md` actualizado con pasos de preparacion del entorno y ejecucion.

### Removed
- Tests por pasos en la raiz del paquete (`test_*.py`) reemplazados por la estructura de pruebas en `tests/`.

## [0.2.0] - 2026-01-28 (Fase 02: documentaci�n)

Versión disponible en la subcarpeta `02-documentando`

### Added
- Documentaci�n de la fase en `docs/` (descripci�n y alcance, ejecuci�n, arquitectura por capas, casos de uso, reglas de negocio, modelo de dominio, contrato de repositorio, datos iniciales, tests/pasos y troubleshooting).
- Comentarios en el c�digo centrados en el **por qu�** (reglas de negocio, normalizaci�n, supuestos y efectos laterales) para aclarar segmentos no obvios.
- `CHANGELOG.md` para registrar la evoluci�n por entregas.

### Changed
- Modificado `README.md` para incluir los aspectos recogidos en los apuntes sobre documentaci�n

## [0.1.0]  - 2026-01-14 (Fase 01: versi�n inicial)

Versi�n disponible en la subcarpeta `01-diseno_capas`

### Added
- Aplicaci�n base de m�quina expendedora por capas:
  - Men� de consola en `presentation/`.
  - Servicios/casos de uso en `application/`.
  - Entidades y reglas de negocio en `domain/` (items, descuentos, compra/cancelaci�n, stock).
  - Repositorio en memoria y datos iniciales en `infrastructure/`.
- Tests `test_*.py` para validar el comportamiento principal por pasos.


