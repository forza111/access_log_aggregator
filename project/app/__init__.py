from flask import Flask

from config import Config
from .access_log_aggregator.routers import module

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(module)


