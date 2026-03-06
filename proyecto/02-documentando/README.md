
## Checklist del proyecto

- [x] Crear cuenta en Github/codeberg
- [x] Crear repositorio para alojar/enlazar materiales de clase
- [x] Compartir repositorio con el usuario del profesor (ichigar)
- [x] Instalar y configurar GIT en ordenador de clase y en ordenador de casa.
- [x] Crear claves ssh en ordenador de casa y en ordenador de clase. Añadir claves públicas a las cuentas de github/codeberg
- [x] Clonar repositorio en clase y en casa
- [x] Probar a hacer cambios en clase y en casa y aprender a mantener actualizados los cambios realizados (clase/casa/repositorio)
- [x] Crear subcarpeta `proyecto` en repositorio.
- [x] Incluir en `README.md` descripción del proyecto
- [x] Crear en `proyecto` subcarpeta `01-capas` e incluir en la misma el código para dicha fase de tu proyecto

## Instalación

1. Clona el repositorio o descarga los archivos del proyecto.
2. Abre una terminal y navega hasta el directorio del proyecto:
   ```powershell
   cd d:\Users\Pepito\Documents\proyecto\Proyecto_ivan_chillon_pd4\proyecto\01-diseno_capas
   ```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando desde el directorio `01-diseno_capas`:

```powershell
python main.py
```

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