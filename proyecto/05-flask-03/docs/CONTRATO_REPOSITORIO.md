# CONTRATO DEL REPOSITORIO

En **Cine Flolix**, la persistencia está desacoplada de la lógica de aplicación utilizando el patrón de diseño *Repository Pattern*.

## `RepositorioCine` (Interfaz Base)
Define el contrato mínimo que cualquier persistencia debe garantizar, definiendo firma para operaciones CRUD. 
La interfaz se halla en `domain/repositorio.py` y contiene:
- Métodos de Guardado (`guardar_pelicula`, `guardar_sala`, `guardar_sesion`, `guardar_entrada`).
- Métodos Getter Únicos (`obtener_pelicula_por_titulo`, `obtener_sala_por_numero`, `obtener_sesion_por_id`).
- Métodos Listadores Transversales.
- Método de eliminación de entradas (`eliminar_entrada`).

## `RepositorioMemoria` (Implementación Concreta)
Utilizada en esta iteración. Está construida en memoria RAM y localizada en la carpeta `infrastructure`.
- `_diccionario_peliculas`: Mapeo por título.
- `_diccionario_salas`: Mapeo por número.
- `_coleccion_entradas`: Lista local utilizada para guardar el historial de ventas.

El módulo de infraestructura satisface todas las cabeceras abstractas de la Interfaz base. Nunca un detalle lógico del entorno (`ServicioCine`) invoca explícitamente a las propiedades de clase.
