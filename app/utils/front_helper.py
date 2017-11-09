from functools import wraps
from flask import url_for, request, redirect, render_template, session, flash
from ..authentication import sessao_ativa, make_session_permanent, sessao_expirada, retorna_usuario
from .zelda_modelo import ZeldaModelo



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if sessao_expirada():
            flash("Sessão expirada")

        if not sessao_ativa():
            return redirect(url_for('login'))

        make_session_permanent()

        return f(*args, **kwargs)
    return decorated_function
