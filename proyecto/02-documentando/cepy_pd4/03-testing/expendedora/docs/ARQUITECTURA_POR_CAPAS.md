# Arquitectura por capas

El proyecto ha sido estructurado usando el diseno por capas.

## Capas y responsabilidades
- Presentation: entrada/salida por consola. No contiene reglas de negocio.
- Application: orquesta casos de uso sobre el dominio.
- Domain: entidades, validaciones y reglas de negocio.
- Infrastructure: repositorios concretos y datos iniciales.

## Dependencias permitidas
- presentation -> application -> domain
- infrastructure -> domain

No se debe depender de presentation desde domain ni application.

## Mapa de archivos
- `presentation/menu.py`: UI de consola.
- `application/servicios.py`: casos de uso.
- `domain/item.py`, `domain/maquina.py`, `domain/repositorio_productos.py`: nucleo.
- `infrastructure/repositorio_memoria.py`, `infrastructure/datos_iniciales.py`: adaptadores.
- `tests/test_item.py`, `tests/test_maquina.py`: pruebas automatizadas del dominio y de flujos principales.
