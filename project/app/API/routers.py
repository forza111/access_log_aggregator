from flask import Blueprint, jsonify
from .models import AccessLog


module = Blueprint('API', __name__)

# @module.route("/")
# def hello_world():
#     response = AccessLog.query.first()
#     return {"ip": str(response.ip_address)}

@module.route("/")
def hello_world():
    response = AccessLog.query.all()
    return jsonify(json_list=[i.serialize for i in response])