from flask import render_template, redirect, url_for
from ...cursor import db
from ...authentication import retorna_usuario
from ..usuario_informacao.usuario_informacao_form import UsuarioInformacaoForm
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.foundanies_modelo import FoundaniesModelo

import os



class InformacaoNegocio():
    def exibir():
        form = UsuarioInformacaoForm()
        usuario = retorna_usuario()
        form.email.data = usuario.email
        form.usuario_nome.data= usuario.get_nome() 
        form.usuario_sobrenome.data= usuario.get_sobrenome()
        form.usuario_celular.data= usuario.get_celular()
        form.usuario_idade.data=usuario.get_idade() 
        form.usuario_sexo.data=usuario.get_sexo() 
        return render_template('informacao.html', form = form, usuario = usuario )
