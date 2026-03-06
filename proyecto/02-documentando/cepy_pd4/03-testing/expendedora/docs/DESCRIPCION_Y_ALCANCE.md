# Descripcion y alcance

## Descripcion funcional
La aplicacion simula una maquina expendedora con un menu de consola. Permite listar productos, seleccionar un producto, insertar dinero, comprar, cancelar, reponer stock, agregar productos y agregar productos con descuento.

## Objetivos de las fases implementadas
- Practicar la separacion por capas (presentation, application, domain, infrastructure).
- Concentrar reglas de negocio en el dominio.
- Mostrar como un repositorio abstracto permite cambiar el almacenamiento.
- Estandarizar la bateria de pruebas con `unittest` dentro de `tests/`.
- Documentar como ejecutar pruebas y cobertura.

## Alcance
Incluye:
- Menu de consola (`presentation/menu.py`).
- Servicio de aplicacion (`application/servicios.py`).
- Entidades y reglas del dominio (`domain/item.py`, `domain/maquina.py`).
- Repositorio en memoria y datos iniciales (`infrastructure/`).
- Tests automatizados en `tests/test_item.py` y `tests/test_maquina.py`.

No incluye:
- Persistencia real (BD/archivos), interfaz grafica, pagos reales, autenticacion.
- Gestion de monedas/billetes con inventario.
- Concurrencia o multiples usuarios.

## Supuestos y limites
- Precios y saldo en euros (float).
- Codigo de producto con letra + numero (ej. A1).
- Stock entero >= 0.
