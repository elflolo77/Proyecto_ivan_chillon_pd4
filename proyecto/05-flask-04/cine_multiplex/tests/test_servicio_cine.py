import unittest
from cine_multiplex.application.servicio_cine import ServicioCine
from cine_multiplex.infrastructure.repositorio_memoria import RepositorioMemoria
from cine_multiplex.infrastructure.errores import EntidadDuplicadaError, EntidadNoEncontradaError

class TestServicioCine(unittest.TestCase):
    def setUp(self):
        """Prepara el servicio con un repositorio limpio en memoria para los tests."""
        self.repo = RepositorioMemoria()
        self.servicio = ServicioCine(self.repo)

    def test_excepcion_pelicula_duplicada(self):
        """Verifica que se lanza EntidadDuplicadaError al registrar una película ya existente."""
        self.servicio.registrar_pelicula_comercial("Matrix", 136, "12+", "Ciencia Ficción", "Warner Bros")
        
        with self.assertRaises(EntidadDuplicadaError):
            self.servicio.registrar_pelicula_comercial("Matrix", 136, "12+", "Ciencia Ficción", "Warner Bros")

    def test_excepcion_pelicula_no_encontrada_al_programar(self):
        """Verifica que se lanza EntidadNoEncontradaError si la película no existe al programar."""
        self.servicio.crear_sala(1, 100, "2D")
        
        with self.assertRaises(EntidadNoEncontradaError):
            self.servicio.programar_sesion("S1", "Película Falsa", 1, "2026-10-10 18:00")

if __name__ == "__main__":
    unittest.main()
