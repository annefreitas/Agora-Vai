from .usuario_editar_negocio import UsuarioEditarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/usuario', methods=['GET', 'POST'])
@login_required

def usuario_editar(user_id):
    return UsuarioEditarNegocio.exibir(user_id)
   
