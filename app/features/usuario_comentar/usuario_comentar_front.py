from .usuario_comentar_negocio import ComentarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/comentar', methods=['GET', 'POST'])
@login_required
def comentar():
    return ComentarNegocio.exibir()
