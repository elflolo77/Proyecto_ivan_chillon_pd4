"""Dominio: Entidades de película."""

class Pelicula:
    """Clase base para representar una película."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero):
        """Inicializa una película y valida su estado."""
        self._titulo = titulo
        self._duracion_minutos = duracion_minutos
        self._clasificacion = clasificacion
        self._genero = genero
        self._esta_en_cartelera = True

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
    def esta_en_cartelera(self):
        """Indica si la película está en cartelera."""
        return self._esta_en_cartelera

    @esta_en_cartelera.setter
    def esta_en_cartelera(self, nuevo_estado_cartelera):
        """Actualiza el estado de disponibilidad."""
        self._esta_en_cartelera = nuevo_estado_cartelera

    def obtener_resumen_pelicula(self):
        """Devuelve resumen textual (implementar en subclases)."""
        raise NotImplementedError

class PeliculaComercial(Pelicula):
    """Película de gran difusión comercial."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero, distribuidora):
        """Inicializa con distribuidora."""
        super().__init__(titulo, duracion_minutos, clasificacion, genero)
        self.distribuidora = distribuidora

    def obtener_resumen_pelicula(self):
        """Resumen especializado para películas comerciales."""
        return f"[COMERCIAL] {self.titulo} ({self.duracion_minutos} min) - {self.genero}"

class PeliculaInfantil(Pelicula):
    """Película orientada al público infantil."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero, edad_minima):
        """Inicializa con edad mínima recomendada."""
        super().__init__(titulo, duracion_minutos, clasificacion, genero)
        self.edad_minima = edad_minima

    def obtener_resumen_pelicula(self):
        """Resumen especializado para películas infantiles."""
        return f"[INFANTIL] {self.titulo} (Min: {self.edad_minima} años) - {self.genero}"

class PeliculaClasica(Pelicula):
    """Película considerada un clásico o reestreno."""
    def __init__(self, titulo, duracion_minutos, clasificacion, genero, anio_lanzamiento):
        """Inicializa con año de estreno original."""
        super().__init__(titulo, duracion_minutos, clasificacion, genero)
        self.anio_lanzamiento = anio_lanzamiento

    def obtener_resumen_pelicula(self):
        """Resumen especializado para películas clásicas."""
        return f"[CLASICA] {self.titulo} (Año: {self.anio_lanzamiento}) - {self.genero}"
