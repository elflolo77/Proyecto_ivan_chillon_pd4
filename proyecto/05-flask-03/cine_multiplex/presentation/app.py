"""Presentación: Rutas de Flask para la aplicación web."""

import logging
from pathlib import Path
import sys

from flask import Flask, redirect, render_template, request, url_for

from cine_multiplex.infrastructure.repositorio_sqlite import RepositorioSQLite
from cine_multiplex.application.servicio_cine import ServicioCine
from cine_multiplex.infrastructure.errores import (
    EntidadNoEncontradaError,
    EntidadDuplicadaError,
    ErrorIntegridadDatos,
    ErrorPersistencia
)

logging.basicConfig(
    filename='cine_multiplex.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)

if not Path("cine.db").exists():
    ruta_proyecto = Path(__file__).resolve().parent.parent.parent
    sys.path.insert(0, str(ruta_proyecto))
    import crear_bd

app = Flask(__name__)
repositorio_cine = RepositorioSQLite("cine.db")
servicio = ServicioCine(repositorio_cine)

@app.before_request
def log_peticion():
    app.logger.info(f"{request.method} {request.path}")

@app.errorhandler(404)
def no_encontrado(e):
    return render_template(
        "error.html",
        codigo=404,
        titulo="Pagina no encontrada",
        mensaje="La ruta solicitada no existe en Cine Flolix.",
    ), 404

@app.errorhandler(500)
def error_servidor(e):
    return render_template(
        "error.html",
        codigo=500,
        titulo="Error del servidor",
        mensaje="No se ha podido completar la peticion en Cine Flolix.",
    ), 500

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/ayuda')
def ayuda():
    reglas = [regla for regla in app.url_map.iter_rules() if regla.endpoint != "static"]
    return render_template("ayuda.html", reglas=reglas)

# Peliculas
@app.route('/peliculas')
def listar_peliculas():
    try:
        peliculas = servicio.listar_peliculas()
        peliculas_vista = [
            {"resumen": pelicula.obtener_resumen_pelicula()}
            for pelicula in peliculas
        ]
        return render_template("peliculas.html", peliculas=peliculas_vista)
    except ErrorPersistencia as e:
        return str(e), 500

@app.route('/peliculas/registrar_comercial/<titulo>/<int:duracion>/<clasificacion>/<genero>/<distribuidora>')
def registrar_pelicula_comercial(titulo, duracion, clasificacion, genero, distribuidora):
    try:
        servicio.registrar_pelicula_comercial(titulo, duracion, clasificacion, genero, distribuidora)
        return redirect(url_for('listar_peliculas'))
    except EntidadDuplicadaError as e:
        return str(e), 409
    except ValueError as e:
        return str(e), 400
    except ErrorPersistencia as e:
        return str(e), 500

@app.route('/peliculas/registrar_infantil/<titulo>/<int:duracion>/<clasificacion>/<genero>/<int:edad_minima>')
def registrar_pelicula_infantil(titulo, duracion, clasificacion, genero, edad_minima):
    try:
        servicio.registrar_pelicula_infantil(titulo, duracion, clasificacion, genero, edad_minima)
        return redirect(url_for('listar_peliculas'))
    except EntidadDuplicadaError as e:
        return str(e), 409
    except ValueError as e:
        return str(e), 400
    except ErrorPersistencia as e:
        return str(e), 500

@app.route('/peliculas/registrar_clasica/<titulo>/<int:duracion>/<clasificacion>/<genero>/<int:anio>')
def registrar_pelicula_clasica(titulo, duracion, clasificacion, genero, anio):
    try:
        servicio.registrar_pelicula_clasica(titulo, duracion, clasificacion, genero, anio)
        return redirect(url_for('listar_peliculas'))
    except EntidadDuplicadaError as e:
        return str(e), 409
    except ValueError as e:
        return str(e), 400
    except ErrorPersistencia as e:
        return str(e), 500
    

# Salas
@app.route('/salas')
def listar_salas():
    try:
        salas = servicio.listar_salas()
        salas_vista = [{"descripcion": str(sala)} for sala in salas]
        return render_template("salas.html", salas=salas_vista)
    except ErrorPersistencia as e:
        return str(e), 500

@app.route('/salas/crear/<int:numero_sala>/<int:capacidad_maxima>/<tecnologia_pantalla>')
def crear_sala(numero_sala, capacidad_maxima, tecnologia_pantalla):
    try:
        servicio.crear_sala(numero_sala, capacidad_maxima, tecnologia_pantalla)
        return redirect(url_for('listar_salas'))
    except EntidadDuplicadaError as e:
        return str(e), 409
    except ValueError as e:
        return str(e), 400
    except ErrorPersistencia as e:
        return str(e), 500

# Sesiones
@app.route('/sesiones')
def listar_sesiones():
    try:
        sesiones = servicio.listar_sesiones()
        sesiones_vista = []
        for sesion in sesiones:
            estado_disponibilidad = (
                "LLENA"
                if sesion.numero_asientos_libres == 0
                else f"Libres: {sesion.numero_asientos_libres}"
            )
            sesiones_vista.append(
                {
                    "descripcion": str(sesion),
                    "estado_disponibilidad": estado_disponibilidad,
                }
            )
        return render_template("sesiones.html", sesiones=sesiones_vista)
    except ErrorPersistencia as e:
        return str(e), 500

@app.route('/sesiones/programar/<identificador>/<titulo_pelicula>/<int:numero_sala>/<fecha_hora>')
def programar_sesion(identificador, titulo_pelicula, numero_sala, fecha_hora):
    try:
        servicio.programar_sesion(identificador, titulo_pelicula, numero_sala, fecha_hora)
        return redirect(url_for('listar_sesiones'))
    except EntidadDuplicadaError as e:
        return str(e), 409
    except EntidadNoEncontradaError as e:
        return str(e), 404
    except ErrorIntegridadDatos as e:
        return str(e), 400
    except ValueError as e:
        return str(e), 400
    except ErrorPersistencia as e:
        return str(e), 500

# Entradas
@app.route('/entradas/vender/<identificador_sesion>/<categoria_tarifa>')
def vender_entrada(identificador_sesion, categoria_tarifa):
    try:
        entrada = servicio.vender_entrada(identificador_sesion, categoria_tarifa)
        return f"¡Entrada vendida! ID: {entrada.id_entrada} - Precio: {entrada.precio_euros} € <a href='/'>Volver</a>"
    except EntidadNoEncontradaError as e:
        return str(e), 404
    except ValueError as e:
        return str(e), 400
    except ErrorPersistencia as e:
        return str(e), 500

@app.route('/entradas/anular/<identificador_entrada>')
def anular_entrada(identificador_entrada):
    try:
        anulada = servicio.anular_entrada(identificador_entrada)
        if anulada:
            return "Entrada anulada correctamente. <a href='/'>Volver</a>"
        else:
            return "Entrada no encontrada.", 404
    except ErrorPersistencia as e:
        return str(e), 500

# Informe
@app.route('/informe')
def informe():
    try:
        estadisticas = servicio.informe_ventas()
        return render_template("informe.html", estadisticas=estadisticas)
    except ErrorPersistencia as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
