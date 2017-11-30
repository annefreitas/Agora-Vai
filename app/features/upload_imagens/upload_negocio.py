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

from django.db.models.signals import post_save

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

        
        for upload in request.files.getlist("file"):

            filename = upload.filename  #diretorio 0
            filename_1= upload.filename #diretorio 1
            
            destination = "/".join([target, filename]) #diretorio 0
            destination_1 = "/".join([target_1, filename_1]) #diretorio 1
            
            upload.save(destination) #diretorio 0
            post_save()
            upload.save(destination_1) #diretorio 1
            
            
            
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

