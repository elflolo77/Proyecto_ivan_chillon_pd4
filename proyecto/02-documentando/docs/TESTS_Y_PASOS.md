# PRUEBAS Y SIGUIENTES PASOS

## Cómo probar la aplicación a mano

Sigue estos pasos para comprobar que todo funciona correctamente:

1. **Preparar datos:** Asegúrate de que el archivo `main.py` está cargando datos de prueba (los que están en `datos_iniciales.py`).
2. **Chequeo inicial:** Ejecuta el programa y en el menú elige la opción *3. Listar sesiones*. No debería aparecer ninguna todavía.
3. **Crear una sesión:** Elige la opción correspondiente para programar. Introduce como ID `S1`, como película `"Dune: Parte Dos"`, y elige la Sala `1`. 
4. **Probar los errores:** Intenta programar otra sesión exactamente igual (misma sala y misma hora). El programa no debería dejarte y debería mostrarte un mensaje de error por pantalla.
5. **Vender una entrada:** Elige la opción *4. (Vender)* y compra una entrada para la sesión `"S1"`, aplicando descuento de tarifa `"Estudiante"`.
6. **Ver las ganancias:** Ve a la opción *5. (Estadísticas)*. Debería mostrar que se han ganado **5.00$** y que hay "1 Entrada vendida".

## Lo que haremos en la próxima iteración (Fase 03)

En el próximo paso del proyecto, dejaremos de hacer todos estos pasos de prueba a mano. Programaremos pruebas automáticas (usando la herramienta `unittest` de Python) que se encargarán de hacer todo esto por nosotros en segundos.
