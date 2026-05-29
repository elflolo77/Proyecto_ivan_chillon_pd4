"""Dominio: Entidad Sala."""

class Sala:
    """Representa una sala de proyección en el cine."""
    def __init__(self, numero, capacidad_maxima, tecnologia_pantalla="2D"):
        """Inicializa una sala con capacidad y tecnología."""
        self._numero = numero
        self._capacidad_maxima = capacidad_maxima
        self._tecnologia_pantalla = tecnologia_pantalla
    
    @property
    def numero(self):
        """Devuelve el número de sala."""
        return self._numero

    @property
    def capacidad_maxima(self):
        """Devuelve el aforo total."""
        return self._capacidad_maxima

    @property
    def tecnologia_pantalla(self):
        """Devuelve el tipo de tecnología de pantalla."""
        return self._tecnologia_pantalla

    def to_dict(self):
        """Devuelve una representación en diccionario de la sala."""
        return {
            "numero": self.numero,
            "capacidad_maxima": self.capacidad_maxima,
            "tecnologia_pantalla": self.tecnologia_pantalla
        }

    def __str__(self):
        """Representación amigable de la sala."""
        return f"Sala {self.numero} ({self.capacidad_maxima} pax, {self.tecnologia_pantalla})"
