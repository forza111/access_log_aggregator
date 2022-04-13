from .models import AccessLogModel
from .ma import ma


class AccessLogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AccessLogModel


access_log_schema = AccessLogSchema(many=True, exclude=("id",))
