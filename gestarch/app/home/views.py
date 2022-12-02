# app/home/views.py

from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    """
    Retorna o HTML para a página inicial
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Retorna o HTML para o dashboard (página inicial após login)
    """
    return render_template('home/dashboard.html', title="Dashboard")
