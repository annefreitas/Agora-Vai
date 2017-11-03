from ..cursor import db
from ..tables.usuario.usuario_modelo import Usuario



class foundaniesModelo:

    
    @staticmethod
    def lista_usuarios():
        result = []
        for data in db.get_usuarios_ids():
            usuario = Usuario(data['usuario_id'])
            result.append(usuario)

        return result

   

        return result
