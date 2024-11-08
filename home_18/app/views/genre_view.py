from flask_restx import Resource, Namespace
from app.dao.model.genre import GenreSchema
from ..implemented import genre_service
from ..decorators import auth_required, admin_required
from flask import request

genre_ns = Namespace("genres")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):

    @auth_required
    def get(self):
        all_genres = genre_service.get_genres()
        return genres_schema.dump(all_genres), 200

    @admin_required
    def post(self):
        genre_json = request.json
        genre_service.create_genre(genre_json)
        return "Жанр добавлен!", 201

@genre_ns.route("/<int:uid>")
class GenreView(Resource):

    @auth_required
    def get(self, uid: int):
        genre = genre_service.get_genre(uid)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, gid: int):
        genre_json = request.json
        genre_json["id"] = gid

        genre_service.update_genre(genre_json)
        return "Данные жанра изменены!", 204

    @admin_required
    def delete(self, gid: int):
        genre = genre_service.delete_genre(gid)
        return f"Жанр {genre} удален!", 204
