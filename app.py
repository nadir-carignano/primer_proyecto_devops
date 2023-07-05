from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    fecha_actual = datetime.now().date()
    vacaciones_julio = datetime(2023, 7, 7).date()
    dias_vacaciones = (vacaciones_julio - fecha_actual).days

    navidad = datetime(2023, 12, 25).date()
    dias_navidad = (navidad - fecha_actual).days

    año_nuevo= datetime(2024, 1, 1).date()
    dias_año_nuevo = (año_nuevo - fecha_actual).days

    return render_template("index.html", dias_vacaciones= dias_vacaciones,dias_navidad=dias_navidad,dias_año_nuevo=dias_año_nuevo)


@app.route("/index.html")
def indexx():
    fecha_actual = datetime.now().date()
    vacaciones_julio = datetime(2023, 7, 7).date()
    dias_vacaciones = (vacaciones_julio - fecha_actual).days

    navidad = datetime(2023, 12, 25).date()
    dias_navidad = (navidad - fecha_actual).days

    año_nuevo = datetime(2024, 1, 1).date()
    dias_año_nuevo = (año_nuevo - fecha_actual).days

    return render_template("index.html", dias_vacaciones=dias_vacaciones, dias_navidad=dias_navidad, dias_año_nuevo=dias_año_nuevo)
    #return render_template("index.html")


@app.route("/contacto.html")
def contacto():
    return render_template("contacto.html")

@app.route("/listaFeriados.html")
def lista_feriados():
    return render_template("listaFeriados.html")
