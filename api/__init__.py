from flask import Flask
from .app import main

def create_app():
    app = Flask(__name__)
    app.secret_key = 'admin'
    app.register_blueprint(main)
    return app
