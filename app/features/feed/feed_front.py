from app import app
from .feed_negocio import FeedNegocio
from ...utils.front_helper import *

@app.route('/')
@app.route('/feed')
@login_required
def feed():
    return FeedNegocio.exibir()
