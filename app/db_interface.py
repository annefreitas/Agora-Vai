from flask_mysqldb import MySQL
from .tables.usuario.usuario_interface import UsuarioInterface



class Zelda(UsuarioInterface):

    def __init__(self, app):
        self.mysql = MySQL(app)

    def execute_query(self, query, insert=False):
        cur = self.mysql.connection.cursor()
        cur.execute(query)
        if insert:
            self.mysql.connection.commit()
        else:
            data = cur.fetchall()
            cur.close()
            return data

    def verifica_existe_email(self,email):
        data = self.execute_query("select count(*) as cont_usuarios from usuario where usuario_email ='{}'".format(email))
        return int(data[0]['cont_usuarios']) > 0

    def verifica_existe_login(self, login):
        data = self.execute_query("select count(*) from usuario where usuario_login = '{}'".format(login))
        return int(data[0]['count(*)']) > 0
