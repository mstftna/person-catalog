from flask import Flask
import flask_login


app = Flask(__name__, template_folder='view')

app.secret_key = "14m6d4"  

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

from src.controller import main
from src.controller import auth
