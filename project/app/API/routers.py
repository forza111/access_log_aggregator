from flask import Blueprint, jsonify, request
from flask_restx import Api

from .models import AccessLogModel
from .schemas import access_log_schema
from ..database import db


api_bp = Blueprint('API', __name__, url_prefix="/api")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    api_bp,
    version="1.0",
    title="Flask API with JWT-Based Authentication",
    description="Welcome to the Swagger UI documentation site!",
    doc="/ui",
    authorizations=authorizations,
)


@api_bp.route("/access_logs")
def get_access_logs():
    logs = db.session.query(AccessLogModel).all()
    response = access_log_schema.dump(logs)
    return jsonify(response)

@api_bp.route("/access_logs/<ip>")
def get_access_logs_by_ip(ip):
    args = request.args
    date_before = args.get("date_before")
    date_after = args.get("date_after")
    logs = db.session.query(AccessLogModel).filter(AccessLogModel.ip_address == ip).order_by(AccessLogModel.id.asc())
    if date_before:
        logs = logs.filter(AccessLogModel.date < date_before)
    if date_after:
        logs = logs.filter(AccessLogModel.date > date_after)
    response = access_log_schema.dump(logs)
    return jsonify(response)
