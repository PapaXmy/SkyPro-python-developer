from flask import request
from flask_restx import Resource, Namespace
from app.dao.model.user import UserSchema
from ..implemented import user_service

user_ns = Namespace("users")
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_users()
        return (users_schema.dump(all_users)), 200

    def post(self):
        user_json = request.json
        if user_service.get_user_username(user_json.get("username")):
            return "Пользователь с таким именем существует!"
        user_service.create_user(user_json)

        return "Пользователь добавлен!", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid: int):
        user = user_service.get_one_user(uid)
        return user_schema.dump(user), 200

    def put(self, uid: int):
        user_json = request.json
        user_json['id'] = uid

        user_service.update_user(user_json)
        return "Данные пользователя изменены!", 204

    def delete(self, uid: int):
        user = user_service.delete_user(uid)
        return f"Пользователь {user} удален!", 204
