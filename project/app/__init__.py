from flask import Flask
# from flask_restplus import Api

from config import Config
from .API.routers import api
from .database import db
from .API.schemas import ma


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
# with app.test_request_context():
#     db.create_all()


app.register_blueprint(api)
ma.init_app(app)
