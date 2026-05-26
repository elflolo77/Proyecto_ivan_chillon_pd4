# MODELO DE DOMINIO

Contiene la conceptualización de los elementos tangibles dentro de nuestro software.

## Estructura principal de Entidades

1. **`Pelicula`**: Concepto matriz. Modela la pieza audiovisual a exhibir. 
   - Aislada por Polimorfismo en tres variantes de casuísticas diferentes: `PeliculaComercial` (`distribuidora`), `PeliculaInfantil` (`edad mínima`), `PeliculaClasica` (`año emisión original`).
2. **`Sala`**: Objeto de contención abstracto. Posee una magnitud finita de asientos integrados (`capacidad`) y restricciones visuales (`pantalla 2D, 3D, IMAX`).
3. **`Sesion`**: Engranaje puente entre el Tiempo y las entidades Físicas (`Películas + Salas`).
   - El estado de la sesión (`_estado_sesion` == `"programada" | "completa" | "cancelada"`) y el sumatorio incremental (`_numero_asientos_ocupados`) restringen de manera estricta el acceso masivo a su propiedad derivada: `numero_asientos_libres`.
4. **`Entrada`**: Contrato individual transferible entre el cine y un cliente que garantiza su puesto de acceso.
   - Cuenta con propiedades únicas como un hash único UUID, la matriz de costes (`tarifa` según edad), y el vínculo explícito al momento (`Sesion`).
