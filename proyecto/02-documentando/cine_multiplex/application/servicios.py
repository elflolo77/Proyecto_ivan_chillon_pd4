class ServicioCine:
    """Servicio principal del cine"""
    
    def __init__(self, lista_peliculas, lista_salas):
        """Inicializa el servicio con las colecciones base."""
        self._lista_peliculas = lista_peliculas
        self._lista_salas = lista_salas
    
    def listar_todas_las_peliculas(self):
        """Lista todas las películas disponibles"""
        return self._lista_peliculas
    
    def listar_todas_las_salas(self):
        """Lista todas las salas disponibles"""
        return self._lista_salas
    
    def buscar_pelicula_por_titulo(self, nombre_pelicula):
        """Busca una película por nombre"""
        for pelicula in self._lista_peliculas:
            if pelicula.titulo == nombre_pelicula:
                return pelicula
        return None
    
    def buscar_sala_por_numero(self, numero_sala):
        """buscar sala por número"""
        for sala in self._lista_salas:
            if sala.numero == numero_sala:
                return sala
        return None
    
    # FUNCIONALIDADES NO IMPLEMENTADAS
    
    def programar_nueva_sesion(self, identificador_pelicula, numero_sala, fecha_hora_sesion):
        """Crear sesión - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de sesiones no implementada")
    
    def procesar_venta_entrada(self, identificador_sesion, numero_butaca):
        """Vender entrada - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de venta de entradas no implementada")
    
    def generar_informe_de_ventas(self, fecha_inicio, fecha_fin):
        """Generar reporte - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de reportes no implementada")
    
    def realizar_reserva_butaca(self, identificador_sesion, numero_fila, numero_asiento):
        """Reservar butaca - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de reservas no implementada")
    
    def anular_sesion_programada(self, identificador_sesion):
        """Cancelar sesión - NO IMPLEMENTADO"""
        raise NotImplementedError("Funcionalidad de cancelación no implementada")
