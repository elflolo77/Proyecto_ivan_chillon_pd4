# Casos de uso

las opciones del menu son:

1. Mostrar productos
2. Seleccionar producto
3. Insertar dinero
4. Comprar
5. Cancelar
6. Reponer
7. Agregar producto
8. Agregar producto con descuento
9. Salir

## 1. Mostrar productos
- Entrada: ninguna.
- Salida: listado (codigo, nombre, precio base, precio final, stock, porcentaje descuento).
  - Nota: si `porcentaje descuento` es 0, entonces `precio final` == `precio base`.

## 2. Seleccionar producto
- Entrada: codigo.
- Validaciones: codigo existe.
- Salida: producto seleccionado.

## 3. Insertar dinero
- Entrada: cantidad > 0.
- Salida: saldo actualizado.

## 4. Comprar
- Precondicion: producto seleccionado, stock disponible, saldo suficiente.
- Salida: cambio (saldo - precio).
- Efectos: reduce stock, puede eliminar producto si stock llega a 0.

## 5. Cancelar
- Salida: devuelve saldo y reinicia seleccion.

## 6. Reponer
- Entrada: codigo existente, unidades >= 0.
- Efecto: aumenta stock.

## 7. Agregar producto
- Entrada: codigo, nombre, precio, cantidad.
- Validaciones: codigo unico, precio > 0, cantidad entero >= 0.

## 8. Agregar producto con descuento
- Entrada: codigo, nombre, precio, cantidad, porcentaje.
- Validaciones: codigo unico, precio > 0, cantidad entero >= 0, 0 <= descuento <= 100.

## 9. Salir
- Termina el programa.

## Errores representativos 

- `ValueError`: codigo inexistente, cantidad no valida, saldo insuficiente.
