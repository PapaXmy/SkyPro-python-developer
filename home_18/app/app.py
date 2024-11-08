from flask import Flask
from flask_restx import Api
from app.config import Config
from app.setup_db import db
from app.views.movie_view import movie_ns
from app.views.director_view import director_ns
from app.views.genre_view import genre_ns
from .views.auth_view import auth_ns
from .views.user_view import user_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    app_config = Config()
    app = create_app(app_config)
    app.run()
