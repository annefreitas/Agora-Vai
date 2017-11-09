from flask import render_template, flash, redirect, url_for, send_from_directory
from ...utils.flash_errors import flash_errors
from ...utils.zelda_modelo import ZeldaModelo
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
        usuario = retorna_usuario()
        caminho=usuario.get_id()
        target = os.path.join(APP_ROOT, "images\\{}".format(caminho))
        print(target)
        if not os.path.isdir(target):
            os.mkdir(target)
        else:
            print("Couldn't create upload directory: {}".format(target))
        print(request.files.getlist("file"))
        for upload in request.files.getlist("file"):
            print(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            destination = "/".join([target, filename])
            print ("Accept incoming file:", filename)
            print ("Save it to:", destination)
            upload.save(destination)
        return redirect(url_for('home'))


    @app.route('/upload/<filename>')
    @login_required
    def send_image(filename):
        usuario = retorna_usuario()
        return send_from_directory("features\\upload_imagens\\images\\{}".format(usuario.get_id()), filename)

