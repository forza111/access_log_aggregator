from flask.cli import FlaskGroup

from app import app
from app.database import db
from app.API.models import AccessLogModel

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(AccessLogModel(ip_address='192.168.123.132',
                             client_id='-',
                             user_id='-',
                             date='2022-01-01 21:24',
                             client_request='GET /apache_pb.gif HTTP/1.0',
                             status_code='200',
                             request_file_size='64',
                             referer='http://www.example.com/start.html',
                             user_agent='Mozilla/4.08 [en] (Win98; I ;Nav)')
                   )
    db.session.commit()


if __name__ == '__main__':
    cli()
