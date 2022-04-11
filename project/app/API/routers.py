from flask import Blueprint, jsonify
from .models import AccessLog
# from .crud import *


module = Blueprint('API', __name__)

@module.route("/")
def hello_world():
    response = AccessLog.query.all()
    return jsonify(hi=response)
