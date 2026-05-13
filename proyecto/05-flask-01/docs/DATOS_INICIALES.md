# DATOS INICIALES (MOCKS)

Para facilitar la comprobación del código sin persistencia SQL funcional, el sistema incluye un poblador automático de entidades en memoria.

Se ejecuta al arrancar el programa. La rutina reside en `infrastructure/datos_iniciales.py` -> `inicializar_repositorio()`.

## Películas pre-cargadas
- Dune: Parte Dos (`PeliculaComercial`)
- Kung Fu Panda 4 (`PeliculaInfantil`)
- El Padrino (`PeliculaClasica`)

## Salas pre-cargadas
- Sala 1 (100 as., 2D)
- Sala 2 (50 as., 3D)
- Sala 3 (30 as., IMAX)

Al arrancar `main.py`, se dispone automáticamente de estos elementos para empezar el flujo de agendado de sesiones y venta de tickets sin requerir inserciones manuales pesadas constantes.
