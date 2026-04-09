# Revisión del proyecto — Alejandro (Cine Flolix)

**Fuente de verdad:** `proyecto/02-documentando/`
**Fases detectadas:** 01 (capas), 02 (documentación) — carpetas `01-diseno_capas/` y `02-documentando/` dentro de `proyecto/`

## REVISIÓN FASE 01 - 2026-03-03 — Nota: 6,5/10

### Cumple

- Repositorio creado y compartido con el profesor.
- Subcarpeta `proyecto/` presente en el repositorio con carpeta de fase `01-diseno_capas/`.
- El proyecto está organizado en capas: `domain/`, `application/`, `infrastructure/`, `presentation/` bien separadas dentro del paquete `cine_multiplex/`.
- Estructura de ficheros correcta: paquetes con `__init__.py`, módulos bien separados.
- POO aplicado correctamente: herencia (`PeliculaComercial`, `PeliculaInfantil`, `PeliculaClasica` heredan de `Pelicula`), encapsulamiento con propiedades (`@property`), contrato de repositorio como clase abstracta definido en `domain/`.
- Nombres de ficheros, clases y variables significativos y conformes a PEP8.

### Errores y aspectos a mejorar

- **[IMPORTANTE] `README.md` — Las instrucciones de ejecución apuntan a `01-diseno_capas` y tienen una ruta de Windows específica de tu equipo (`d:\Users\Pepito\Documents\...`) que no sirve para nadie más.**
  - *Cómo resolverlo:* Actualiza el README para que las instrucciones apunten a la carpeta correcta de la fase actual y usa rutas relativas o instrucciones genéricas (p. ej., "navega hasta el directorio `01-diseno_capas/`").

- **[BUG] `presentation/menu.py:59` — `duracion = int(input(...))` está fuera del bloque `try` que empieza en la línea 63.** Si el usuario escribe texto en lugar de un número, el programa termina con un `ValueError` sin capturar.
  - *Cómo resolverlo:* Mueve la conversión `int()` dentro del bloque `try` correspondiente, o añade un `try/except ValueError` propio para esa línea.

- **[BUG] `presentation/menu.py:111` — `sala = int(input(...))` también está fuera del `try` que empieza en la línea 113.** Mismo crash con entrada no numérica.
  - *Cómo resolverlo:* Igual que el punto anterior: mueve la conversión dentro del bloque `try`.

- **[BUG] `application/servicio_cine.py:anular_entrada` — La funcionalidad de anular entradas no tiene ninguna opción en el menú; es completamente inaccesible desde la UI.** Además, si se añadiera al menú, el método tiene dos bugs adicionales: la línea 115 accede directamente a `self.repo.entradas` rompiendo el encapsulamiento, y la línea 117 llama a `self.repo.guardar_datos()` que no existe en `RepositorioMemoria`, lo que provocaría un `AttributeError`.
  - *Cómo resolverlo:* Añade una opción de submenú en ventas para anular entradas. Añade `eliminar_entrada(id)` en `RepositorioMemoria` (y decláralo en la interfaz `RepositorioCine`) y úsalo desde el servicio en lugar de `self.repo.entradas.remove(...)`. Elimina la llamada a `guardar_datos()`.

- **[DISEÑO] `application/servicio_cine.py:59` — La variable `sesiones_sala` se calcula pero nunca se usa: la validación de solapamiento de sesiones no está implementada.** El comentario indica que era una intención pero quedó sin terminar. Es posible programar dos películas en la misma sala a la misma hora sin que el sistema lo detecte.
  - *Cómo resolverlo:* Usa `sesiones_sala` para comprobar si alguna sesión existente en esa sala coincide en horario con la nueva y lanza `ValueError` si hay conflicto. O elimina el comentario y la variable si no vas a implementarlo en esta fase.

- **[DISEÑO] `domain/entrada.py:13` — `self._fecha_venta = None` se declara en el constructor pero nunca se le asigna un valor real.** Siempre devolverá `None`.
  - *Cómo resolverlo:* Asígnale la fecha actual en el propio constructor: `from datetime import datetime` y `self._fecha_venta = datetime.now()`.

