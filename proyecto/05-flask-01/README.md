
# Fase 02: Documentación y Refactorización del Diseño en Capas

## Descripción General
Este directorio (`02-documentando`) contiene la evolución del proyecto base originado en la fase 01. En esta fase se ha garantizado la correcta estructuración del código orientándose en Patrones de Diseño, aplicando convenciones de código (PEP-8) y ampliando exhaustivamente la documentación teórica.

## Documentación del Proyecto
Toda la documentación arquitectónica, funcional y de reglas de negocio reside encapsulada en la carpeta `docs/`.

Por favor, comienza tu lectura en el índice global:
👉 **[Acceder a docs/README.md](docs/README.md)**

## Instrucciones Rápidas

Para probar la lógica implementada asilada de Base de Datos en memoria:

1. Abre tu terminal y cerciórate de que te encuentras sobre la raíz de la fase actual:
```powershell
cd proyecto/02-documentando
```

2. Ejecuta el programa:
```powershell
python main.py
```

<details open>
  <summary>Fase 02 - documentando</summary>

- [x] Copiado en subcarpeta `02-documentando` el contenido actual de la carpeta `01-diseno_capas` o se crea una nueva rama para la nueva etapa (antes crear la rama 01-diseno-capas).
- [x] Renombrar todos los identificadores de modulos, clases, métodos y variables que no cumplan con los [criterios de los apuntes](https://ichigar.codeberg.page/pd4/ut1/recursos/poo_ut1_6_documentacion/#eligiendo-nombres)
- [x] Añadir docstring a los módulos, clases y métodos públicos del proyecto siguiendo los [criterios de los apuntes](https://ichigar.codeberg.page/pd4/ut1/recursos/poo_ut1_6_documentacion/#eligiendo-nombres).
- [x] Comentar las reglas de negocio de las clases del dominio.
- [x] Comentar los bloques de código que no expresen claramente para qué se usan.
- [x] Eliminar comentarios evidentes.
#### Usando como referencia los [documentos del proyecto model](https://codeberg.org/ichigar/cepy_pd4/src/branch/main/proyecto/02-documentando/expendedora) añadir los siguientes ficheros:
- [x] README.md
- [x] CHANGELOG.md
- [x] `docs/README.md`
- [x] `docs/DESCRIPCION_Y_ALCANCE.md`
- [x] `docs/EJECUCION.md`
- [x] `docs/ARQUITECTURA_POR_CAPAS.md`
- [x] `docs/CASOS_DE_USO.md`
- [x] `docs/REGLAS_DE_NEGOCIO.md`
- [x] `docs/MODELO_DE_DOMINIO.md`
- [x] `docs/CONTRATO_REPOSITORIO.md`
- [x] `docs/DATOS_INICIALES.md`
- [x] `docs/TESTS_Y_PASOS.md`
- [x] `docs/TROUBLESHOOTING.md`
</details>

# FASE III. TESTING
## Instrucciones

Para probar la lógica y las pruebas unitarias en esta fase del proyecto:

1. Abre tu terminal en la raíz de la fase actual:
```powershell
cd proyecto/03-testing
```

2. Ejecutar la aplicación:
```powershell
python main.py
```

3. Ejecutar las pruebas unitarias:
```powershell
python -m unittest discover cine_multiplex/tests
```

4. Ejecutar reporte de cobertura:
```powershell
coverage run -m unittest discover cine_multiplex/tests; coverage report
```

### Ejecución Fase 05 (Flask Web App)

1. Abre tu terminal en la raíz de la fase actual:
```powershell
cd proyecto/05-flask-01
```

2. Instala dependencias necesarias:
```powershell
pip install -r requirements.txt
```

3. Ejecuta la aplicación Flask:
```powershell
python -m cine_multiplex.presentation.app
```
La aplicación web quedará expuesta en `http://127.0.0.1:5000/`.

<details>
  <summary>Fase 03 - testing</summary>

- [x] Copiar en `03-testing` el estado base de `02-documentando` (o crear rama especifica para la fase 03).
- [x] Reorganizar las pruebas en la subcarpeta `tests/`.
- [x] Crear y mantener test para, al menos, dos clases del dominio.
- [x] Verificar que todos los test pasan con `python -m unittest`.
- [x] Anadir `coverage` como dependencia de fase (en `requirements.txt`).
- [x] Ejecutar cobertura con `coverage run -m unittest` y revisar reporte con `coverage report`.
- [x] Documentar la ejecucion de tests y coverage en `docs/TESTS_Y_PASOS.md`.
- [x] Actualizar `docs/EJECUCION.md` con pasos completos desde clonado hasta ejecucion.
- [x] Revisar y corregir documentos desactualizados de `docs/` para reflejar la fase 03.
- [x] Registrar los cambios de fase en `CHANGELOG.md` (version `0.3.0`).
- [x] Actualizar `README.md` para reflejar estructura y comandos actuales.

</details>
<details open>
  <summary>Fase 04 - persistencia con SQLite</summary>

### Diseño e implementación del esquema de base de datos

- [x] Copiar en `04-sqlite` el estado base de `03-testing` (o crear rama específica para la fase 04).
- [x] Diseñar las tablas SQL mapeando cada entidad de dominio a tablas con sus columnas, tipos y restricciones (`PRIMARY KEY`, `NOT NULL`, `FOREIGN KEY`).
- [x] Usar nombres de columnas en snake_case.

### Script de inicialización de base de datos

- [x] Crear script que cree el esquema de la BD e inserte datos iniciales de prueba
  - Debe poder ejecutarse varias veces sin error
  - Crea todas las tablas respetando dependencias de claves foráneas
  - Inserta datos iniciales para probar la aplicación

### Excepciones de dominio para persistencia

- [x] (*opcional*) Crear fichero de excepciones (`infrastructure/errores.py`) con las excepciones que el repositorio SQLite lanza al usuario
  - Clase base para todas las excepciones de persistencia
  - Excepciones por cada tipo de error que puede ocurrir (duplicado, no encontrado, etc.)

### Implementación del repositorio SQLite

- [x] Crear clase(s) de repositorio que implementen persistencia en SQLite (realizando las mismas operaciones que el repositorio en memoria: guardar, obtener, actualizar, eliminar, etc.)
- [x] Usar consultas SQL parametrizadas (parámetros `?`) para prevenir inyección SQL
- [x] Capturar excepciones SQLite (`sqlite3.IntegrityError`, `sqlite3.OperationalError`, etc.) y transformarlas en excepciones de dominio
- [x] Activar `PRAGMA foreign_keys = ON` al conectar para garantizar integridad referencial
- [x] **El flujo principal de la aplicación (menú) debe usar SOLO el repositorio SQLite para persistencia** (no usar en memoria)

### Repositorio en memoria (referencia, no en uso)

- [x] (**opcional**) Mantener el código del repositorio en memoria como referencia de implementación y contrato
- [x] (**opcional**) Modificar `infrastructure/repositorio_memoria.py` para lanzar las **mismas excepciones de dominio** que el repositorio SQLite (útil para tests sin persistencia)

### Integración con SQLite en la capa de presentación

- [x] Modificar la capa de presentación para cargar datos iniciales desde la BD en lugar de desde memoria (al iniciar la aplicación)
- [x] Capturar excepciones de dominio, no excepciones de `sqlite3`
- [x] (*opcional*) Mostrar mensajes amigables al usuario cuando ocurran errores de persistencia
- [x] No hacer imports de `sqlite3` directamente en la presentación.

### Actualización de los tests

- [x] *(opcional)* Actualizar tests existentes para esperar excepciones de dominio en lugar de excepciones genéricas de Python
- [x] Verificar que `python -m unittest` pasa con todos los tests en verde
- [x] *(opcional)* Crear tests específicos para el repositorio SQLite

### Documentación

- [x] Actualizar `CHANGELOG.md` (versión `0.4.0`) con los cambios principales
- [x] Actualizar `README.md` con instrucciones de cómo ejecutar el script de inicialización
- [x] Documentar el diseño de la BD en `docs/DISEÑO_BD.md`:
- [x] (*opcional*) Documentar el contrato de excepciones en `docs/CONTRATO_EXCEPCIONES.md`:

### Verificación final

- [x]a aplicación funciona igual desde el punto de vista del usuario (mismo menú, mismas operaciones)
- [x]Los datos persisten entre ejecuciones (cierra y reabre la app, verifica que los datos están)
- [x] Los tests pasan todos sin cambios de lógica de dominio
</details>

# FASE 05: Flask Web Application

## Checklist para esta fase
[x] Carpeta 05-flask-01/ creada con el contenido de 04-sqlite/ como base.
[x] requirements.txt incluye flask.
[x] presentation/app.py ejecutable con python -m {paquete}.presentation.app.
[x] Route / con mensaje de bienvenida y enlaces a las rutas principales.
[x] Todas las operaciones del menú de consola expuestas como routes, incluyendo:
Consultas (listados, detalles por identificador, búsquedas).
Acciones que modifican datos (altas, bajas, ediciones, reposiciones, reservas, cambios de estado…). Más adelante se ajustarán para usar POST al ver los formularios.
Operaciones transaccionales o con estado intermedio (selecciones previas a una compra, confirmaciones, etc.), modeladas como la máquina de estados del lab a2. Solo se puede dejar alguna ruta fuera si no tiene sentido sin elementos que todavía no se han visto (por ejemplo, operaciones que requieren autenticación de usuarios o subida de ficheros).
[x] Los routes usan <codigo>, <int:id>, <float:precio>… para los parámetros tipados.
[x] Los routes que modifican datos redirigen con redirect(url_for(...)) tras la acción (patrón "actúa → redirige").
[x] Todas las excepciones de dominio capturadas en menu.py están también capturadas en los routes correspondientes con el código HTTP apropiado (404 para "no encontrado", 409 para conflicto de estado como duplicado, 400 para datos inválidos).
[x] En generar se siguen las indicaciones del documento  UAE1_GUIA_FLASK.md añadido al repositorio por el profesor.
[x] presentation/menu.py sigue funcionando sin cambios.
[x] CHANGELOG.md con entrada nueva.
[x] README.md y docs/EJECUCION.md actualizados con el comando de arranque y las rutas expuestas.
