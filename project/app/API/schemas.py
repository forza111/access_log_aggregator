from flask_marshmallow import Marshmallow

from .models import AccessLog

ma = Marshmallow()


class AccessLogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AccessLog
        load_instance = True
