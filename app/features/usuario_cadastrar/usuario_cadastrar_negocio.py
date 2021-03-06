from flask import render_template, flash, redirect, url_for
from .usuario_cadastrar_form import CadastrarUsuarioForm
from ...cursor import db
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador
from ...utils.foundanies_modelo import FoundaniesModelo
from ...utils.files import flash_errors_extensao
from flask_json import json_response
from ...utils.mailer import Mailer, enviar_email_confirmacao

class UsuarioCadastrarNegocio:

    def exibir():

        form = CadastrarUsuarioForm()

        if form.validate_on_submit():
           
            data = db.verifica_existe_email(form.usuario_email.data)
            data_1 = db.verifica_existe_login(form.usuario_login.data)

            if len(data) > 0:
                flash("Email já cadastrado no sistema.")
                return render_template('usuario_criar.html', form=form)

            if len(data_1) > 0:
                flash("Login já cadastrado no sistema.")
                return render_template('usuario_criar.html', form=form)
            
            usuario = Usuario()
            usuario.nome = form.usuario_nome.data
            usuario.sobrenome = form.usuario_sobrenome.data
            usuario.celular = form.usuario_celular.data
            usuario.idade = form.usuario_idade.data
            usuario.sexo = form.usuario_sexo.data
            usuario.email = form.usuario_email.data
            usuario.login = form.usuario_login.data
            usuario.descricao= form.usuario_descricao.data
            usuario.salva()
            usuario.set_senha(form.usuario_senha.data)

            if form.file.data is not None:
                usuario.set_foto(form.file.data)
                if usuario.get_caminho_foto() is None:
                    flash_errors_extensao()
                    return render_template('usuario_criar.html', form=form)
                
            enviar_email_confirmacao(usuario)

            return redirect(url_for('login'))

        else:
            flash_errors(form)

        return render_template('usuario_criar.html', form=form)
