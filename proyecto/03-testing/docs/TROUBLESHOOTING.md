# TROUBLESHOOTING / PROBLEMAS COMUNES

Lista de situaciones anómalas que un usuario o estudiante en fase de prueba podría experimentar y sus causas conocidas.

---

### ValueError en inputs numéricos
- **Síntoma:** El programa arroja texto rojo como `invalid literal for int() with base 10`.
- **Causa/Solución:** Trataste de escribir texto (ej: "hola") en las opciones de "Duración", "Capacidad" de sala o en la Selección principal del Menú. Los bloques `try/except ValueError:` de la fase 01 capturaban esto correctamente en menús profundos, pero evalúa si te has salido a un menú global sin try/catch. Utiliza exclusivamente números.

### AttributeError con diccionarios de persistencia ("object has no attribute 'x'")
- **Síntoma:** El programa se cierra de forma severa al intentar `repositorio.peliculas[xxx]`.
- **Causa/Solución:** Tu versión actual del código está apuntando a variables de infraestructura privada sin respetar el patrón SOLID. Asegúrate (en especial tras el refactor) de usar _sólo el contrato_: `self._repositorio.obtener_pelicula(xxx)` en lugar del acceso abusivo a diccionarios.

### Sesión duplicada
- **Síntoma:** Aparece un mensaje de error al intentar programar una sesión en la misma sala y hora que otra ya existente.
- **Causa/Solución:** El sistema impide crear dos sesiones con la misma sala y fecha/hora exactas. Revisa los datos de sala y hora antes de volver a programar.
