"""Aplicación: Servicio principal de Cine Flolix."""

from cine_multiplex.domain.pelicula import PeliculaComercial, PeliculaInfantil, PeliculaClasica
from cine_multiplex.domain.sala import Sala
from cine_multiplex.domain.sesion import Sesion
from cine_multiplex.domain.entrada import Entrada

class ServicioCine:
    """Coordina las operaciones del cine."""
    
    def __init__(self, repositorio):
        self.repo = repositorio

    # --- Gestión de Películas ---
    def registrar_pelicula_comercial(self, titulo, duracion, clasificacion, genero, distribuidora):
        pelicula = PeliculaComercial(titulo, duracion, clasificacion, genero, distribuidora)
        self.repo.guardar_pelicula(pelicula)
        return pelicula

    def registrar_pelicula_infantil(self, titulo, duracion, clasificacion, genero, edad_minima):
        pelicula = PeliculaInfantil(titulo, duracion, clasificacion, genero, edad_minima)
        self.repo.guardar_pelicula(pelicula)
        return pelicula

    def registrar_pelicula_clasica(self, titulo, duracion, clasificacion, genero, anio_estreno):
        pelicula = PeliculaClasica(titulo, duracion, clasificacion, genero, anio_estreno)
        self.repo.guardar_pelicula(pelicula)
        return pelicula

    def listar_peliculas(self):
        return self.repo.listar_peliculas()

    # --- Gestión de Salas ---
    def crear_sala(self, numero, capacidad, tipo_pantalla="2D"):
        sala = Sala(numero, capacidad, tipo_pantalla)
        self.repo.guardar_sala(sala)
        return sala

    def listar_salas(self):
        return self.repo.listar_salas()

    # --- Gestión de Sesiones ---
    def programar_sesion(self, id_sesion, titulo_pelicula, numero_sala, fecha_hora_str):
        """Programa una sesión. fecha_hora_str formato: 'YYYY-MM-DD HH:MM'"""
        pelicula = self.repo.obtener_pelicula(titulo_pelicula)
        sala = self.repo.obtener_sala(numero_sala)
        
        if not pelicula:
            raise ValueError(f"Película '{titulo_pelicula}' no encontrada.")
        if not sala:
            raise ValueError(f"Sala {numero_sala} no encontrada.")
            
        # Validación simple de formato (opcional, si queremos mantener robustez básica)
        if not isinstance(fecha_hora_str, str):
            raise ValueError("La fecha debe ser una cadena de texto.")

        # Verificar solapamientos (simplificado: misma sala, misma hora exacta o rango)
        # Aquí haremos chequeo simple de hora exacta para MVP, idealmente rango duración
        sesiones_sala = [s for s in self.repo.listar_sesiones() if s.sala.numero == numero_sala]
        
        for s in sesiones_sala:
            if s.fecha_hora == fecha_hora_str:
                raise ValueError(f"Ya existe una sesión en la sala {numero_sala} a las {fecha_hora_str}.")
        
        sesion = Sesion(id_sesion, pelicula, sala, fecha_hora_str)
        self.repo.guardar_sesion(sesion)
        return sesion

    def listar_sesiones(self):
        return self.repo.listar_sesiones()

    def obtener_sesion(self, id_sesion):
        return self.repo.obtener_sesion(id_sesion)

    # --- Gestión de Entradas ---
    def vender_entrada(self, id_sesion, tipo_tarifa):
        """Vende una entrada para la sesión indicada."""
        sesion = self.repo.obtener_sesion(id_sesion)
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
        self.repo.guardar_entrada(entrada)
        
        # Actualizar sesión en persistencia (por cambio de aforo)
        self.repo.guardar_sesion(sesion)
        
        return entrada

    def anular_entrada(self, id_entrada):
        # Esta lógica requeriría buscar la entrada por ID, obtener su sesión, y anular.
        # Por simplicidad de la lista, hacemos búsqueda lineal.
        entradas = self.repo.listar_entradas()
        entrada_encontrada = None
        for e in entradas:
            if e.id == id_entrada:
                entrada_encontrada = e
                break
        
        if entrada_encontrada:
            sesion = entrada_encontrada.sesion
            sesion.anular_entrada()
            # Eliminar via repositorio
            self.repo.eliminar_entrada(entrada_encontrada.id)
            self.repo.guardar_sesion(sesion)
            return True
        return False
        
    # --- Estadísticas ---
    def informe_ventas(self):
        total_recaudado = sum(e.tarifa for e in self.repo.listar_entradas())
        entradas_vendidas = len(self.repo.listar_entradas())
        return {
            "total_recaudado": total_recaudado,
            "entradas_vendidas": entradas_vendidas
        }
