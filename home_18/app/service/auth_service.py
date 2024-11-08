import jwt
from flask import abort
import calendar
import datetime
from ..constants import secret, algo
from app.service.user_service import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, refresh=False):
        user = self.user_service.get_user_username(username)

        if user is None:
            raise Exception

        if not refresh:
            if not self.user_service.check_password(user.password, password):
                raise Exception("Invalid password")

        try:
            user_data = {"username": user.username, "role": user.role}

            min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            user_data["exp"] = calendar.timegm(min30.timetuple())
            access_token = jwt.encode(user_data, secret, algorithm=algo)

            days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
            user_data["exp"] = calendar.timegm(days130.timetuple())
            refresh_token = jwt.encode(user_data, secret, algorithm=algo)

            tokens = {"access_token": access_token,
                      "refresh_token": refresh_token}

            return tokens

        except Exception:
            raise Exception

    def refresh_token(self, refresh_token):
        try:
            user_data = jwt.decode(
                jwt=refresh_token, key=secret, algorithms=[algo])
        except jwt.ExpiredSignatureError:
            abort(401)
        except jwt.InvalidTokenError:
            abort(401)

        username = user_data.get("username")
        user = self.user_service.get_user_username(username=username)

        if user is None:
            raise Exception

        tokens = self.generate_tokens(username, user.password, refresh=True)

        if tokens is None:
            raise Exception

        return tokens
