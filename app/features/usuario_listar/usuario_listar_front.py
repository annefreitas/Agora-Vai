from .usuario_listar_negocio import UsuarioListarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/usuario')
@login_required
def usuario_listar():
    return UsuarioListarNegocio.exibir()
