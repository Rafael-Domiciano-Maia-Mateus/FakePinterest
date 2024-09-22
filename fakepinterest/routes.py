from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.models import Usuario
from fakepinterest import login_manager

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)

@login_manager.user_loader
def load_user(id_usuario):
    return Usuario.query.get(int(id_usuario))
