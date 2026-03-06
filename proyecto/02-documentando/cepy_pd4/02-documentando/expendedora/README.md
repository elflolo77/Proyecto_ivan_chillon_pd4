# Máquina expendedora por capas

Proyecto de ejemplo para practicar **documentación** y **arquitectura por capas** (presentación, aplicación, dominio e infraestructura) con una máquina expendedora. La propuesta concentra las **reglas de negocio** en el dominio para poder reemplazar fácilmente el almacenamiento.

## Quickstart

Desde la carpeta que contiene `expendedora/`:

```bash
python -m expendedora.presentation.menu
```

## Requisitos

- Python 3.10+ (recomendado 3.11+).
- No requiere dependencias externas (solo librería estándar).
- No hay requisitos específicos de sistemas operativo.

## Uso (menú de consola)

Ejecuta:

```bash
python -m expendedora.presentation.menu
```

El menú permite: listar productos, seleccionar, insertar saldo, comprar (devuelve cambio), cancelar (devuelve saldo), reponer stock y crear productos con descuento.

## Estructura del proyecto (por capas)

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
  docs/
  test_*.py
```

- `presentation/menu.py`: interfaz de consola que solo pide datos y muestra resultados.
- `application/servicios.py`: coordina los casos de uso sobre la `MaquinaExpendedora` sin exponer la lógica interna.
- `domain/`: alberga las entidades (`Item`, `ItemConDescuento`), las validaciones, la máquina y el contrato `RepositorioProductos`.
- `infrastructure/`: contiene los datos iniciales y el repositorio en memoria (`RepositorioProductosMemoria`) empleado por la máquina.
- `test_*.py`: pruebas sencillas que validan cada paso sin depender de `input()` ni `print()`.

## Documentación
Consulta la documentación detallada de la fase en `doc/` (índice en [doc/README.md](doc/README.md)).

## Tests (comprobación rápida)

Estos tests están pensados para ejecutarse como módulos, uno a uno:

```bash
python -m expendedora.test_item
python -m expendedora.test_item_descuento
python -m expendedora.test_paso2_repo_memoria
python -m expendedora.test_maquina_parte1
python -m expendedora.test_maquina_parte2
python -m expendedora.test_repo_no_sobrescribir
python -m expendedora.test_eliminar_repo
python -m expendedora.test_servicio
python -m expendedora.test_contrato
python -m expendedora.test_datos_iniciales
```

