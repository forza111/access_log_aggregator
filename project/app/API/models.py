from app import db

class AccessLog(db.Model):
    __tablename__ = "access_log"

    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(39), nullable=False)
    client_id = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, nullable=True)
    client_request = db.Column(db.String(300), nullable=False)
    status_code = db.Column(db.String(3), nullable=False)
    request_file_size = db.Column(db.String(100), nullable=False)
    referer = db.Column(db.String(300), nullable=False)
    user_agent = db.Column(db.String(300), nullable=False)

