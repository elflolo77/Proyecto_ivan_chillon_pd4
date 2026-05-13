"""Punto de entrada: Cine Flolix."""

from cine_multiplex.infrastructure.repositorio_sqlite import RepositorioSQLite
from cine_multiplex.application.servicio_cine import ServicioCine
from cine_multiplex.presentation.menu import MenuCine

def main():
    """Arranque de la aplicación y wiring de dependencias."""
    repositorio_cine = RepositorioSQLite("cine.db")
    
    servicio_cine = ServicioCine(repositorio_cine)
    interfaz_menu = MenuCine(servicio_cine)
    
    interfaz_menu.ejecutar()

if __name__ == "__main__":
    main()
