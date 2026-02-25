"""Punto de entrada: Cine Flolix."""

from cine_multiplex.infrastructure.datos_iniciales import inicializar_repositorio
from cine_multiplex.application.servicio_cine import ServicioCine
from cine_multiplex.presentation.menu import MenuCine

def main():
    # Inicializar dependencias con datos de prueba
    repo = inicializar_repositorio()
    
    servicio = ServicioCine(repo)
    menu = MenuCine(servicio)
    
    # Ejecutar aplicación
    menu.ejecutar()

if __name__ == "__main__":
    main()
