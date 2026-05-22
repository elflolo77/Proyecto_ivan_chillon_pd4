# Guía de Ejecución — Fase 04 (SQLite)

Esta guía describe cómo inicializar, ejecutar y probar la aplicación "Cine Flolix" con persistencia en SQLite.

## Requisitos previos
- **Python**: Se requiere Python 3.9 o superior.
- **Dependencias**: Se requiere el paquete `coverage` para las pruebas unitarias y cobertura de código. Puedes instalarlo con:
  ```powershell
  pip install -r requirements.txt
  ```

---

## Inicialización de la Base de Datos

Antes de ejecutar la aplicación por primera vez, puedes inicializar manualmente la base de datos `cine.db` con el esquema físico y los datos iniciales de prueba (3 películas, 3 salas y 1 sesión de ejemplo).

Ubica tu terminal en la raíz de esta fase del proyecto (`proyecto/04-sqlite`) y ejecuta:
```powershell
python crear_bd.py
```
> [!NOTE]
> Este paso es opcional en el arranque inicial, ya que el punto de entrada de la aplicación (`main.py`) detectará automáticamente si `cine.db` no existe y la creará con la estructura inicial.

---

## Ejecución de la Aplicación (Consola)

Para iniciar la interfaz interactiva de consola de Cine Flolix, ubica tu terminal en la raíz de esta fase del proyecto (`proyecto/04-sqlite`) y ejecuta:
```powershell
python main.py
```

Una vez iniciada la aplicación, se mostrará el menú interactivo para realizar la gestión de películas, salas, sesiones, venta de entradas e informes estadísticos. Los datos introducidos se persistirán de manera permanente en el archivo local `cine.db`.

---

## Ejecución de Pruebas Unitarias

Para ejecutar el conjunto de pruebas unitarias asociadas a esta fase del proyecto, ejecuta:
```powershell
python -m unittest discover cine_multiplex/tests -v
```

### Reporte de Cobertura de Código

Si deseas comprobar el nivel de cobertura de los tests sobre el código fuente, ejecuta:
```powershell
coverage run -m unittest discover cine_multiplex/tests
coverage report
```
