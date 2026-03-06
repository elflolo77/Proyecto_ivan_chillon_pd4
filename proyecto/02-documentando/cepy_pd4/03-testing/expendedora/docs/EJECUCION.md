# Ejecucion

## Requisitos
- Python 3.10+.
- Ejecutar desde la carpeta padre que contiene el paquete `expendedora/`.
- `coverage` para generar reportes de cobertura de tests.

## Clonar repositorio
```bash
git clone ssh://git@codeberg.org/ichigar/cepy_pd4.git
cd cepy_pd4/proyecto/03-testing
```

## Preparar entorno
```bash
cd expendedora
python -m venv .venv
source .venv/Scripts/activate               # GitBash
source .venv/Scripts/Activate.ps1           # PowerShell
pip install -r requirements.txt
cd ..
```

## Ejecutar menu
```bash
python -m expendedora.presentation.menu
```

## Ejecutar tests y cobertura
```bash
python -m unittest
coverage run -m unittest
coverage report
```

## Flujo rapido de ejemplo
1. Opcion 1: Mostrar productos.
2. Opcion 2: Seleccionar producto (ej. A1).
3. Opcion 3: Insertar dinero (ej. 2.00).
4. Opcion 4: Comprar.

## Errores comunes
- "El codigo no existe." si se selecciona un codigo inexistente.
- "Saldo insuficiente" si no se inserta dinero suficiente.
- "No hay stock disponible" si la cantidad es 0.
