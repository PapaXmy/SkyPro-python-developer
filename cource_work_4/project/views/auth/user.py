from flask_restx import Namespace, Resource
from project.container import user_service
from project.setup.api.models import user
from flask import request
from project.exceptions import ItemNotFound
from project.tools.security import auth_required
from werkzeug.exceptions import BadRequest

api = Namespace('users')


@api.route('/')
class UsersView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='ok')
    def get(self):
        """
        Получение всех пользователей.
        """
        return user_service.get_all()


@api.route('/<int:user_id>')
class UserView(Resource):
    @api.response(404, 'Не найден')
    @api.marshal_with(user, code=200, description='ok')
    def get(self, user_id: int):
        """
        Получение пользователя по id.
        """

        return user_service.get_item(user_id)

    @api.response(404, 'Не найден')
    @api.marshal_with(user, code=200, description='ok')
    @auth_required
    def patch(self, user_id):
        """
        Изменение информации пользователя.
        """
        user_json = request.json
        user_json['id'] = user_id

        return user_service.update_user(user_json), 200


@api.route('/password/<int:user_id>')
class UserViewPut(Resource):
    @api.response(404, 'Не найден')
    @api.marshal_with(user, code=200, description='ok')
    @auth_required
    def put(self, user_id: int):
        """
        Изменение пароля пользователя.
        """
        user_json = request.json
        user_json['id'] = user_id

        password_1 = user_json.get('password_1')
        password_2 = user_json.get('password_2')

        if not password_1 or not password_2:
            raise BadRequest(
                'Обязательно ввести два пароля для обновления!')

        if password_1 != password_2:
            raise BadRequest('Пароли не совпадают.')

        updated_password = user_service.update_user(user_json, password_1)
        return updated_password, 200
