"""Dominio: Entidades de Película."""

class Pelicula:
    """Clase base para películas."""
    def __init__(self, titulo, duracion, clasificacion, genero):
        self._titulo = titulo
        self._duracion = duracion # en minutos
        self._clasificacion = clasificacion
        self._genero = genero
        self._en_cartelera = True

    @property
    def titulo(self):
        return self._titulo

    @property
    def duracion(self):
        return self._duracion

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
    def __init__(self, titulo, duracion, clasificacion, genero, distribuidora):
        super().__init__(titulo, duracion, clasificacion, genero)
        self.distribuidora = distribuidora

    def mostrar_info(self):
        return f"[COMERCIAL] {self.titulo} ({self.duracion} min) - {self.genero}"

class PeliculaInfantil(Pelicula):
    """Películas para público familiar e infantil."""
    def __init__(self, titulo, duracion, clasificacion, genero, edad_minima):
        super().__init__(titulo, duracion, clasificacion, genero)
        self.edad_minima = edad_minima

    def mostrar_info(self):
        return f"[INFANTIL] {self.titulo} (Min: {self.edad_minima} años) - {self.genero}"

class PeliculaClasica(Pelicula):
    """Películas antiguas o reestrenos."""
    def __init__(self, titulo, duracion, clasificacion, genero, anio_estreno):
        super().__init__(titulo, duracion, clasificacion, genero)
        self.anio_estreno = anio_estreno

    def mostrar_info(self):
        return f"[CLASICA] {self.titulo} (Año: {self.anio_estreno}) - {self.genero}"
