"""Dominio: Entidad Sala."""

class Sala:
    """Representa una sala de cine."""
    def __init__(self, numero, capacidad_personas, tipo_pantalla="2D"):
        self._numero = numero
        self._capacidad_personas = capacidad_personas
        self._tipo_pantalla = tipo_pantalla
    
    @property
    def numero(self):
        return self._numero

    @property
    def capacidad_personas(self):
        return self._capacidad_personas

    @property
    def tipo_pantalla(self):
        return self._tipo_pantalla

    def __str__(self):
        return f"Sala {self.numero} ({self.capacidad_personas} pax, {self.tipo_pantalla})"