- **[DISEÑO] `application/servicios.py` y `cine_multiplex/cine_db.json` — Ficheros huérfanos sin usar.** `servicios.py` contiene una clase `ServicioCine` alternativa con métodos que lanzan `NotImplementedError` o llaman a atributos inexistentes (`pelicula.codigo()`, `sala.numero()`). `cine_db.json` no está referenciado en ningún fichero Python.
  - *Cómo resolverlo:* Elimina ambos ficheros del repositorio.


## REVISIÓN FASE 02 - 2026-03-03 — Nota: 3/10

### Cumple

- Código copiado a la carpeta `02-documentando/` correctamente.
- Docstrings de módulo presentes en la primera línea de todos los ficheros Python, antes de los imports.
- Docstrings de clases presentes en todas las clases: `Sesion`, `Pelicula`, `PeliculaComercial`, `PeliculaInfantil`, `PeliculaClasica`, `Sala`, `Entrada`, `RepositorioCine`, `RepositorioMemoria`, `ServicioCine`.
- Algunos métodos con docstring: `vender_entrada()` y `anular_entrada()` en `Sesion`; `programar_sesion()`, `vender_entrada()` y `anular_entrada()` en `ServicioCine`; `inicializar_repositorio()` en `datos_iniciales.py`.

### Errores y aspectos a mejorar

- **[IMPORTANTE] Falta la carpeta `docs/` completamente.** Es la principal entrega de la fase 02. Deben incluirse: `DESCRIPCION_Y_ALCANCE.md`, `EJECUCION.md`, `ARQUITECTURA_POR_CAPAS.md`, `CASOS_DE_USO.md`, `REGLAS_DE_NEGOCIO.md`, `MODELO_DE_DOMINIO.md`, `CONTRATO_REPOSITORIO.md`, `DATOS_INICIALES.md`, `TESTS_Y_PASOS.md`, `TROUBLESHOOTING.md`.
  - *Cómo resolverlo:* Crea la carpeta `docs/` dentro de `02-documentando/` y añade cada documento con contenido real. Toma como referencia el repositorio modelo de la máquina expendedora.

- **[IMPORTANTE] Falta `CHANGELOG.md`.** No existe ni en la raíz del repositorio ni en la carpeta de fase.
  - *Cómo resolverlo:* Crea `CHANGELOG.md` en `02-documentando/` con versión `0.2.0` y una sección que liste los cambios introducidos respecto a la fase 01. Usa como referencia el formato en el proyecto de la expendedora.

- **[IMPORTANTE] Docstrings de métodos incompletos.** Muchos métodos públicos no tienen docstring: todas las propiedades y `__init__` de `pelicula.py`; todos los métodos de `sala.py`; `registrar_pelicula_comercial()`, `listar_peliculas()`, `crear_sala()`, `informe_ventas()` y otros en `servicio_cine.py`; todos los métodos de `menu.py`.
  - *Cómo resolverlo:* Añade docstrings a todos los métodos públicos indicando qué hace, qué parámetros recibe y qué devuelve.

- **[IMPORTANTE] Reglas de negocio no comentadas en el dominio.** En `sesion.py` las reglas ("no se puede vender en sesión cancelada", "la sesión pasa a estado `completa` cuando no quedan asientos") no tienen comentarios que las identifiquen explícitamente.
  - *Cómo resolverlo:* Añade comentarios `# Regla de negocio: ...` junto a la lógica que impone cada regla en las clases del dominio.

- **[IMPORTANTE] `README.md` no actualizado para fase 02.** Sigue apuntando a `01-diseno_capas` con una ruta de Windows ficticia.
  - *Cómo resolverlo:* Actualiza el README para que refleje la fase actual (`02-documentando/`), describa los cambios introducidos respecto a la fase anterior y corrija las instrucciones de ejecución.

- **[SUGERENCIA] `infrastructure/datos_iniciales.py` — Variables `p1`, `p2`, `p3`, `s1`, `s2`, `s3` son poco descriptivas.**
  - *Cómo resolverlo:* Usa nombres como `pelicula_dune`, `pelicula_kung_fu`, `sala_imax`, etc.

- **[SUGERENCIA] `presentation/menu.py:60` — `clasif` es una abreviatura de `clasificacion`.**
  - *Cómo resolverlo:* Usa el nombre completo `clasificacion`.


## REVISIÓN FASE 03 - 2026-03-03 — Nota: 0/10

> Sin implementar.
