from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from .API.routers import module

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(module)
db = SQLAlchemy(app)


