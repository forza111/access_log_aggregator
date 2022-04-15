from flask_bcrypt import Bcrypt
from flask import Flask


from config import Config
from .API.routers import api_bp
from .database import db
from .API.schemas import ma
from . import auth


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(api_bp)
    ma.init_app(app)
    return app

bcrypt = Bcrypt()