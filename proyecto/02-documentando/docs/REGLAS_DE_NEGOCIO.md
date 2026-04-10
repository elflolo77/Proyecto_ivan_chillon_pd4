# REGLAS DE NEGOCIO

En un entorno arquitectónico por capas, las reglas que determinan qué se puede o no puede hacer dentro de la aplicación son protegidas tanto por los Servicios de Aplicación como por los Constructores del Dominio.

## Reglas de Dominio (Aplicables en `domain/`)
1. **Aforo y estado de sesión:**
   - Una `Sesion` no puede vender entradas si está cancelada.
   - Si no quedan asientos libres, la sesión pasa a estado `completa` y se rechaza la venta con el mensaje "La sesión está completa.".
   - La anulación libera un asiento siempre que haya al menos una entrada vendida.
2. **Ciclo de vida Sesión:**
   - Toda sesión comienza `programada`.
   - Si se llena, se actualiza a `completa`.
   - El estado `cancelada` bloquea nuevas ventas.

## Reglas de Aplicación (Aplicables en `application/servicio_cine.py`)
1. **Programación de sesiones (`programar_sesion`):**
   - Verifica que la película exista y que la sala exista.
   - Valida que la fecha y hora se reciba como cadena.
2. **Políticas de Precios (`vender_entrada`):**
   - Precio base: 10.0€.
   - "Estudiante": 50% de descuento.
   - "Reducida": 20% de descuento.
   - Cualquier otra categoría usa el precio base.
3. **Venta y anulación:**
   - La venta crea una `Entrada`, guarda el ticket y actualiza la sesión.
   - La anulación busca la entrada por su identificador, elimina el registro si existe y libera un asiento en la sesión relacionada.
