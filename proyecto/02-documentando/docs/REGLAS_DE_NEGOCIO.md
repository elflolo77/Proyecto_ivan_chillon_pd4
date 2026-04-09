# REGLAS DE NEGOCIO

En un entorno arquitectónico por capas, las reglas que determinan qué se puede o no puede hacer dentro de la aplicación son protegidas tanto por los Servicios de Aplicación como por los Constructores del Dominio.

## Reglas de Dominio (Aplicables en `domain/`)
1. **Aforo Limitado:**
   - Una `Sesion` jamás puede vender entradas si su propiedad `capacidad_disponible` se equipara a cero (Trigger de State `completa`). Dispara excepción `"La sesión está completa."`.
   - Sólo se puede anular un estado si `_asientos_ocupados > 0`.
2. **Ciclo de vida Sesión:**
   - Toda sesión comienza `programada`. Si se clausura manualmente, pasa a estado temporalmente simulado de `"cancelada"`, lo cual arroja bloqueo en las compras posteriores.

## Reglas de Aplicación (Aplicables en `application/servicio_cine.py`)
1. **Solapamiento Temporal (`programar_sesion`):**
   - No pueden agendarse dos sesiones en idéntica Sala y exacta `fecha_hora`. 
   - *Nota de Sistema*: Actualmente solo se audita coincidencia por texto exacto (`2024-10-05 20:00` coincidente con `2024-10-05 20:00`). Para uso productivo mayor, el módulo datetime vigilará un _rango duración_ por película y bloqueos por limpieza post-créditos.
2. **Políticas de Precios (`vender_entrada`):**
   - Existe una constante de coste preestablecida (10.0€).
   - "Estudiante": Aporta descuento del 50%.
   - "Reducida": Aporta descuento del 20%.
   - "General" u otra no reconocida: Aporta el Base estricto.
3. **Referencias Cruzadas Únicas:**
   - La inserción de tickets demanda un chequeo de ID para encontrar la sesión a deducir en memoria RAM de `repositorio_datos` antes de procesar ventas o fallos.
