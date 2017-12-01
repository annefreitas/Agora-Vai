from .usuario_editar_negocio import UsuarioEditarNegocio
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.foundanies_modelo import FoundaniesModelo
from ...authentication import retorna_usuario
from app import app
from ...utils.front_helper import *
@app.route('/usuario/<user_id>', methods=['GET', 'POST'])
@login_required

def usuario_editar(user_id): 
        return UsuarioEditarNegocio.exibir(user_id)
    
    
   
