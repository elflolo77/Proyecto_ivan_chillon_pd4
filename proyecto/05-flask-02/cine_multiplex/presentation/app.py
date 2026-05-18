"""Presentación: Rutas de Flask para la aplicación web."""

from flask import Flask, redirect, url_for

from cine_multiplex.infrastructure.repositorio_sqlite import RepositorioSQLite
from cine_multiplex.application.servicio_cine import ServicioCine
from cine_multiplex.infrastructure.errores import (
    EntidadNoEncontradaError,
    EntidadDuplicadaError,
    ErrorIntegridadDatos,
    ErrorPersistencia
)

app = Flask(__name__)
repositorio_cine = RepositorioSQLite("cine.db")
servicio = ServicioCine(repositorio_cine)

@app.route('/')
def inicio():
    return ('<h1>Cine Flolix</h1>'
            '<ul>'
            '<li><a href="/peliculas">Ver películas</a></li>'
            '<li><a href="/salas">Ver salas</a></li>'
            '<li><a href="/sesiones">Ver sesiones</a></li>'
            '<li><a href="/informe">Informe de ventas</a></li>'
            '</ul>')

# Peliculas
@app.route('/peliculas')
def listar_peliculas():
    try:
        peliculas = servicio.listar_peliculas()
        if not peliculas:
            return 'No hay películas.'
        lineas = [p.obtener_resumen_pelicula() for p in peliculas]
        return '<br>'.join(lineas)
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
        if not salas:
            return 'No hay salas.'
        lineas = [str(s) for s in salas]
        return '<br>'.join(lineas)
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
        if not sesiones:
            return 'No hay sesiones.'
        lineas = []
        for s in sesiones:
            estado_disponibilidad = "LLENA" if s.numero_asientos_libres == 0 else f"Libres: {s.numero_asientos_libres}"
            lineas.append(f"{s} | {estado_disponibilidad}")
        return '<br>'.join(lineas)
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
        return f"¡Entrada vendida! ID: {entrada.id_entrada} - Precio: ${entrada.precio_euros} <a href='/'>Volver</a>"
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
        return (f"Total Recaudado: ${estadisticas['total_recaudado']:.2f}<br>"
                f"Entradas Vendidas: {estadisticas['entradas_vendidas']}<br>"
                f"<a href='/'>Volver</a>")
    except ErrorPersistencia as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
