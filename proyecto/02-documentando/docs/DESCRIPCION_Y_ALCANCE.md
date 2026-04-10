# DESCRIPCIÓN Y ALCANCE

**Cine Flolix** (Fase 02) es una herramienta de simulación de un POS (Point Of Sale) de taquilla y gestión de cines bajo un backend CLI dictaminado por los principios arquitectónicos SOLID.

## Alcance del Software en la fase actual
### Permite: 
- Insertar Películas mediante atributos de sub-clases adaptadas.
- Organizar Salas estáticas.
- Programar la proyección de Sesiones.
- Operar compras de tickets aplicando una matriz de tarifas dinámica ("General", "Reducida", "Estudiante").
- Extracción de analítica básica sobre recuento y ganancias.

### Excluye deliberadamente:
- Persistencia real de datos (al salir del programa el estado mutado desaparece).
- Selección nominal de butacas por coordenadas dentro de una sesión.
- Lógica de red (Sin servidor Web).
- Interface de Usuario visual.

La arquitectura separa la lógica de dominio de la persistencia en memoria y mantiene el sistema simple y consistente con el código actual.
