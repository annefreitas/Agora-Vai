from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField,TextField,TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

#Cadastra Usuario
class CadastrarUsuarioForm(Form):
    usuario_login = StringField('Login Usuario', validators=[DataRequired('Login do Usuario é obrigatório')])
    usuario_email = TextField("Email",  validators=[DataRequired("O seu email é obrigatório.")])
    usuario_senha = PasswordField('Senha', validators=[DataRequired('Senha do Usuario é obrigatório')])
    usuario_descricao = TextAreaField('Descrição')
    file = FileField('Foto do Usuário', validators=[])
