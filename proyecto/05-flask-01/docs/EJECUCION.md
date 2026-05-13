# EJECUCIÓN

Guía rápida para lanzar el programa "Cine Flolix".

## Requisitos previos
- **Python**: Se requiere cualquier versión funcional de `Python 3.x` (Preferiblemente Python 3.9 o superior).
- **Dependencias**: El programa no usa módulos de terceros (Pip) ajenos a *The Python Standard Library*. No es necesario montar un Virtual Environment restrictivo ni instalar librerías.

## Comandos

Deberás ubicar tu terminal (PowerShell, Bash o CMD) en la raíz específica de esta fase del proyecto:

```powershell
cd proyecto/02-documentando
```

## Ejecución de la Aplicación

Deberás ubicar tu terminal (PowerShell, Bash o CMD) en la raíz específica de esta fase del proyecto (`03-testing`):

```powershell
python main.py
```

De inmediato, aparecerá el promt interactivo de la Consola. Las entradas numéricas determinan el progreso del flujo.

---

## ACTUALIZACIÓN - 2026-04-15 (Fase 03: Testing)

Para esta fase, se han añadido nuevas capacidades de prueba y medición de cobertura.

### Requisitos adicionales
- **Dependencias**: Se requiere el paquete `coverage`. Puedes instalarlo con:
  ```powershell
  pip install -r requirements.txt
  ```

### Ejecución en Fase 03
Ubica tu terminal en la raíz de la fase actual:
```powershell
cd proyecto/03-testing
```

**Ejecutar la aplicación:**
```powershell
python main.py
```

**Ejecutar pruebas unitarias:**
```powershell
python -m unittest discover cine_multiplex/tests
```

**Generar reporte de cobertura:**
```powershell
coverage run -m unittest discover cine_multiplex/tests
coverage report
```
