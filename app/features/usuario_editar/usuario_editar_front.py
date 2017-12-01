from .usuario_editar_negocio import UsuarioEditarNegocio
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.foundanies_modelo import FoundaniesModelo
from ...authentication import retorna_usuario
from app import app
from ...utils.front_helper import *
@app.route('/usuario', methods=['GET', 'POST'])
@login_required

def usuario_editar(): 
        return UsuarioEditarNegocio.exibir()
    
    
   
