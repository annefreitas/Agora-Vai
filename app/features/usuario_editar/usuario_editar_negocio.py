from flask import render_template, flash, redirect, url_for
from .usuario_editar_form import EditarUsuarioForm
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador
from ...utils.foundanies_modelo import FoundaniesModelo
from ...utils.files import flash_errors_extensao
from ...cursor import db

from app import app

class UsuarioEditarNegocio:
    def exibir(user_id):
        form = EditarUsuarioForm()

        usuario = Usuario(user_id)
        if usuario.get_id() is None:
            return redirect(url_for('home'))


        if form.validate_on_submit():

            data_1 = db.verifica_existe_login(form.usuario_login.data)
            if len(data_1) > 0 and (form.usuario_login.data != usuario.get_login()):
                flash("Login já cadastrado no sistema.")
                return render_template('usuario_editar.html', form=form)

            usuario.nome = form.usuario_nome.data
            usuario.sobrenome = form.usuario_sobrenome.data
            usuario.celular = form.usuario_celular.data
            usuario.idade = form.usuario_idade.data
            usuario.sexo = form.usuario_sexo.data
            
            usuario.login = form.usuario_login.data
            usuario.descricao= form.usuario_descricao.data
            usuario.salva()
            
            usuario.set_senha(form.usuario_senha.data)
            
            if form.file.data is not None:
                usuario.set_foto(form.file.data)
                if usuario.get_caminho_foto() is None:
                    flash_errors_extensao()
                    return render_template('usuario_editar.html', form=form)


            return redirect(url_for('home'))

        else:
            flash_errors(form)
        form.process()

        form.usuario_login.data = usuario.login

        return render_template('usuario_editar.html', form=form)
