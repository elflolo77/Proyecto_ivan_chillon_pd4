import unittest

from expendedora.domain.maquina import MaquinaExpendedora
from expendedora.infrastructure.datos_iniciales import crear_repositorio_con_datos

# Datos iniciales para pruebas
# Item("A1", "Agua", 1.00, 10)
# Item("A2", "Papas", 1.50, 8)
# ItemConDescuento("D1", "Refresco", 2.50, 5, 20)

class TestMaquinaExpendedoraConDatosIniciales(unittest.TestCase):

    def setUp(self):
        """preparador que se ejecuta antes de cada test"""
        self.repo = crear_repositorio_con_datos()
        self.maquina = MaquinaExpendedora(self.repo)

    def test_mostrar_productos_devuelve_catalogo(self):
        productos = self.maquina.mostrar_productos()
        # Comprobamos solo lo esencial: que están los códigos precargados
        codigos = [p[0] for p in productos]
        self.assertIn("A1", codigos)
        self.assertIn("A2", codigos)
        self.assertIn("D1", codigos)

    def test_seleccionar_codigo_inexistente_lanza_error(self):
        with self.assertRaises(ValueError):
            self.maquina.seleccionar("ZZ")

    def test_comprar_agua_devuelve_cambio_y_reduce_stock(self):
        # Agua A1 cuesta 1.00
        self.maquina.seleccionar("A1")
        self.maquina.insertar_dinero(2.00)
        cambio = self.maquina.comprar()

        self.assertEqual(cambio, 1.00)

        # Re-seleccionamos para comprobar stock actual (de 10 a 9)
        self.maquina.seleccionar("A1")
        item = self.maquina._obtener_seleccion()
        self.assertEqual(item.cantidad, 9)

    def test_comprar_refresco_con_descuento(self):
        # Refresco D1: base 2.50 con 20% => 2.00
        self.maquina.seleccionar("D1")
        self.maquina.insertar_dinero(2.00)
        cambio = self.maquina.comprar()

        self.assertEqual(cambio, 0.00)

    def test_comprar_saldo_insuficiente(self):
        self.maquina.seleccionar("A2")  # Papas 1.50
        self.maquina.insertar_dinero(1.00)
        with self.assertRaises(ValueError) as ctx:
            self.maquina.comprar()
        self.assertIn("Saldo insuficiente", str(ctx.exception))

    def test_reponer_suma_unidades(self):
        # A2 empieza con 8
        self.maquina.reponer("A2", 2)
        self.maquina.seleccionar("A2")
        item = self.maquina._obtener_seleccion()
        self.assertEqual(item.cantidad, 10)

    def test_cancelar_devuelve_saldo_y_limpia_estado(self):
        self.maquina.insertar_dinero(2.0)
        devuelto = self.maquina.cancelar()
        self.assertAlmostEqual(devuelto, 2.0)
        self.assertEqual(self.maquina.saldo, 0.0)
        with self.assertRaises(ValueError):
            self.maquina.comprar()  # no hay selección

    def test_insertar_dinero_acumula(self):
        self.maquina.insertar_dinero(1.0)
        self.maquina.insertar_dinero(0.5)
        self.assertAlmostEqual(self.maquina.saldo, 1.5)

    def test_comprar_resetea_saldo_y_seleccion(self):
        self.maquina.seleccionar("A1")
        self.maquina.insertar_dinero(2.0)
        self.maquina.comprar()
        self.assertEqual(self.maquina.saldo, 0.0)
        with self.assertRaises(ValueError):
            self.maquina.comprar()  # ya no hay selección

    def test_dos_compras_requieren_seleccionar_e_insertar_de_nuevo(self):
        # 1ª compra
        self.maquina.seleccionar("A1")
        self.maquina.insertar_dinero(1.0)
        self.maquina.comprar()

        # 2ª compra: si no seleccionas e insertas otra vez, debe fallar
        with self.assertRaises(ValueError):
            self.maquina.comprar()

        self.maquina.seleccionar("A1")
        self.maquina.insertar_dinero(1.0)
        self.maquina.comprar()  # ahora sí

    def test_mostrar_productos_no_esta_vacio(self):
        productos = self.maquina.mostrar_productos()
        self.assertGreaterEqual(len(productos), 3)

    def test_reponer_unidades_cero_no_cambia_stock(self):
        self.maquina.seleccionar("A2")
        item = self.maquina._obtener_seleccion()
        stock_antes = item.cantidad

        self.maquina.reponer("A2", 0)

        self.maquina.seleccionar("A2")
        item2 = self.maquina._obtener_seleccion()
        self.assertEqual(item2.cantidad, stock_antes)

    def test_reponer_codigo_inexistente_lanza_error(self):
        with self.assertRaises(ValueError):
            self.maquina.reponer("X9", 3)

    def test_compra_rebaja_stock_de_descuento(self):
        # D1: Refresco con descuento, stock inicial 5
        self.maquina.seleccionar("D1")
        item = self.maquina._obtener_seleccion()
        self.assertEqual(item.cantidad, 5)

        self.maquina.insertar_dinero(2.0)  # 2.50 con 20% => 2.00
        self.maquina.comprar()

        self.maquina.seleccionar("D1")
        item2 = self.maquina._obtener_seleccion()
        self.assertEqual(item2.cantidad, 4)


if __name__ == "__main__":
    unittest.main()
