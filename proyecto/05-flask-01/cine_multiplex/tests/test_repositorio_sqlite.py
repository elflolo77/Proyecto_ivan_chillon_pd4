import unittest
import sqlite3
import os
from cine_multiplex.infrastructure.repositorio_sqlite import RepositorioSQLite
from cine_multiplex.domain.sala import Sala
from cine_multiplex.infrastructure.errores import ErrorPersistencia, EntidadDuplicadaError

class TestRepositorioSQLite(unittest.TestCase):
    def setUp(self):
        """Configuración antes de cada test. Usamos una base de datos temporal."""
        self.ruta_bd_test = "test_cine.db"
        if os.path.exists(self.ruta_bd_test):
            try:
                os.remove(self.ruta_bd_test)
            except PermissionError:
                pass
        # Crear esquema básico
        conn = sqlite3.connect(self.ruta_bd_test)
        cursor = conn.cursor()
        cursor.executescript("""
            CREATE TABLE salas (
                numero INTEGER PRIMARY KEY,
                capacidad_maxima INTEGER NOT NULL,
                tecnologia_pantalla TEXT NOT NULL
            );
        """)
        conn.commit()
        conn.close()
        
        self.repo = RepositorioSQLite(self.ruta_bd_test)

    def tearDown(self):
        """Limpieza después de cada test."""
        if os.path.exists(self.ruta_bd_test):
            os.remove(self.ruta_bd_test)

    def test_guardar_y_obtener_sala(self):
        """Prueba que se puede guardar una sala y luego recuperarla."""
        sala = Sala(1, 100, "2D")
        self.repo.guardar_sala(sala)
        
        sala_recuperada = self.repo.obtener_sala_por_numero(1)
        self.assertIsNotNone(sala_recuperada)
        self.assertEqual(sala_recuperada.numero, 1)
        self.assertEqual(sala_recuperada.capacidad_maxima, 100)
        self.assertEqual(sala_recuperada.tecnologia_pantalla, "2D")

    def test_actualizar_sala_existente(self):
        """Prueba que al guardar una sala con el mismo número, se actualiza en lugar de duplicarse."""
        sala_original = Sala(2, 50, "3D")
        self.repo.guardar_sala(sala_original)
        
        sala_modificada = Sala(2, 80, "IMAX")
        self.repo.guardar_sala(sala_modificada)
        
        sala_recuperada = self.repo.obtener_sala_por_numero(2)
        self.assertEqual(sala_recuperada.capacidad_maxima, 80)
        self.assertEqual(sala_recuperada.tecnologia_pantalla, "IMAX")

    def test_listar_salas(self):
        """Prueba listar todas las salas guardadas."""
        self.repo.guardar_sala(Sala(1, 100, "2D"))
        self.repo.guardar_sala(Sala(2, 50, "3D"))
        
        salas = self.repo.listar_todas_las_salas()
        self.assertEqual(len(salas), 2)

    def test_error_operacional_bd(self):
        """Prueba que un error de SQLite se traduce en ErrorPersistencia."""
        # Forzar error apuntando a un directorio o base de datos corrupta
        repo_invalido = RepositorioSQLite("/ruta/invalida/que/no/existe.db")
        with self.assertRaises(ErrorPersistencia):
            repo_invalido.listar_todas_las_salas()

if __name__ == "__main__":
    unittest.main()
