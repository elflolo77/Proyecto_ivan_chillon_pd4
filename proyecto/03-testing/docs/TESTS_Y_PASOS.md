# PRUEBAS Y SIGUIENTES PASOS

## Pruebas Automatizadas (Fase 03)

Se han implementado pruebas unitarias para las clases principales del dominio para asegurar que las reglas de negocio se cumplen y el estado de los objetos es consistente.

### Cómo ejecutar los tests
Desde la raíz del proyecto:
```powershell
python -m unittest discover cine_multiplex/tests
```

### Clases Cubiertas
- **Pelicula** (y sus especializaciones): Se valida la creación, los metadatos y el cambio de estado en cartelera.
- **Sala**: Se valida la correcta inicialización y la representación textual.

## Reporte de Cobertura

La cobertura de código nos permite identificar qué partes de nuestro software están siendo validadas por las pruebas automáticas.

### Ejecución de Cobertura
```powershell
coverage run -m unittest discover cine_multiplex/tests
coverage report
```

### Resultados Obtenidos
| Módulo | Cobertura |
| :--- | :--- |
| `cine_multiplex/domain/pelicula.py` | 98% |
| `cine_multiplex/domain/sala.py` | 100% |
| **Media Total** | **~98%** |

---

## Cómo probar la aplicación a mano (Legacy)

Sigue estos pasos para comprobar que todo funciona correctamente:

1. **Preparar datos:** Asegúrate de que el archivo `main.py` está cargando datos de prueba (los que están en `datos_iniciales.py`).
2. **Chequeo inicial:** Ejecuta el programa y en el menú elige la opción *3. Listar sesiones*. No debería aparecer ninguna todavía.
3. **Crear una sesión:** Elige la opción correspondiente para programar. Introduce como ID `S1`, como película `"Dune: Parte Dos"`, y elige la Sala `1`. 
4. **Probar los errores:** Intenta programar otra sesión exactamente igual (misma sala y misma hora). El programa no debería dejarte y debería mostrarte un mensaje de error por pantalla.
5. **Vender una entrada:** Elige la opción *4. (Vender)* y compra una entrada para la sesión `"S1"`, aplicando descuento de tarifa `"Estudiante"`.
6. **Anular una entrada:** Elige la opción *4. (Anular)* y escribe el ID de la entrada vendida. Debería liberar un asiento en la sesión.
7. **Ver las ganancias:** Ve a la opción *5. (Estadísticas)*. Debería mostrar que se han ganado **5.00$** o menos según la anulación y que el recuento de entradas vendidas refleja el historial actual.
