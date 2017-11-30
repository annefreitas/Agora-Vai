from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField,TextField,TextAreaField,IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

#Cadastra Usuario
class UsuarioInformacaoForm(Form):
    usuario_login = StringField('Login Usuario', validators=[DataRequired('Login do Usuario é obrigatório')])
    usuario_nome = StringField('Informe seu nome', validators=[DataRequired('Nome do Usuario é obrigatório')])
    usuario_sobrenome = StringField('Informe seu sobrenome', validators=[DataRequired('Seu sobrenome é obrigatório')])
    usuario_sexo = StringField('Informe seu sexo', validators=[DataRequired('Seu sexo é obrigatório')])
    usuario_idade = StringField('Informe sua idade', validators=[DataRequired('Idade é obrigatória')])
    usuario_celular = IntegerField('Informe o nº do seu celular', validators=[DataRequired('Nº de celular é obrigatório')])
    email = TextField("Email",  validators=[DataRequired("O seu email é obrigatório.")])
    usuario_senha = PasswordField('Senha', validators=[DataRequired('Senha do Usuario é obrigatório')])
    usuario_descricao = TextAreaField('Descrição')
    file = FileField('Foto do Usuário', validators=[])
