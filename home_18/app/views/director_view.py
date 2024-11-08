from flask_restx import Resource, Namespace
from app.dao.model.director import DirectorSchema
from app.implemented import director_service
from ..decorators import auth_required, admin_required
from flask import request

director_ns = Namespace("directors")
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorsView(Resource):

    @auth_required
    def get(self):
        all_directors = director_service.get_directors()
        return (directors_schema.dump(all_directors)), 200

    @admin_required
    def post(self):
        director_json = request.json
        director_service.create_director(director_json)
        return "Режисер добавлен!", 201


@director_ns.route("/<int:uid>")
class DirectorView(Resource):

    @auth_required
    def get(self, uid: int):
        director = director_service.get_director(uid)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, did: int):
        director_json = request.json
        director_json["id"] = did

        director_service.update_director(director_json)
        return "Данные режисера изменены!", 204

    @admin_required
    def delete(self, did: int):
        director = director_service.delete_director(did)
        return f"Режисер {director} удален!", 204
