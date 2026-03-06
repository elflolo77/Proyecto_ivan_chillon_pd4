"""Dominio: Entidad Sala."""

class Sala:
    """Representa una sala de cine."""
    def __init__(self, numero, capacidad_maxima, tecnologia_pantalla="2D"):
        self._numero = numero
        self._capacidad_maxima = capacidad_maxima
        self._tecnologia_pantalla = tecnologia_pantalla
    
    @property
    def numero(self):
        return self._numero

    @property
    def capacidad_maxima(self):
        return self._capacidad_maxima

    @property
    def tecnologia_pantalla(self):
        return self._tecnologia_pantalla

    def __str__(self):
        return f"Sala {self.numero} ({self.capacidad_maxima} pax, {self.tecnologia_pantalla})"
