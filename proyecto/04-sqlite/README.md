
# Fase 02: Documentación y Refactorización del Diseño en Capas

## Descripción General
Este directorio (`02-documentando`) contiene la evolución del proyecto base originado en la fase 01. En esta fase se ha garantizado la correcta estructuración del código orientándose en Patrones de Diseño, aplicando convenciones de código (PEP-8) y ampliando exhaustivamente la documentación teórica.

## Documentación del Proyecto
Toda la documentación arquitectónica, funcional y de reglas de negocio reside encapsulada en la carpeta `docs/`.

Por favor, comienza tu lectura en el índice global:
👉 **[Acceder a docs/README.md](docs/README.md)**

## Instrucciones Rápidas

Para probar la lógica implementada asilada de Base de Datos en memoria:

1. Abre tu terminal y cerciórate de que te encuentras sobre la raíz de la fase actual:
```powershell
cd proyecto/02-documentando
```

2. Ejecuta el programa:
```powershell
python main.py
```

<details open>
  <summary>Fase 02 - documentando</summary>

- [x] Copiado en subcarpeta `02-documentando` el contenido actual de la carpeta `01-diseno_capas` o se crea una nueva rama para la nueva etapa (antes crear la rama 01-diseno-capas).
- [x] Renombrar todos los identificadores de modulos, clases, métodos y variables que no cumplan con los [criterios de los apuntes](https://ichigar.codeberg.page/pd4/ut1/recursos/poo_ut1_6_documentacion/#eligiendo-nombres)
- [x] Añadir docstring a los módulos, clases y métodos públicos del proyecto siguiendo los [criterios de los apuntes](https://ichigar.codeberg.page/pd4/ut1/recursos/poo_ut1_6_documentacion/#eligiendo-nombres).
- [x] Comentar las reglas de negocio de las clases del dominio.
- [x] Comentar los bloques de código que no expresen claramente para qué se usan.
- [x] Eliminar comentarios evidentes.
#### Usando como referencia los [documentos del proyecto model](https://codeberg.org/ichigar/cepy_pd4/src/branch/main/proyecto/02-documentando/expendedora) añadir los siguientes ficheros:
- [x] README.md
- [x] CHANGELOG.md
- [x] `docs/README.md`
- [x] `docs/DESCRIPCION_Y_ALCANCE.md`
- [x] `docs/EJECUCION.md`
- [x] `docs/ARQUITECTURA_POR_CAPAS.md`
- [x] `docs/CASOS_DE_USO.md`
- [x] `docs/REGLAS_DE_NEGOCIO.md`
- [x] `docs/MODELO_DE_DOMINIO.md`
- [x] `docs/CONTRATO_REPOSITORIO.md`
- [x] `docs/DATOS_INICIALES.md`
- [x] `docs/TESTS_Y_PASOS.md`
- [x] `docs/TROUBLESHOOTING.md`
</details>

# FASE III. TESTING
## Instrucciones

Para probar la lógica y las pruebas unitarias en esta fase del proyecto:

1. Abre tu terminal en la raíz de la fase actual:
```powershell
cd proyecto/03-testing
```

2. Ejecutar la aplicación:
```powershell
python main.py
```

3. Ejecutar las pruebas unitarias:
```powershell
python -m unittest discover cine_multiplex/tests
```

4. Ejecutar reporte de cobertura:
```powershell
coverage run -m unittest discover cine_multiplex/tests; coverage report
```

<details>
  <summary>Fase 03 - testing</summary>

- [x] Copiar en `03-testing` el estado base de `02-documentando` (o crear rama especifica para la fase 03).
- [x] Reorganizar las pruebas en la subcarpeta `tests/`.
- [x] Crear y mantener test para, al menos, dos clases del dominio.
- [x] Verificar que todos los test pasan con `python -m unittest`.
- [x] Anadir `coverage` como dependencia de fase (en `requirements.txt`).
- [x] Ejecutar cobertura con `coverage run -m unittest` y revisar reporte con `coverage report`.
- [x] Documentar la ejecucion de tests y coverage en `docs/TESTS_Y_PASOS.md`.
- [x] Actualizar `docs/EJECUCION.md` con pasos completos desde clonado hasta ejecucion.
- [x] Revisar y corregir documentos desactualizados de `docs/` para reflejar la fase 03.
- [x] Registrar los cambios de fase en `CHANGELOG.md` (version `0.3.0`).
- [x] Actualizar `README.md` para reflejar estructura y comandos actuales.

</details>