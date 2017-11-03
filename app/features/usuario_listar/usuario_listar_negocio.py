from flask import render_template, flash, redirect, url_for
from ...utils.flash_errors import flash_errors
from ...utils.foundanies_modelo import foundaniesModelo

class UsuarioListarNegocio:

    def exibir():
        usuarios = foundaniesModelo.lista_usuarios()
        return render_template('usuario_listar.html', usuarios = usuarios)
