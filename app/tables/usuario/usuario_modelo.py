from ...cursor import db
from ...utils.files import upload
from ...utils.criptografador import Criptografador
from app import app

class Usuario:
    
    def __init__(self, usuario_id=None):

        self.__usuario_id = None
        self.login = None
        self.email = None
        self.__status = 0
        self.__caminho_foto = 'user_profile.jpg'
        self.__descricao=None
        self.__nome = None
        self.__sobrenome = None
        self.__celular = 0
        self.__idade = None
        self.__sexo = None
        
        
        

        if usuario_id is not None:
            data = db.get_usuario(usuario_id)
            if len(data) > 0:
                self.__usuario_id = usuario_id
                self.login = data[0]['usuario_login']
                self.email = data[0]['usuario_email']
                self.__status = data[0]['usuario_status']
                self.__caminho_foto = data[0]['usuario_caminho_foto']
                self.__descricao= data[0]['usuario_descricao']
                self.__nome = data [0] ['usuario_nome']
                self.__celular = data [0] ['usuario_celular']
                self.__idade = data [0] ['usuario_idade']
                self.__sexo = data [0] ['usuario_sexo']
                self.__sobrenome = data [0] ['usuario_sobrenome']
                
                
    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_celular(self):
        return self.__celular

    def get_idade(self):
        return self.__idade
     
    def get_sexo(self):
        return self.__sexo

    
    def get_id(self):
        return self.__usuario_id
    
    def get_login(self):
        return self.login


    def get_status(self):
        return self.__status

    def get_status_texto(self):
        if self.__status == 0:
            return 'Não confirmado'
        elif self.__status == 1:
            return 'Confirmado'
        
        return 'Indefinido'


    def get_caminho_foto(self):
        return self.__caminho_foto

    def get_descricao(self):
        return self.__descricao

    

    def ativa(self):
        if self.get_status() == 0:
            self.__status = 1
            db.ativa_usuario(self.get_id())


    def set_foto(self, arquivo_input):
        if self.get_id() is not None:
            caminho = upload(app.config['USUARIOS_UPLOAD_PATH'], arquivo_input, self.get_id())
            if caminho is not None:
                self.__caminho_foto = caminho
                db.edita_usuario_caminho_foto(self)

    def set_senha(self, senha):
        senhaHash = Criptografador.gerar_hash(senha, '')
        db.altera_senha(self.get_id(), senhaHash)

    def deleta(self):
        db.deleta_usuario(self.get_id())

    def salva(self):
        if self.get_id() is None:
            self.__usuario_id = db.cadastra_usuario(self)
        else:
            db.edita_usuario(self)

