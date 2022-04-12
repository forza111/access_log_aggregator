import os

from app import create_app


# from flask.cli import FlaskGroup
#
# from app.database import db
#
#
# cli = FlaskGroup(app)


# @cli.command("create_db")
# def create_db():
#     db.drop_all()
#     db.create_all()
#     db.session.commit()


app = create_app()

if __name__ == '__main__':
    app.run()
