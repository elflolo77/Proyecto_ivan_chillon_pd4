"""Punto de entrada: Cine Flolix."""

from cineflolix.infrastructure.datos_iniciales import inicializar_repositorio
from cineflolix.application.servicio_cine import ServicioCine
from cineflolix.presentation.menu import MenuCine

def main():
    # Inicializar dependencias con datos de prueba
    repo = inicializar_repositorio()
    
    servicio = ServicioCine(repo)
    menu = MenuCine(servicio)
    
    # Ejecutar aplicación
    menu.ejecutar()

if __name__ == "__main__":
    main()
