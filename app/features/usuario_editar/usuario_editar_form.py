from flask_wtf import Form
from wtforms import StringField, PasswordField, HiddenField, RadioField, SelectField, TextAreaField,TextField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Editar Usuário
class EditarUsuarioForm(Form):
    usuario_login = StringField('Login do Usuário', validators=[DataRequired('Login do Usuário é obrigatório')])
    usuario_senha = PasswordField('Senha do Usuário', validators=[DataRequired('A senha do Usuário é obrigatória')])
    usuario_descricao = TextAreaField('Descrição')
    usuario_nome = StringField('Informe seu nome', validators=[DataRequired('Nome do Usuario é obrigatório')])
    usuario_sobrenome = StringField('Informe seu sobrenome', validators=[DataRequired('Seu sobrenome é obrigatório')])
    usuario_sexo = StringField('Informe seu sexo', validators=[DataRequired('Seu sexo é obrigatório')])
    usuario_idade = StringField('Informe sua idade', validators=[DataRequired('Idade é obrigatória')])
    usuario_celular = IntegerField('Informe um nº de celular valido', validators=[DataRequired('Informe um nº de celular valido')])
    file = FileField('Foto do Usuário', validators=[])
