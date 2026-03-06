"""Infraestructura: Datos iniciales del sistema."""

from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica
from cine_multiplex.domain.sala import Sala
from cine_multiplex.infrastructure.repositorio_memoria import RepositorioMemoria

def inicializar_repositorio():
    """Crea y devuelve un repositorio con datos precargados."""
    repositorio_cine = RepositorioMemoria()
    
    # Peliculas
    pelicula_1 = PeliculaComercial("Dune: Parte Dos", 166, "PG-13", "Ciencia Ficción", "Warner Bros")
    pelicula_2 = PeliculaInfantil("Kung Fu Panda 4", 94, "PG", "Animación", 5)
    pelicula_3 = PeliculaClasica("El Padrino", 175, "R", "Crimen", 1972)
    
    repositorio_cine.guardar_pelicula(pelicula_1)
    repositorio_cine.guardar_pelicula(pelicula_2)
    repositorio_cine.guardar_pelicula(pelicula_3)
    
    # Salas
    sala_1 = Sala(1, 100, "2D")
    sala_2 = Sala(2, 50, "3D")
    sala_3 = Sala(3, 30, "IMAX")
    
    repositorio_cine.guardar_sala(sala_1)
    repositorio_cine.guardar_sala(sala_2)
    repositorio_cine.guardar_sala(sala_3)
    
    return repositorio_cine
