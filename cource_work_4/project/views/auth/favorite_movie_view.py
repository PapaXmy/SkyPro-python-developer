from flask_restx import Namespace, Resource
from project.container import user_service
from flask import request, abort
from project.exceptions import ItemNotFound, DuplicateMovie
from project.tools.security import auth_required

api = Namespace('favorites')


@api.route('/movie/<int:movie_id>')
class FavoriteMovie(Resource):

    @api.response(201, 'Фильм добавлен в избранное.')
    @auth_required
    def post(self, movie_id):
        user_id = request.user['id']
        try:
            user_service.add_favorite_movie(user_id, movie_id)
            return {'message': 'Фильм добавлен в избранное'}, 201
        except ItemNotFound:
            abort(404, 'Фильм или пользователь не найдены.')
        except DuplicateMovie:
            return {'message': 'Фильм уже доваблен в избранное.'}

    @api.response(200, 'Фильм удален из избранного.')
    @auth_required
    def delete(self, movie_id):
        user_id = request.user['id']

        if not user_id:
            abort(400, 'Не указан id пользователя.')

        try:
            user_service.delete_favorite_movie(user_id, movie_id)
            return {'message': 'Фильм удален из избранного.'}, 200
        except ItemNotFound:
            abort(404, 'Фильм или пользователь не найден.')
