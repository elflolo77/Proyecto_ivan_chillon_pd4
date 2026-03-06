import unittest
from expendedora.domain.item import Item, ItemConDescuento


class TestItem(unittest.TestCase):

    def test_codigo_normaliza_strip_y_upper(self):
        item = Item(" a1 ", "Agua", 1.5, 10)
        self.assertEqual(item.codigo, "A1")

    def test_codigo_invalido_por_formato_lanza_valueerror(self):
        with self.assertRaises(ValueError):
            Item("A", "Agua", 1.5, 10)    # demasiado corto

        with self.assertRaises(ValueError):
            Item("1A", "Agua", 1.5, 10)   # no empieza por letra

        with self.assertRaises(ValueError):
            Item("AA", "Agua", 1.5, 10)   # no hay número tras la letra

        with self.assertRaises(ValueError):
            Item("A*", "Agua", 1.5, 10)   # parte numérica no es dígito

    def test_nombre_vacio_lanza_valueerror(self):
        with self.assertRaises(ValueError):
            Item("A1", "", 1.5, 10)

        with self.assertRaises(ValueError):
            Item("A1", "   ", 1.5, 10)

    def test_nombre_con_espacios_laterales_lanza_valueerror(self):
        with self.assertRaises(ValueError):
            Item("A1", " Agua", 1.5, 10)

        with self.assertRaises(ValueError):
            Item("A1", "Agua ", 1.5, 10)

    def test_precio_string_numerico_se_convierte_a_float(self):
        item = Item("A1", "Agua", "2.00", 10)
        self.assertEqual(item.precio, 2.0)
        self.assertIsInstance(item.precio, float)

    def test_precio_no_valido_lanza_valueerror(self):
        with self.assertRaises(ValueError):
            Item("A1", "Agua", 0, 10)

        with self.assertRaises(ValueError):
            Item("A1", "Agua", -1, 10)

        with self.assertRaises(ValueError):
            Item("A1", "Agua", "no-numero", 10)

        with self.assertRaises(ValueError):
            Item("A1", "Agua", None, 10)

    def test_cantidad_debe_ser_entero_y_no_negativa(self):
        # válidos
        item0 = Item("A1", "Agua", 1.0, 0)
        self.assertEqual(item0.cantidad, 0)

        item10 = Item("A1", "Agua", 1.0, 10)
        self.assertEqual(item10.cantidad, 10)

        # inválidos
        with self.assertRaises(ValueError):
            Item("A1", "Agua", 1.0, -1)

        with self.assertRaises(ValueError):
            Item("A1", "Agua", 1.0, 2.5)

        with self.assertRaises(ValueError):
            Item("A1", "Agua", 1.0, "10")

    def test_precio_final_devuelve_precio_base(self):
        item = Item("A1", "Agua", 2.0, 10)
        self.assertEqual(item.precio_final(), 2.0)

    def test_mostrar_producto_devuelve_tupla_esperada(self):
        item = Item("A1", "Agua", 2.0, 10)
        esperado = ("A1", "Agua", 2.0, 2.0, 10, 0.0)
        self.assertEqual(item.mostrar_producto(), esperado)

    def test_valores_limite(self):
        item = Item("A1", "Agua con gas", 0.01, 0)
        self.assertEqual(item.precio, 0.01)
        self.assertEqual(item.cantidad, 0)
        self.assertEqual(item.nombre, "Agua con gas")

class TestItemConDescuento(unittest.TestCase):

    def test_creacion_y_descuento_valido(self):
        item = ItemConDescuento("A1", "Teclado", 100, 2, 10)
        self.assertEqual(item.porcentaje_descuento, 10.0)

    def test_precio_final_con_descuento(self):
        item = ItemConDescuento("A1", "Teclado", 100, 2, 10)
        self.assertAlmostEqual(item.precio_final(), 90.0)

    def test_precio_final_sin_descuento(self):
        item = ItemConDescuento("A1", "Teclado", 100, 2, 0)
        self.assertAlmostEqual(item.precio_final(), 100.0)

    def test_precio_final_descuento_total(self):
        item = ItemConDescuento("A1", "Teclado", 100, 2, 100)
        self.assertAlmostEqual(item.precio_final(), 0.0)

    def test_descuento_invalido_menor_que_0(self):
        with self.assertRaises(ValueError):
            ItemConDescuento("A1", "Teclado", 100, 2, -1)

    def test_descuento_invalido_mayor_que_100(self):
        with self.assertRaises(ValueError):
            ItemConDescuento("A1", "Teclado", 100, 2, 101)

    def test_descuento_invalido_no_numerico(self):
        with self.assertRaises(ValueError):
            ItemConDescuento("A1", "Teclado", 100, 2, "hola")

    def test_mostrar_producto_formato(self):
        item = ItemConDescuento("A1", "Teclado", 100, 2, 10)
        esperado = ("A1", "Teclado", 100, 90.0, 2, 10.0)
        self.assertEqual(item.mostrar_producto(), esperado)

if __name__ == "__main__":
    unittest.main()