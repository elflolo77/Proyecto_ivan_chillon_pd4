import unittest
from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica

class TestPelicula(unittest.TestCase):
    def setUp(self):
        """Configuración de base para las pruebas."""
        self.pelicula_comercial = PeliculaComercial(
            "Inception", 148, "12+", "Ciencia Ficción", "Warner Bros"
        )
        self.pelicula_infantil = PeliculaInfantil(
            "Toy Story", 81, "TP", "Animación", 3
        )
        self.pelicula_clasica = PeliculaClasica(
            "Casablanca", 102, "TP", "Drama", 1942
        )

    def test_propiedades_basicas_comercial(self):
        """Verifica las propiedades públicas de una película comercial."""
        self.assertEqual(self.pelicula_comercial.titulo, "Inception")
        self.assertEqual(self.pelicula_comercial.duracion_minutos, 148)
        self.assertEqual(self.pelicula_comercial.clasificacion, "12+")
        self.assertEqual(self.pelicula_comercial.genero, "Ciencia Ficción")
        self.assertEqual(self.pelicula_comercial.distribuidora, "Warner Bros")

    def test_propiedades_basicas_infantil(self):
        """Verifica las propiedades públicas de una película infantil."""
        self.assertEqual(self.pelicula_infantil.titulo, "Toy Story")
        self.assertEqual(self.pelicula_infantil.edad_minima, 3)

    def test_propiedades_basicas_clasica(self):
        """Verifica las propiedades públicas de una película clásica."""
        self.assertEqual(self.pelicula_clasica.titulo, "Casablanca")
        self.assertEqual(self.pelicula_clasica.anio_lanzamiento, 1942)

    def test_esta_en_cartelera_setter(self):
        """Verifica el setter de esta_en_cartelera."""
        # Por defecto debe estar en cartelera
        self.assertTrue(self.pelicula_comercial.esta_en_cartelera)
        
        # Cambiamos el estado
        self.pelicula_comercial.esta_en_cartelera = False
        self.assertFalse(self.pelicula_comercial.esta_en_cartelera)

    def test_obtener_resumen_comercial(self):
        """Verifica el resumen de una película comercial."""
        resumen = self.pelicula_comercial.obtener_resumen_pelicula()
        self.assertIn("[COMERCIAL]", resumen)
        self.assertIn("Inception", resumen)
        self.assertIn("148 min", resumen)

    def test_obtener_resumen_infantil(self):
        """Verifica el resumen de una película infantil."""
        resumen = self.pelicula_infantil.obtener_resumen_pelicula()
        self.assertIn("[INFANTIL]", resumen)
        self.assertIn("Toy Story", resumen)
        self.assertIn("Min: 3 años", resumen)

    def test_obtener_resumen_clasica(self):
        """Verifica el resumen de una película clásica."""
        resumen = self.pelicula_clasica.obtener_resumen_pelicula()
        self.assertIn("[CLASICA]", resumen)
        self.assertIn("Casablanca", resumen)
        self.assertIn("Año: 1942", resumen)

if __name__ == "__main__":
    unittest.main()
