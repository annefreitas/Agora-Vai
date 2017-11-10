from flask import render_template, flash, redirect, url_for
from ...utils.flash_errors import flash_errors
from ...utils.foundanies_modelo import FoundaniesModelo

class UsuarioListarNegocio:

    def exibir():
        usuarios = FoundaniesModelo.lista_usuarios()
        return render_template('usuario_listar.html', usuarios = usuarios)
