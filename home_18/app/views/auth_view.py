from flask_restx import Resource, Namespace
from flask import request, abort
from app.implemented import auth_service


auth_ns = Namespace("auth")


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        auth_json = request.json
        username = auth_json.get("username", None)
        password = auth_json.get("password", None)

        if None in [username, password]:
            abort(400)

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201

    def put(self):
        auth_json = request.json
        refresh_token = auth_json.get("refresh_token")
        tokens = auth_service.refresh_token(refresh_token)

        return tokens, 201
