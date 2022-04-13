from flask import Blueprint, jsonify
from .models import AccessLogModel
from .schemas import access_log_schema


api = Blueprint('API', __name__, url_prefix="/api")


@api.route("/access_logs")
def get_access_logs():
    logs = AccessLogModel.query.all()
    response = access_log_schema.dump(logs)
    return jsonify(response)