# Proyecto Cine Multiplex

Este proyecto es una aplicación de gestión para un cine multiplex, organizada siguiendo una arquitectura de diseño por capas (domain, application, infrastructure, presentation).

## Estructura del Proyecto

- `proyecto/`: Carpeta principal del proyecto.
  - `01-capas/`: Código correspondiente a la fase de diseño por capas.
    - `cine_multiplex/`: Paquete principal de la aplicación.
    - `main.py`: Punto de entrada de la aplicación.

## Instrucciones para ejecutar el proyecto.

### Fase 1

1. Accede a la carpeta del proyecto para la Fase 1:

```bash
cd proyecto/01-capas
```

2. Ejecuta la aplicación:

```bash
python main.py
```
o como módulo:
```bash
python -m cine_multiplex.main
```

## Checklists por fases del proyecto
<details>
  <summary>Fase 01 - diseño capas</summary>

- [x] Crear cuenta en Github/codeberg
- [x] Crear repositorio para alojar/enlazar materiales de clase
- [x] Compartir repositorio con el usuario del profesor (ichigar)
- [x] Instalar y configurar GIT en ordenador de clase y en ordenador de casa.
- [x] Crear claves ssh en ordenador de casa y en ordenador de clase. Añadir claves públicas a las cuentas de github/codeberg
- [x] Clonar repositorio en clase y en casa
- [x] Probar a hacer cambios en clase y en casa y aprender a mantener actualizados los cambios realizados (clase/casa/repositorio)
- [x] Crear subcarpeta `proyecto` en repositorio.
- [x] Incluir en `README.md` con las instrucciones para instalar y ejecutar el proyecto.
- [x] Crear en `proyecto` subcarpeta `01-capas` e incluir en la misma el código para dicha fase de tu proyecto
- [x] Los apartados de la interfaz que aparecen en el menú principal deben funcionar correctamente.
- [x] El proyecto está organizado en capas.
- [x] La estructura de archivos y carpetas siguen las pautas de módulos, paquetes y subpaquetes vistos hasta ahora en clase.
- [x] Se han aplicado los principios de POO vistos en clase.
- [x] Los nombres de ficheros, clases y variables son significativos y siguen los principios de la recomendación PEP8.

</details>

<details open>
  <summary>Fase 02 - documentando</summary>

- [ ] Copiado en subcarpeta `02-documentando` el contenido actual de la carpeta `01-diseno_capas` o se crea una nueva rama para la nueva etapa (antes crear la rama 01-diseno-capas).
- [ ] Renombrar todos los identificadores de modulos, clases, métodos y variables que no cumplan con los [criterios de los apuntes](https://ichigar.codeberg.page/pd4/ut1/recursos/poo_ut1_6_documentacion/#eligiendo-nombres)
- [ ] Añadir docstring a los módulos, clases y métodos públicos del proyecto siguiendo los [criterios de los apuntes](https://ichigar.codeberg.page/pd4/ut1/recursos/poo_ut1_6_documentacion/#eligiendo-nombres).
- [ ] Comentar las reglas de negocio de las clases del dominio.
- [ ] Comentar los bloques de código que no expresen claramente para qué se usan.
- [ ] Eliminar comentarios evidentes.
#### Usando como referencia los [documentos del proyecto model](https://codeberg.org/ichigar/cepy_pd4/src/branch/main/proyecto/02-documentando/expendedora) añadir los siguientes ficheros:
- [ ] README.md
- [ ] CHANGELOG.md
- [ ] `docs/README.md
- [ ] `docs/DESCRIPCION_Y_ALCANCE.md`
- [ ] `docs/EJECUCION.md`
- [ ] `docs/ARQUITECTURA_POR_CAPAS.md`
- [ ] `docs/CASOS_DE_USO.md`
- [ ] `docs/REGLAS_DE_NEGOCIO.md`
- [ ] `docs/MODELO_DE_DOMINIO.md`
- [ ] `docs/CONTRATO_REPOSITORIO.md`
- [ ] `docs/DATOS_INICIALES.md`
- [ ] `docs/TESTS_Y_PASOS.md`
- [ ] `docs/TROUBLESHOOTING.md`
</details>

## Aspectos a tener en cuenta durante el desarrollo del proyecto

- Hacer `pull` del repositorio para ver posibles comentarios del profesor o para descagar cambios hechos en otro equipo.
- Hacer commits periódicos cada vez que se complete una tarea mediante código.
- Hacer `push` después de cada commit
- Añadir al repositorio en subcarpeta las actividades completadas en clase
- Añadir en página en el repositorio enlace o copia de los materiales que va añadiendo el profesor.