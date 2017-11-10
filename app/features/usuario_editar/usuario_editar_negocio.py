from flask import render_template, flash, redirect, url_for
from .usuario_editar_form import EditarUsuarioForm
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador
from ...utils.foundanies_modelo import FoundaniesModelo
from ...utils.files import flash_errors_extensao

from app import app

class UsuarioEditarNegocio:
    def exibir(user_id):
        form = EditarUsuarioForm()

        usuario = Usuario(user_id)
        if usuario.get_id() is None:
            return redirect(url_for('usuario_listar'))


        if form.validate_on_submit():
            usuario.login = form.usuario_login.data
            usuario.salva()
            
            usuario.set_senha(form.usuario_senha.data)
            
            if form.file.data is not None:
                usuario.set_foto(form.file.data)
                if usuario.get_caminho_foto() is None:
                    flash_errors_extensao()
                    return render_template('usuario_editar.html', form=form)


            return redirect(url_for('usuario_listar'))

        else:
            flash_errors(form)
        form.process()

        form.usuario_login.data = usuario.login

        return render_template('usuario_editar.html', form=form)
