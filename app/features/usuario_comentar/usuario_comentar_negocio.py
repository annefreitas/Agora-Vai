from flask import render_template, redirect, url_for
from ...cursor import db
from ...authentication import retorna_usuario
from ..usuario_confirmar_email.usuario_confirmar_email_form import ConfirmarEmailForm
import os



class ComentarNegocio():
    def exibir():
        form = ConfirmarEmailForm()
        usuario = retorna_usuario()
        form.usuario_id.data = usuario.get_id()
        form.email.data = usuario.email
        image_names = os.listdir('./app/features/upload_imagens/images/feed/')
        return render_template('usuario_comentar.html', form = form, usuario = usuario,image_names=image_names )