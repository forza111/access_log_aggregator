from .models import AccessLog

def get_logs():
    response = AccessLog.query.all()
    return response