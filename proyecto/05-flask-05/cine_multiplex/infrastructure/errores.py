"""Excepciones de infraestructura para persistencia de datos."""

class ErrorPersistencia(Exception):
    """Clase base para todas las excepciones de persistencia."""
    pass

class EntidadNoEncontradaError(ErrorPersistencia):
    """Excepción lanzada cuando no se encuentra una entidad en la base de datos."""
    pass

class EntidadDuplicadaError(ErrorPersistencia):
    """Excepción lanzada cuando se intenta crear una entidad que ya existe."""
    pass

class ErrorIntegridadDatos(ErrorPersistencia):
    """Excepción lanzada cuando se viola una restricción de integridad (ej. claves foráneas)."""
    pass
