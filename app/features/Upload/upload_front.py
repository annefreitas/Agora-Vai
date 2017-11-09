from .upload_negocio import *
from app import app
from ...utils.front_helper import *
import os
@app.route("/up")
@login_required
def up():
    return render_template("upload.html")
        
