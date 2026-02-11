"""Dominio: Entidades de Película."""

class Pelicula:
    """Clase base para películas."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero):
        self._titulo = titulo
        self._duracion_minutos = duracion_minutos # en minutos
        self._clasificacion = clasificacion
        self._genero = genero
        self._en_cartelera = True

    @property
    def titulo(self):
        return self._titulo

    @property
    def duracion_minutos(self):
        return self._duracion_minutos

    @property
    def clasificacion(self):
        return self._clasificacion
    
    @property
    def genero(self):
        return self._genero

    @property
    def en_cartelera(self):
        return self._en_cartelera

    @en_cartelera.setter
    def en_cartelera(self, estado):
        self._en_cartelera = estado

    def mostrar_info(self):
        """Muestra información específica de la película."""
        raise NotImplementedError

class PeliculaComercial(Pelicula):
    """Estrenos y películas de gran difusión."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero, distribuidora):
        super().__init__(titulo, duracion_minutos, clasificacion, genero)
        self.distribuidora = distribuidora

    def mostrar_info(self):
        return f"[COMERCIAL] {self.titulo} ({self.duracion_minutos} min) - {self.genero}"

class PeliculaInfantil(Pelicula):
    """Películas para público familiar e infantil."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero, edad_minima_anios):
        super().__init__(titulo, duracion_minutos, clasificacion, genero)
        self.edad_minima_anios = edad_minima_anios

    def mostrar_info(self):
        return f"[INFANTIL] {self.titulo} (Min: {self.edad_minima_anios} años) - {self.genero}"

class PeliculaClasica(Pelicula):
    """Películas antiguas o reestrenos."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero, anio_estreno):
        super().__init__(titulo, duracion_minutos, clasificacion, genero)
        self.anio_estreno = anio_estreno

    def mostrar_info(self):
        return f"[CLASICA] {self.titulo} (Año: {self.anio_estreno}) - {self.genero}"
