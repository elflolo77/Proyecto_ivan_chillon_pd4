"""Infraestructura: Datos iniciales del sistema."""

from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica
from cine_multiplex.domain.sala import Sala
from cine_multiplex.infrastructure.repositorio_memoria import RepositorioMemoria

def inicializar_repositorio():
    """Crea y devuelve un repositorio con datos precargados."""
    repo = RepositorioMemoria()
    
    # Peliculas
    p1 = PeliculaComercial("Dune: Parte Dos", 166, "PG-13", "Ciencia Ficción", "Warner Bros")
    p2 = PeliculaInfantil("Kung Fu Panda 4", 94, "PG", "Animación", 5)
    p3 = PeliculaClasica("El Padrino", 175, "R", "Crimen", 1972)
    
    repo.guardar_pelicula(p1)
    repo.guardar_pelicula(p2)
    repo.guardar_pelicula(p3)
    
    # Salas
    s1 = Sala(1, 100, "2D")
    s2 = Sala(2, 50, "3D")
    s3 = Sala(3, 30, "IMAX")
    
    repo.guardar_sala(s1)
    repo.guardar_sala(s2)
    repo.guardar_sala(s3)
    
    return repo
