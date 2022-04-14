import os

from app import create_app

def test_config():
    app = create_app()
    assert app.config["SQLALCHEMY_DATABASE_URI"] ==