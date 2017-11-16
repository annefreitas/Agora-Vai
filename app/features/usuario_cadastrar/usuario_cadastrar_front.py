from .usuario_cadastrar_negocio import UsuarioCadastrarNegocio
from app import app
from ...utils.front_helper import *

@app.route('/cadastrar', methods=['GET', 'POST'])
def usuario_cadastrar():
   return UsuarioCadastrarNegocio.exibir()
