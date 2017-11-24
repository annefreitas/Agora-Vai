from app import app
from .usuario_mostrar_comentario_negocio import ComentariosNegocio
from ...utils.front_helper import *

@app.route('/comentarios')
@login_required
def comentarios():
    return ComentariosNegocio.exibir()
