# Tests y pasos

## Ejecucion de pruebas
Desde la carpeta padre que contiene el paquete `expendedora/`:

```bash
python -m unittest
```

Tambien puedes ejecutar solo para un módulo concreto:

```bash
python -m unittest expendedora.tests.test_item
python -m unittest expendedora.tests.test_maquina
```

## Que valida cada test
- `tests/test_item.py`: validaciones de `Item` y `ItemConDescuento` (codigo, nombre, precio, cantidad, descuento, precio final y formato de salida).
- `tests/test_maquina.py`: flujos principales de `MaquinaExpendedora` con datos iniciales (seleccion, saldo, compra, cambio, reposicion, cancelacion y actualizacion de stock).

## Pruebas de coverage
Desde la carpeta padre que contiene el paquete `expendedora/`:

```bash
coverage run -m unittest
```

Generar reporte en consola:

```bash
coverage report
```

Generar reporte HTML:

```bash
coverage html
```

El reporte se consulta en `htmlcov/index.html`.
