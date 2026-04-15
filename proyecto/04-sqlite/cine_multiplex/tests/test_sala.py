import unittest
from cine_multiplex.domain.sala import Sala

class TestSala(unittest.TestCase):
    def test_creacion_sala_por_defecto(self):
        """Verifica la creación de una sala con valores por defecto."""
        sala = Sala(1, 100)
        self.assertEqual(sala.numero, 1)
        self.assertEqual(sala.capacidad_maxima, 100)
        self.assertEqual(sala.tecnologia_pantalla, "2D")

    def test_creacion_sala_personalizada(self):
        """Verifica la creación de una sala con tecnología específica."""
        sala = Sala(5, 50, "IMAX 3D")
        self.assertEqual(sala.numero, 5)
        self.assertEqual(sala.capacidad_maxima, 50)
        self.assertEqual(sala.tecnologia_pantalla, "IMAX 3D")

    def test_representacion_str(self):
        """Verifica el método __str__ de la sala."""
        sala = Sala(3, 120, "Atmos")
        esperado = "Sala 3 (120 pax, Atmos)"
        self.assertEqual(str(sala), esperado)

if __name__ == "__main__":
    unittest.main()
