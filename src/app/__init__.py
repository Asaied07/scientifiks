from flask import Flask
import os
from app.routes import *  # Importar TODOS los blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    return app