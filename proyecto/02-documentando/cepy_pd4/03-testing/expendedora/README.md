# Maquina expendedora por capas

Proyecto de ejemplo para practicar arquitectura por capas (presentation, application, domain, infrastructure) y testing con `unittest` + `coverage`.

## Estado de la fase
Esta carpeta corresponde a la fase `03-testing`.

## Requisitos
- Python 3.10+ (recomendado 3.11+).
- Dependencias de test en `requirements.txt` (incluye `coverage`).

## Quickstart
Desde `proyecto/03-testing`:

```bash
cd expendedora
python -m venv .venv
source .venv/Scripts/activate               # GitBash
source .venv/Scripts/Activate.ps1           # PowerShell
pip install -r requirements.txt
cd ..
python -m expendedora.presentation.menu
```

## Uso (menu de consola)
Ejecuta desde la carpeta padre que contiene el paquete `expendedora/`:

```bash
python -m expendedora.presentation.menu
```

El menu permite: listar productos, seleccionar, insertar saldo, comprar (devuelve cambio), cancelar (devuelve saldo), reponer stock y crear productos con descuento.

## Tests
Ejecutar toda la suite:

```bash
python -m unittest
```

Ejecutar por modulo:

```bash
python -m unittest expendedora.tests.test_item
python -m unittest expendedora.tests.test_maquina
```

Cobertura:

```bash
coverage run -m unittest
coverage report
coverage html
```

El reporte HTML queda en `htmlcov/index.html`.

## Estructura del proyecto
```text
expendedora/
  presentation/
    menu.py
  application/
    servicios.py
  domain/
    item.py
    maquina.py
    repositorio_productos.py
  infrastructure/
    datos_iniciales.py
    repositorio_memoria.py
  tests/
    test_item.py
    test_maquina.py
  docs/
  requirements.txt
```

- `presentation/menu.py`: interfaz de consola.
- `application/servicios.py`: orquestacion de casos de uso.
- `domain/`: entidades, validaciones y reglas de negocio.
- `infrastructure/`: repositorio en memoria y datos iniciales.
- `tests/`: pruebas unitarias con `unittest`.
- `docs/`: documentacion funcional y tecnica de la fase.

## Documentacion
Indice y detalle en `docs/README.md`.

## Changelog
Historial de cambios en `CHANGELOG.md`.
