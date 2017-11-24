from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField,TextField,TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

#Cadastra Comentario
class CadastrarComentarioForm(Form):
    usuario_comentario = TextAreaField('Descrição')
  
