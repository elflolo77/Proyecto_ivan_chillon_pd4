"""Dominio: Entidades de Película."""

class Pelicula:
    """Clase base para películas.
    
    Representa la información general de una película en el sistema.
    """
    def __init__(self, titulo, duracion_minutos, clasificacion, genero):
        """Inicializa una nueva película.
        
        Args:
            titulo (str): Título de la película.
            duracion_minutos (int): Duración en minutos.
            clasificacion (str): Clasificación por edad (ej. 'PG-13').
            genero (str): Género de la película.
        """
        self._titulo = titulo
        # Regla de negocio: La duración se almacena en minutos y debe ser positiva.
        self._duracion_minutos = duracion_minutos 
        self._clasificacion = clasificacion
        self._genero = genero
        # Regla de negocio: Por defecto, una película nueva entra en cartelera.
        self._en_cartelera = True

    @property
    def titulo(self):
        """Devuelve el título de la película."""
        return self._titulo

    @property
    def duracion_minutos(self):
        """Devuelve la duración en minutos."""
        return self._duracion_minutos

    @property
    def clasificacion(self):
        """Devuelve la clasificación por edades."""
        return self._clasificacion
    
    @property
    def genero(self):
        """Devuelve el género de la película."""
        return self._genero

    @property
    def en_cartelera(self):
        """Indica si la película está actualmente en cartelera."""
        return self._en_cartelera

    @en_cartelera.setter
    def en_cartelera(self, estado):
        """Actualiza el estado de cartelera."""
        self._en_cartelera = estado

    def mostrar_info(self):
        """Muestra información específica de la película."""
        raise NotImplementedError

class PeliculaComercial(Pelicula):
    """Estrenos y películas de gran difusión."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero, distribuidora):
        """Inicializa una película comercial.
        
        Args:
            distribuidora (str): Empresa distribuidora.
        """
        super().__init__(titulo, duracion_minutos, clasificacion, genero)
        self.distribuidora = distribuidora

    def mostrar_info(self):
        """Devuelve una descripción formateada de la película comercial."""
        return f"[COMERCIAL] {self.titulo} ({self.duracion_minutos} min) - {self.genero}"

class PeliculaInfantil(Pelicula):
    """Películas para público familiar e infantil."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero, edad_minima_anios):
        """Inicializa una película infantil.
        
        Args:
            edad_minima_anios (int): Edad mínima recomendada.
        """
        super().__init__(titulo, duracion_minutos, clasificacion, genero)
        self.edad_minima_anios = edad_minima_anios

    def mostrar_info(self):
        """Devuelve una descripción formateada de la película infantil."""
        return f"[INFANTIL] {self.titulo} (Min: {self.edad_minima_anios} años) - {self.genero}"

class PeliculaClasica(Pelicula):
    """Películas antiguas o reestrenos."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero, anio_estreno):
        """Inicializa una película clásica.
        
        Args:
            anio_estreno (int): Año original de estreno.
        """
        super().__init__(titulo, duracion_minutos, clasificacion, genero)
        self.anio_estreno = anio_estreno

    def mostrar_info(self):
        """Devuelve una descripción formateada de la película clásica."""
        return f"[CLASICA] {self.titulo} (Año: {self.anio_estreno}) - {self.genero}"
