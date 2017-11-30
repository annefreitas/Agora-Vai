from app import app
from .informacao_negocio import InformacaoNegocio
from ...utils.front_helper import *


@app.route('/informacao')
@login_required
def informacao():
    return InformacaoNegocio.exibir()
