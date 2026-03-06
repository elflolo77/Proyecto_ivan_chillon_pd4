"""Dominio: Entidad Sala."""

class Sala:
    """Representa una sala de proyección en el cine."""
    def __init__(self, numero: int, capacidad_maxima: int, tecnologia_pantalla: str = "2D"):
        """Inicializa una sala con capacidad y tecnología."""
        self._numero = numero
        self._capacidad_maxima = capacidad_maxima # Aforo máximo (int)
        self._tecnologia_pantalla = tecnologia_pantalla # Tecnología: 2D, 3D, IMAX...
    
    @property
    def numero(self) -> int:
        """Devuelve el número de sala."""
        return self._numero

    @property
    def capacidad_maxima(self) -> int:
        """Devuelve el aforo total."""
        return self._capacidad_maxima

    @property
    def tecnologia_pantalla(self) -> str:
        """Devuelve el tipo de tecnología de pantalla."""
        return self._tecnologia_pantalla

    def __str__(self) -> str:
        """Representación amigable de la sala."""
        return f"Sala {self.numero} ({self.capacidad_maxima} pax, {self.tecnologia_pantalla})"
