"""Dominio: Entidad Sala."""

class Sala:
    """Representa una sala de cine."""
    def __init__(self, numero, capacidad_personas, tipo_pantalla="2D"):
        """Inicializa una sala.
        
        Args:
            numero (int): Número identificador de la sala.
            capacidad_personas (int): Aforo máximo de la sala.
            tipo_pantalla (str, optional): Tipo de proyección (default "2D").
        """
        self._numero = numero
        # Regla de negocio: La capacidad debe ser un entero positivo.
        self._capacidad_personas = capacidad_personas
        self._tipo_pantalla = tipo_pantalla
    
    @property
    def numero(self):
        """Devuelve el número de sala."""
        return self._numero

    @property
    def capacidad_personas(self):
        """Devuelve la capacidad máxima en personas."""
        return self._capacidad_personas

    @property
    def tipo_pantalla(self):
        """Devuelve el tipo de pantalla (ej. 2D, 3D)."""
        return self._tipo_pantalla

    def __str__(self):
        """Devuelve una representación en cadena de la sala."""
        return f"Sala {self.numero} ({self.capacidad_personas} pax, {self.tipo_pantalla})"
