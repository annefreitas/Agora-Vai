from flask import render_template, redirect, url_for
from ...cursor import db
from ...authentication import retorna_usuario
from ...utils.foundanies_modelo import foundaniesModelo

class HomeNegocio():
    
    def exibir():
        usuario = retorna_usuario()
        return render_template('home.html', usuario = usuario)
