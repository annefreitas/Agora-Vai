from flask import render_template, redirect, url_for
from ...cursor import db
from ...authentication import retorna_usuario
from ..usuario_confirmar_email.usuario_confirmar_email_form import ConfirmarEmailForm
import os



class ComentariosNegocio():
    def exibir():
        form = ConfirmarEmailForm()
        usuario = retorna_usuario()
        form.usuario_id.data = usuario.get_id()
        form.email.data = usuario.email
        return render_template('usuario_mostrar_comentario.html', form = form, usuario = usuario)