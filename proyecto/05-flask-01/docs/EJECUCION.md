# Guía de Ejecución — Fase 05 (Flask Web Application 01)

Esta guía describe cómo inicializar, ejecutar y probar la aplicación "Cine Flolix" en su versión web con Flask y su versión tradicional de consola, ambas persistiendo en SQLite.

## Requisitos previos
- **Python**: Se requiere Python 3.9 o superior.
- **Dependencias**: Se requieren los paquetes `flask` y `coverage`. Asegúrate de instalarlos mediante el archivo `requirements.txt`:
  ```powershell
  pip install -r requirements.txt
  ```

---

## Inicialización de la Base de Datos

Antes de ejecutar la aplicación por primera vez, puedes inicializar manualmente la base de datos `cine.db` con el esquema físico y los datos iniciales de prueba.

Ubica tu terminal en la raíz de esta fase del proyecto (`proyecto/05-flask-01`) y ejecuta:
```powershell
python crear_bd.py
```
> [!NOTE]
> Este paso es opcional, ya que tanto la aplicación de consola (`main.py`) como la web con Flask (`app.py`) autocrean de forma dinámica la base de datos `cine.db` si detectan que no existe al arrancar.

---

## Ejecución de la Aplicación Web (Flask)

Para arrancar el servidor web de Flask, ubica tu terminal en la raíz de esta fase del proyecto (`proyecto/05-flask-01`) y ejecuta:
```powershell
python -m cine_multiplex.presentation.app
```

La aplicación se servirá localmente en: `http://127.0.0.1:5000/`

### Rutas Web Disponibles
- **Página de Inicio:** `/` (menú con enlaces principales)
- **Películas:**
  - Ver catálogo: `/peliculas`
  - Registrar comercial: `/peliculas/registrar_comercial/<titulo>/<duracion>/<clasificacion>/<genero>/<distribuidora>`
  - Registrar infantil: `/peliculas/registrar_infantil/<titulo>/<duracion>/<clasificacion>/<genero>/<edad_minima>`
  - Registrar clásica: `/peliculas/registrar_clasica/<titulo>/<duracion>/<clasificacion>/<genero>/<anio>`
- **Salas:**
  - Ver salas: `/salas`
  - Crear sala: `/salas/crear/<numero_sala>/<capacidad_maxima>/<tecnologia_pantalla>`
- **Sesiones:**
  - Ver sesiones: `/sesiones`
  - Programar sesión: `/sesiones/programar/<identificador>/<titulo_pelicula>/<int:numero_sala>/<fecha_hora>`
- **Entradas:**
  - Vender entrada: `/entradas/vender/<identificador_sesion>/<categoria_tarifa>`
  - Anular entrada: `/entradas/anular/<identificador_entrada>`
- **Informes:**
  - Informe de ventas: `/informe`

---

## Ejecución de la Aplicación de Consola

Puedes seguir ejecutando la interfaz de consola interactiva. Para ello, ubica tu terminal en `proyecto/05-flask-01` y ejecuta:
```powershell
python main.py
```

---

## Ejecución de Pruebas Unitarias

Para ejecutar las pruebas unitarias:
```powershell
python -m unittest discover cine_multiplex/tests -v
```

### Cobertura de Código
```powershell
coverage run -m unittest discover cine_multiplex/tests
coverage report
```
