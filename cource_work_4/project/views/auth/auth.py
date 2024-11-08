from flask_restx import Namespace, Resource
from project.container import user_service
from project.setup.api.models import user
from flask import request
from project.exceptions import ItemNotFound
from project.tools.security import auth_user, refresh_token
from werkzeug.exceptions import BadRequest

api = Namespace('auth')


@api.route('/register')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='ok')
    def post(self):
        auth_json = request.json
        email = auth_json.get('email')
        password = auth_json.get('password')

        if None in [email, password]:
            raise BadRequest('Не введены почта или пароль.')

        return user_service.create_user(auth_json)


@api.route('/login')
class AuthView(Resource):
    def post(self):
        auth_json = request.json
        email = auth_json.get('email')
        user = user_service.get_user_by_email(email=email)
        tokens = auth_user(auth_json, user)

        return tokens

    def put(self):
        token_json = request.json
        new_token = token_json.get('refresh_token')
        return refresh_token(new_token)
