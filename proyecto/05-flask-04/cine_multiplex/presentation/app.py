"""Presentacion: rutas de Flask para la aplicacion web."""

import logging
from pathlib import Path
import sys

from flask import Flask, redirect, render_template, request, url_for

from cine_multiplex.application.servicio_cine import ServicioCine
from cine_multiplex.infrastructure.errores import (
    EntidadDuplicadaError,
    EntidadNoEncontradaError,
    ErrorIntegridadDatos,
    ErrorPersistencia,
)
from cine_multiplex.infrastructure.repositorio_sqlite import RepositorioSQLite

logging.basicConfig(
    filename="cine_multiplex.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

if not Path("cine.db").exists():
    ruta_proyecto = Path(__file__).resolve().parent.parent.parent
    sys.path.insert(0, str(ruta_proyecto))
    import crear_bd

app = Flask(__name__)
repositorio_cine = RepositorioSQLite("cine.db")
servicio = ServicioCine(repositorio_cine)
TARIFAS_ENTRADA = ("General", "Reducida", "Estudiante")


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


def _obtener_entrada(identificador_entrada):
    for entrada in repositorio_cine.listar_todas_las_entradas():
        if entrada.id_entrada == identificador_entrada:
            return entrada
    return None


def _render_formulario_pelicula(tipo, datos=None, error=None, status=200):
    return render_template(
        "form_pelicula.html",
        tipo=tipo,
        datos=datos or {},
        error=error,
    ), status


def _render_formulario_sala(datos=None, error=None, status=200):
    return render_template("form_sala.html", datos=datos or {}, error=error), status


def _render_formulario_sesion(datos=None, error=None, status=200):
    return render_template(
        "form_sesion.html",
        datos=datos or {},
        peliculas=servicio.listar_peliculas(),
        salas=servicio.listar_salas(),
        error=error,
    ), status


def _render_formulario_venta(datos=None, error=None, status=200):
    return render_template(
        "form_vender_entrada.html",
        datos=datos or {},
        sesiones=servicio.listar_sesiones(),
        tarifas=TARIFAS_ENTRADA,
        error=error,
    ), status


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/ayuda")
def ayuda():
    reglas = [regla for regla in app.url_map.iter_rules() if regla.endpoint != "static"]
    return render_template("ayuda.html", reglas=reglas)


@app.route("/peliculas")
def listar_peliculas():
    try:
        peliculas_vista = [
            {"resumen": pelicula.obtener_resumen_pelicula()}
            for pelicula in servicio.listar_peliculas()
        ]
        return render_template("peliculas.html", peliculas=peliculas_vista)
    except ErrorPersistencia as e:
        return str(e), 500


@app.route("/peliculas/registrar_comercial", methods=["GET", "POST"])
def registrar_pelicula_comercial():
    if request.method == "POST":
        datos = {k: request.form.get(k, "") for k in ("titulo", "duracion", "clasificacion", "genero", "distribuidora")}
        try:
            servicio.registrar_pelicula_comercial(
                datos["titulo"].strip(),
                int(datos["duracion"]),
                datos["clasificacion"].strip(),
                datos["genero"].strip(),
                datos["distribuidora"].strip(),
            )
            return redirect(url_for("listar_peliculas"))
        except EntidadDuplicadaError as e:
            return _render_formulario_pelicula("comercial", datos, str(e), 409)
        except ValueError as e:
            return _render_formulario_pelicula("comercial", datos, str(e), 400)
        except ErrorPersistencia as e:
            return str(e), 500
    return _render_formulario_pelicula("comercial")


@app.route("/peliculas/registrar_infantil", methods=["GET", "POST"])
def registrar_pelicula_infantil():
    if request.method == "POST":
        datos = {k: request.form.get(k, "") for k in ("titulo", "duracion", "clasificacion", "genero", "edad_minima")}
        try:
            servicio.registrar_pelicula_infantil(
                datos["titulo"].strip(),
                int(datos["duracion"]),
                datos["clasificacion"].strip(),
                datos["genero"].strip(),
                int(datos["edad_minima"]),
            )
            return redirect(url_for("listar_peliculas"))
        except EntidadDuplicadaError as e:
            return _render_formulario_pelicula("infantil", datos, str(e), 409)
        except ValueError as e:
            return _render_formulario_pelicula("infantil", datos, str(e), 400)
        except ErrorPersistencia as e:
            return str(e), 500
    return _render_formulario_pelicula("infantil")


@app.route("/peliculas/registrar_clasica", methods=["GET", "POST"])
def registrar_pelicula_clasica():
    if request.method == "POST":
        datos = {k: request.form.get(k, "") for k in ("titulo", "duracion", "clasificacion", "genero", "anio")}
        try:
            servicio.registrar_pelicula_clasica(
                datos["titulo"].strip(),
                int(datos["duracion"]),
                datos["clasificacion"].strip(),
                datos["genero"].strip(),
                int(datos["anio"]),
            )
            return redirect(url_for("listar_peliculas"))
        except EntidadDuplicadaError as e:
            return _render_formulario_pelicula("clasica", datos, str(e), 409)
        except ValueError as e:
            return _render_formulario_pelicula("clasica", datos, str(e), 400)
        except ErrorPersistencia as e:
            return str(e), 500
    return _render_formulario_pelicula("clasica")


@app.route("/salas")
def listar_salas():
    try:
        salas_vista = [{"descripcion": str(sala)} for sala in servicio.listar_salas()]
        return render_template("salas.html", salas=salas_vista)
    except ErrorPersistencia as e:
        return str(e), 500


@app.route("/salas/crear", methods=["GET", "POST"])
def crear_sala():
    if request.method == "POST":
        datos = {k: request.form.get(k, "") for k in ("numero_sala", "capacidad_maxima", "tecnologia_pantalla")}
        try:
            servicio.crear_sala(
                int(datos["numero_sala"]),
                int(datos["capacidad_maxima"]),
                datos["tecnologia_pantalla"].strip(),
            )
            return redirect(url_for("listar_salas"))
        except EntidadDuplicadaError as e:
            return _render_formulario_sala(datos, str(e), 409)
        except ValueError as e:
            return _render_formulario_sala(datos, str(e), 400)
        except ErrorPersistencia as e:
            return str(e), 500
    return _render_formulario_sala()


@app.route("/sesiones")
def listar_sesiones():
    try:
        sesiones_vista = []
        for sesion in servicio.listar_sesiones():
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


@app.route("/sesiones/programar", methods=["GET", "POST"])
def programar_sesion():
    if request.method == "POST":
        datos = {k: request.form.get(k, "") for k in ("identificador", "titulo_pelicula", "numero_sala", "fecha_hora")}
        try:
            servicio.programar_sesion(
                datos["identificador"].strip(),
                datos["titulo_pelicula"].strip(),
                int(datos["numero_sala"]),
                datos["fecha_hora"].strip(),
            )
            return redirect(url_for("listar_sesiones"))
        except EntidadDuplicadaError as e:
            return _render_formulario_sesion(datos, str(e), 409)
        except EntidadNoEncontradaError as e:
            return _render_formulario_sesion(datos, str(e), 404)
        except ErrorIntegridadDatos as e:
            return _render_formulario_sesion(datos, str(e), 400)
        except ValueError as e:
            return _render_formulario_sesion(datos, str(e), 400)
        except ErrorPersistencia as e:
            return str(e), 500
    return _render_formulario_sesion()


@app.route("/entradas/vender", methods=["GET", "POST"])
def vender_entrada():
    if request.method == "POST":
        datos = {k: request.form.get(k, "") for k in ("identificador_sesion", "categoria_tarifa")}
        try:
            servicio.vender_entrada(
                datos["identificador_sesion"].strip(),
                datos["categoria_tarifa"].strip(),
            )
            return redirect(url_for("informe"))
        except EntidadNoEncontradaError as e:
            return _render_formulario_venta(datos, str(e), 404)
        except ValueError as e:
            return _render_formulario_venta(datos, str(e), 400)
        except ErrorPersistencia as e:
            return str(e), 500
    return _render_formulario_venta()


@app.route("/entradas/anular", methods=["GET", "POST"])
def buscar_entrada_para_anular():
    datos = {"identificador_entrada": request.form.get("identificador_entrada", "")}
    if request.method == "POST":
        identificador_entrada = datos["identificador_entrada"].strip()
        entrada = _obtener_entrada(identificador_entrada)
        if not entrada:
            return render_template("form_anular_entrada.html", datos=datos, error="Entrada no encontrada."), 404
        return redirect(url_for("anular_entrada", identificador_entrada=identificador_entrada))
    return render_template("form_anular_entrada.html", datos={}, error=None)


@app.route("/entradas/anular/<identificador_entrada>", methods=["GET", "POST"])
def anular_entrada(identificador_entrada):
    entrada = _obtener_entrada(identificador_entrada)
    if not entrada:
        return render_template(
            "form_anular_entrada.html",
            datos={"identificador_entrada": identificador_entrada},
            error="Entrada no encontrada.",
        ), 404
    if request.method == "POST":
        try:
            servicio.anular_entrada(identificador_entrada)
            return redirect(url_for("informe"))
        except ErrorPersistencia as e:
            return str(e), 500
    return render_template("confirmar_anular_entrada.html", entrada=entrada)


@app.route("/informe")
def informe():
    try:
        estadisticas = servicio.informe_ventas()
        entradas = repositorio_cine.listar_todas_las_entradas()
        return render_template(
            "informe.html",
            estadisticas=estadisticas,
            entradas=entradas,
        )
    except ErrorPersistencia as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(debug=True)
