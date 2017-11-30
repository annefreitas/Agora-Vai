from flask import render_template, flash, redirect, url_for, send_from_directory
from ...utils.flash_errors import flash_errors
from ...utils.foundanies_modelo import FoundaniesModelo
from ...utils.files import flash_errors_extensao
from ...tables.usuario.usuario_modelo import Usuario
from ...cursor import db
from flask_json import json_response
from ...utils.front_helper import *
from flask_mysqldb import MySQL
from ...authentication import retorna_usuario
import os

from app import app
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
class UploadNegocio:
    @app.route("/upload", methods=["POST"])
    @login_required
    
    def upload():
        vet=[]
        usuario = retorna_usuario()
        caminho=usuario.get_id()
        
        target_1 = os.path.join(APP_ROOT, "images\\feed") 
        target = os.path.join(APP_ROOT, "images\\{}".format(caminho))

        #devia salvar a imagem no diretorio perfil
        for upload in request.files.getlist("file"):
            filename = upload.filename
            filename_1= upload.filename
            
            destination = "/".join([target, filename])
            destination_1 = "/".join([target_1, filename1])
            
            upload.save(destination)
            upload.save(destination_1)
            
        return redirect(url_for('home'))

    
    @app.route('/upload/<filename>')
    @login_required
    def send_image(filename):
        usuario = retorna_usuario()
        return send_from_directory("features\\upload_imagens\\images\\{}".format(usuario.get_id()), filename)

    @app.route('/upload_feed/<filename>')
    @login_required
    def send_image_feed(filename):
        return send_from_directory("features\\upload_imagens\\images\\feed", filename)

