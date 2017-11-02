from ...cursor import db


class Usuario:
    
    def __init__(self, usuario_id=None):

        self.__usuario_id = None
        self.login = None
        self.__logado = 1 #padrão (deslogado)
        self.email = None
        self.caminho_foto = 'user_profile.jpg'

        if usuario_id is not None:
            data = db.get_usuario(usuario_id)
            if len(data) > 0:
                self.__usuario_id = usuario_id
                self.login = data[0]['usuario_login']
                self.email = data[0]['usuario_email']
                self.caminho_foto = data[0]['usuario_caminho_foto']

    def get_id(self):
        return self.__usuario_id

    def get_logado(self):
        return self.__logado


    def deleta(self):
        db.deleta_usuario(self.get_id())

    def salva(self):
        if self.get_id() is None:
            self.__usuario_id = db.cadastra_usuario(self)
        else:
            db.edita_usuario(self)
