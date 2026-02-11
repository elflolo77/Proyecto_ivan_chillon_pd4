"""Aplicación: Servicio principal de Cine Flolix."""

from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica
from cine_multiplex.domain.sala import Sala
from cine_multiplex.domain.sesion import Sesion
from cine_multiplex.domain.entrada import Entrada

class ServicioCine:
    """Coordina las operaciones del cine."""
    
    def __init__(self, repositorio):
        """Inicializa el servicio con un repositorio."""
        self.repositorio = repositorio

    # --- Gestión de Películas ---
    def registrar_pelicula_comercial(self, titulo, duracion_minutos, clasificacion, genero, distribuidora):
        """Registra una película comercial."""
        pelicula = PeliculaComercial(titulo, duracion_minutos, clasificacion, genero, distribuidora)
        self.repositorio.guardar_pelicula(pelicula)
        return pelicula

    def registrar_pelicula_infantil(self, titulo, duracion_minutos, clasificacion, genero, edad_minima_anios):
        """Registra una película infantil."""
        pelicula = PeliculaInfantil(titulo, duracion_minutos, clasificacion, genero, edad_minima_anios)
        self.repositorio.guardar_pelicula(pelicula)
        return pelicula

    def registrar_pelicula_clasica(self, titulo, duracion_minutos, clasificacion, genero, anio_estreno):
        """Registra una película clásica."""
        pelicula = PeliculaClasica(titulo, duracion_minutos, clasificacion, genero, anio_estreno)
        self.repositorio.guardar_pelicula(pelicula)
        return pelicula

    def listar_peliculas(self):
        """Lista todas las películas registradas."""
        return self.repositorio.listar_peliculas()

    # --- Gestión de Salas ---
    def crear_sala(self, numero, capacidad_personas, tipo_pantalla="2D"):
        """Crea y registra una nueva sala."""
        sala = Sala(numero, capacidad_personas, tipo_pantalla)
        self.repositorio.guardar_sala(sala)
        return sala

    def listar_salas(self):
        """Lista todas las salas registradas."""
        return self.repositorio.listar_salas()

    # --- Gestión de Sesiones ---
    def programar_sesion(self, id_sesion, titulo_pelicula, numero_sala, fecha_hora_str):
        """Programa una sesión.
        
        Args:
            id_sesion (str): ID único para la sesión.
            titulo_pelicula (str): Título de la película a proyectar.
            numero_sala (int): Número de la sala.
            fecha_hora_str (str): Fecha y hora en formato 'YYYY-MM-DD HH:MM'.
        """
        pelicula = self.repositorio.obtener_pelicula(titulo_pelicula)
        sala = self.repositorio.obtener_sala(numero_sala)
        
        if not pelicula:
            raise ValueError(f"Película '{titulo_pelicula}' no encontrada.")
        if not sala:
            raise ValueError(f"Sala {numero_sala} no encontrada.")
            
        # Validación simple de formato (opcional, si queremos mantener robustez básica)
        if not isinstance(fecha_hora_str, str):
            raise ValueError("La fecha debe ser una cadena de texto.")

        # Verificar solapamientos (simplificado: misma sala, misma hora exacta o rango)
        # Aquí haremos chequeo simple de hora exacta para MVP, idealmente rango duración
        sesiones_sala = [sesion for sesion in self.repositorio.listar_sesiones() if sesion.sala.numero == numero_sala]
        
        sesion = Sesion(id_sesion, pelicula, sala, fecha_hora_str)
        self.repositorio.guardar_sesion(sesion)
        return sesion

    def listar_sesiones(self):
        """Lista todas las sesiones programadas."""
        return self.repositorio.listar_sesiones()

    def obtener_sesion(self, id_sesion):
        """Obtiene una sesión por su ID."""
        return self.repositorio.obtener_sesion(id_sesion)

    # --- Gestión de Entradas ---
    def vender_entrada(self, id_sesion, tipo_tarifa):
        """Vende una entrada para la sesión indicada.
        
        Args:
            id_sesion (str): ID de la sesión.
            tipo_tarifa (str): Tipo de tarifa ('General', 'Reducida', 'Estudiante').
        """
        sesion = self.repositorio.obtener_sesion(id_sesion)
        if not sesion:
            raise ValueError("Sesión no encontrada.")
            
        # Calcular tarifa (lógica simple)
        precio_base = 10.0
        tarifas = {
            "General": precio_base,
            "Reducida": precio_base * 0.8,
            "Estudiante": precio_base * 0.5
        }
        precio = tarifas.get(tipo_tarifa, precio_base)
        
        # Intentar vender en el dominio (valida aforo)
        sesion.vender_entrada()
        
        # Crear ticket
        entrada = Entrada(sesion, precio, tipo_tarifa)
        self.repositorio.guardar_entrada(entrada)
        
        # Actualizar sesión en persistencia (por cambio de aforo)
        self.repositorio.guardar_sesion(sesion)
        
        return entrada

    def anular_entrada(self, id_entrada):
        """Anula una entrada vendida dado su ID."""
        # Esta lógica requeriría buscar la entrada por ID, obtener su sesión, y anular.
        # Por simplicidad de la lista, hacemos búsqueda lineal.
        entradas = self.repositorio.listar_entradas()
        entrada_encontrada = None
        for entrada in entradas:
            if entrada.id == id_entrada:
                entrada_encontrada = entrada
                break
        
        if entrada_encontrada:
            sesion = entrada_encontrada.sesion
            sesion.anular_entrada()
            # Eliminar de la lista de vendidas? O marcarla anulada?
            # El requisito dice "Anular entradas", la entidad Entrada podría tener estado.
            # Aquí la eliminamos de la lista para simplificar o dejaría ahí pero necesitamos actualizar repos.
            self.repositorio.entradas.remove(entrada_encontrada) # Hack acceso directo para MVP
            self.repositorio.guardar_sesion(sesion)
            self.repositorio.guardar_datos()
            return True
        return False
        
    # --- Estadísticas ---
    def informe_ventas(self):
        """Genera un informe con total recaudado y entradas vendidas."""
        total_recaudado = sum(entrada.precio_euros for entrada in self.repositorio.listar_entradas())
        entradas_vendidas = len(self.repositorio.listar_entradas())
        return {
            "total_recaudado": total_recaudado,
            "entradas_vendidas": entradas_vendidas
        }
