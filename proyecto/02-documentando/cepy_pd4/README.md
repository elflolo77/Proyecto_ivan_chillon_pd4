# Proyecto modelo. Máquina expendedora de refrescos y snacks

## Instrucciones para ejecutar el proyecto.

### Fase 1

Clonar el repositorio:

```bash
git clone ssh://git@codeberg.org/ichigar/cepy_pd4.git
```

Accede a la carpeta padre en la que está el paquete del proyecto para la Fase 1

```bash
cd cepy_pd4/proyecto/01-diseno-capas
```

Ejecuta la aplicación

```
python -m expendedora.presentation.menu
```

## Checklists por fases del proyecto
<details>
  <summary>Fase 01 - diseño capas</summary>

- [ ] Crear cuenta en Github/codeberg
- [ ] Crear repositorio para alojar/enlazar materiales de clase
- [ ] Compartir repositorio con el usuario del profesor (ichigar)
- [ ] Instalar y configurar GIT en ordenador de clase y en ordenador de casa.
- [ ] Crear claves ssh en ordenador de casa y en ordenador de clase. Añadir claves públicas a las cuentas de github/codeberg
- [ ] Clonar repositorio en clase y en casa
- [ ] Probar a hacer cambios en clase y en casa y aprender a mantener actualizados los cambios realizados (clase/casa/repositorio)
- [ ] Crear subcarpeta `proyecto` en repositorio.
- [ ] Incluir en `README.md` con las instrucciones para instalar y ejecutar el proyecto.
- [ ] Crear en `proyecto` subcarpeta `01-capas` e incluir en la misma el código para dicha fase de tu proyecto
- [ ] Los apartados de la interfaz que aparecen en el menú principal deben funcionar correctamente.
- [ ] El proyecto está organizado en capas.
- [ ] La estructura de archivos y carpetas siguen las pautas de módulos, paquetes y subpaquetes vistos hasta ahora en clase.
- [ ] Se han aplicado los principios de POO vistos en clase.
- [ ] Los nombres de ficheros, clases y variables son significativos y siguen los principios de la recomendación PEP8.

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

<details open>
  <summary>Fase 03 - testing</summary>

- [ ] Copiar en `03-testing` el estado base de `02-documentando` (o crear rama especifica para la fase 03).
- [ ] Reorganizar las pruebas en la subcarpeta `tests/`.
- [ ] Crear y mantener test para, al menos, dos clases del dominio.
- [ ] Verificar que todos los test pasan concon `python -m unittest`.
- [ ] Anadir `coverage` como dependencia de fase (en `requirements.txt`).
- [ ] Ejecutar cobertura con `coverage run -m unittest` y revisar reporte con `coverage report`.
- [ ] Documentar la ejecucion de tests y coverage en `docs/TESTS_Y_PASOS.md`.
- [ ] Actualizar `docs/EJECUCION.md` con pasos completos desde clonado hasta ejecucion.
- [ ] Revisar y corregir documentos desactualizados de `docs/` para reflejar la fase 03.
- [ ] Registrar los cambios de fase en `CHANGELOG.md` (version `0.3.0`).
- [ ] Actualizar `README.md` para reflejar estructura y comandos actuales.

</details>

## Aspectos a tener en cuenta durante el desarrollo del proyecto

- Hacer `pull` del repositorio para ver posibles comentarios del profesor o para descagar cambios hechos en otro equipo.
- Hacer commits periódicos cada vez que se complete una tarea mediante código.
- Hacer `push` después de cada commit
- Añadir al repositorio en subcarpeta las actividades completadas en clase
- Añadir en página en el repositorio enlace o copia de los materiales que va añadiendo el profesor.
