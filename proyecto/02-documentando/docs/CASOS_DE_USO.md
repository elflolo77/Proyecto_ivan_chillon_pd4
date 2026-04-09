# CASOS DE USO

En este documento se describen las diferentes operaciones que se pueden realizar al interactuar con la aplicación. Para cada caso se especifica: entrada, validaciones y salida.

Las opciones del menú principal (Consola) son:

1. Gestión de Películas
2. Gestión de Salas
3. Gestión de Sesiones
4. Venta de Entradas
5. Estadísticas
0. Salir

---

## 1. Gestión de Películas
Permite listar las películas registradas o registrar un estreno nuevo (Comercial, Infantil o Clásica).
- **Entrada:** Opción numérica (1-4). Título, duración, clasificación, género y atributos especiales.
- **Salida:** Listado de películas con formato polimórfico, o confirmación de la película registrada.
- **Validaciones:** Se exige duración en formato numérico entero.

## 2. Gestión de Salas
- **Entrada:** Opción 1 o 2. Para sala nueva: Número, capacidad (entero), tipo de tecnología.
- **Salida:** Listado de salas disponibles.
- **Errores (`ValueError`):** Almacenar campos no numéricos en la capacidad o identificador.

## 3. Gestión de Sesiones
- **Entrada:** Opción 1 o 2. Si programa sesión: ID sesión, Título exacto de la película, Número exacto de la sala, Fecha y Hora (String formato dictado).
- **Validaciones:**
    - Verifica existencia de la Película y la Sala en persistencia.
    - Evita colisiones lanzando una `Exception` si la sala ya está asignada en la misma `fecha_hora`.
- **Salida:** Listado de sesiones incluyendo detalle de Plazas libres. 

## 4. Venta de Entradas
Engloba operaciones de Venta directa y Anulación.
- **Venta de Entrada:**
  - **Precondición:** Existe la sesión.
  - **Entrada:** ID de sesión, y la cadena referenciando el tipo de Tarifa (General, Reducida, Estudiante).
  - **Efectos:** Reduce asientos libres de la sesión, genera un ID hash para ticket y registra el mismo en persistencia.
- **Anular Entrada:**
  - **Entrada:** Hash / UUID de la Entrada.
  - **Salida:** Devolución ("Entrada anulada" u error).
  - **Efectos:** Libera la sesión y destruye el registro de la venta en el repositorio.

## 5. Estadísticas
- **Salida:** Monto total facturado (`float`) y suma incremental del total de entradas vendidas a lo largo de este Runtime.
