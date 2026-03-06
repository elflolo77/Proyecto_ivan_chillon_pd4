# Maquina expendedora por capas

Este paquete sirve como modelo para esta fase del proyecto: la idea es que el alumnado construya su propio trabajo con un alcance similar al de las actividades UT1-A8 y UT1-A9, pero con libertad para adaptar funciones y reglas. La propuesta muestra cómo separar responsabilidades siguiendo una arquitectura por capas (presentacion, aplicacion, dominio e infraestructura) y concentra todas las reglas de negocio en el dominio para poder reemplazar facilmente el almacenamiento.

## Proposito del proyecto
- Mostrar como crear una aplicacion ordenada manteniendo cohesion, encapsulacion y acoplamiento bajo.
- Permitir experimentar con un menu de consola que delega toda la logica en servicios y en el dominio.
- Facilitar la incorporacion de mejoras (descuentos, repositorios alternativos, persistencia externa) sin romper el nucleo del negocio.

## Estructura por capas
- `presentation/menu.py`: interfaz de consola que solo pide datos y muestra resultados.
- `application/servicios.py`: coordina los casos de uso sobre la `MaquinaExpendedora` sin exponer la logica interna.
- `domain/`: alberga las entidades (`Item`, `ItemConDescuento`), las validaciones, la maquina y el contrato `RepositorioProductos`.
- `infrastructure/`: contiene los datos iniciales y el repositorio en memoria (`RepositorioProductosMemoria`) empleado por la maquina.
- `test_*.py`: pruebas sencillas que validan cada paso sin depender de `input()` ni `print()`.

## Requisitos y ejecucion
1. Instala Python 3.10+ y ejecuta desde la raiz del paquete:
   ```bash
   python -m expendedora.presentation.menu
   ```
2. Para comprobar los componentes por separado, ejecuta cualquiera de estos tests:
   ```bash
   python -m expendedora.test_item
   python -m expendedora.test_item_descuento
   python -m expendedora.test_paso2_repo_memoria
   python -m expendedora.test_paso3_maquina
   python -m expendedora.test_repo_no_sobrescribir
   python -m expendedora.test_eliminar_repo
   ```




