class ServicioCine:
    """Servicio principal del cine"""
    
    def __init__(self, peliculas, salas):
        self._peliculas = peliculas
        self._salas = salas
    
    def listar_peliculas(self):
        """Lista todas las películas disponibles"""
        return self._peliculas
    
    def listar_salas(self):
        """Lista todas las salas disponibles"""
        return self._salas
    
    def buscar_pelicula(self, codigo):
        """Busca una película por código"""
        for pelicula in self._peliculas:
            if pelicula.codigo() == codigo:
                return pelicula
        return None
    
    def buscar_sala(self, numero):
        """buscar sala por número"""
        for sala in self._salas:
            if sala.numero() == numero:
                return sala
        return None
    
    # FUNCIONALIDADES NO IMPLEMENTADAS
    
    def crear_sesion(self, codigo_pelicula, numero_sala, horario):
        """Crear sesión - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de sesiones no implementada")
    
    def vender_entrada(self, sesion_id, butaca):
        """Vender entrada - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de venta de entradas no implementada")
    
    def generar_reporte(self, fecha_inicio, fecha_fin):
        """Generar reporte - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de reportes no implementada")
    
    def reservar_butaca(self, sesion_id, fila, asiento):
        """Reservar butaca - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de reservas no implementada")
    
    def cancelar_sesion(self, sesion_id):
        """Cancelar sesión - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de cancelación no implementada")
