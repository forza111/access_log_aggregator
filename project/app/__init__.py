from flask import Flask

from config import Config
from .API.routers import module
from .database import db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
# with app.test_request_context():
#     db.create_all()
app.register_blueprint(module)

