from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from project.exceptions import BaseServiceError
from project.setup.api import api
from project.setup.db import db
from project.views import genres_ns
from project.views.main.directors import api as directors_ns
from project.views.main.movies import api as movies_ns
from project.views.auth.user import api as user_ns
from project.views.auth.auth import api as auth_ns
from project.views.auth.favorite_movie_view import api as favorite_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    app.config['RESTX_ERROR_404_HELP'] = False

    CORS(app=app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(favorite_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app
