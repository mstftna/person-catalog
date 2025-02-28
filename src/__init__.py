from flask import Flask
# import os.path
import flask_login


# app = Flask(__name__)
app = Flask(__name__, template_folder='view')

app.secret_key = "14m6d4"  

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# TEMPLATE_DIR = 'view'
# STATIC_DIR = os.path.abspath('../static')

# # app = Flask(__name__) # to make the app run without any
# app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

from src.controller import main
from src.controller import auth