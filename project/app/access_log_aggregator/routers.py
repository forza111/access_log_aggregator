from flask import Blueprint


module = Blueprint('API', __name__)

@module.route("/")
def hello_world():
    return "hello WorlD"