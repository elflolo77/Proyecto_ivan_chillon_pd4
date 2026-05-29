import unittest
import json
from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica
from cine_multiplex.domain.sala import Sala
from cine_multiplex.domain.sesion import Sesion
from cine_multiplex.presentation.app import app, servicio, repositorio_cine
from cine_multiplex.infrastructure.errores import EntidadNoEncontradaError

class TestAPIAndSerialization(unittest.TestCase):
    def setUp(self):
        # Configure app for testing
        app.config['TESTING'] = True
        self.client = app.test_client()
        # Clean repository/database state (since we use a real db file for SQLite, we can clean it up or mock service calls,
        # but let's test serialization first and then check endpoints).
        
    def test_serialization(self):
        p = PeliculaComercial("Inception", 148, "12+", "Sci-Fi", "Warner Bros")
        p_dict = p.to_dict()
        self.assertEqual(p_dict["titulo"], "Inception")
        self.assertEqual(p_dict["distribuidora"], "Warner Bros")
        self.assertEqual(p_dict["tipo_pelicula"], "COMERCIAL")

        s = Sala(5, 120, "IMAX")
        s_dict = s.to_dict()
        self.assertEqual(s_dict["numero"], 5)
        self.assertEqual(s_dict["capacidad_maxima"], 120)
        self.assertEqual(s_dict["tecnologia_pantalla"], "IMAX")

        se = Sesion("S99", p, s, "2026-06-01 20:00")
        se_dict = se.to_dict()
        self.assertEqual(se_dict["id_sesion"], "S99")
        self.assertEqual(se_dict["pelicula"]["titulo"], "Inception")
        self.assertEqual(se_dict["sala"]["numero"], 5)

    def test_api_list_peliculas(self):
        response = self.client.get('/api/peliculas')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_api_detail_pelicula_not_found(self):
        response = self.client.get('/api/peliculas/PeliculaInexistenteQueNoExisteEnDB')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_api_list_sesiones(self):
        response = self.client.get('/api/sesiones')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_api_detail_sesion_not_found(self):
        response = self.client.get('/api/sesiones/SesionInexistenteQueNoExisteEnDB')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn("error", data)

if __name__ == "__main__":
    unittest.main()
