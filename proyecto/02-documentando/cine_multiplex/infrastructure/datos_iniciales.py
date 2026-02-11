"""Infraestructura: Datos iniciales del sistema."""

from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica
from cine_multiplex.domain.sala import Sala
from cine_multiplex.infrastructure.repositorio_memoria import RepositorioMemoria

def inicializar_repositorio():
    """Crea y devuelve un repositorio con datos precargados."""
    repo = RepositorioMemoria()
    
    # Peliculas
    pelicula_dune = PeliculaComercial("Dune: Parte Dos", 166, "PG-13", "Ciencia Ficción", "Warner Bros")
    pelicula_kungfu = PeliculaInfantil("Kung Fu Panda 4", 94, "PG", "Animación", 5)
    pelicula_padrino = PeliculaClasica("El Padrino", 175, "R", "Crimen", 1972)
    
    repo.guardar_pelicula(pelicula_dune)
    repo.guardar_pelicula(pelicula_kungfu)
    repo.guardar_pelicula(pelicula_padrino)
    
    # Salas
    sala_principal = Sala(1, 100, "2D")
    sala_3d = Sala(2, 50, "3D")
    sala_imax = Sala(3, 30, "IMAX")
    
    repo.guardar_sala(sala_principal)
    repo.guardar_sala(sala_3d)
    repo.guardar_sala(sala_imax)
    
    return repo
