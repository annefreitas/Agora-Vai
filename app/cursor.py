from app import app
from .db_interface import Foundanies

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'foundanies'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# init MYSQL
db = Foundanies(app)
