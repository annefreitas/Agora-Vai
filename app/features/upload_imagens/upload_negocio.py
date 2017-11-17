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
APP_ROOT1 = os.path.dirname(os.path.abspath(__file__))

class UploadNegocio:
    @app.route("/upload", methods=["POST"])
    @login_required
    def upload():
        usuario = retorna_usuario()
        #perfil
        caminho=usuario.get_id()
        target = os.path.join(APP_ROOT, "images\\{}".format(caminho))
        #perfil
        print(target)
        #perfil
        if not os.path.isdir(target):
            os.mkdir(target)
        else:
            print("Couldn't create upload directory: {}".format(target))
        print(request.files.getlist("file"))

        
        ######################################################################
        #perfil
        for upload in request.files.getlist("file"):
            print(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            destination = "/".join([target, filename])
            print ("Accept incoming file:", filename)
            print ("Save it to:", destination)
            upload.save(destination)
        ######################################################################
        #feed
        target1 = os.path.join(APP_ROOT1, "images\\feed")
        #feed
        print(target1)
        #####################################################################
        #feed
        if not os.path.isdir(target1):
            os.mkdir(target1)
        else:
            print("Couldn't create upload directory: {}".format(target1))
        print(request.files.getlist("file"))
        #####################################################################
        #feed
        for upload in request.files.getlist("file"):
            print(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            destination = "/".join([target1, filename])
            print ("Accept incoming file:", filename)
            print ("Save it to:", destination)
            upload.save(destination)
            
        return redirect(url_for('home'))



    @app.route('/upload/<filename>')
    @login_required
    def send_image(filename):
        usuario = retorna_usuario()
        return send_from_directory("features\\upload_imagens\\images\\{}".format(usuario.get_id()), filename)

    @app.route('/upload_feed/<filename>')
    @login_required
    def send_image_feed(filename):
        usuario = retorna_usuario()
        return send_from_directory("features\\upload_imagens\\images\\feed", filename)

