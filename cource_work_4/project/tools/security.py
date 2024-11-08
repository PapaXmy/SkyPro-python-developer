import base64
import hashlib
import hmac
from flask import current_app
from project.config import BaseConfig
from typing import Union
from flask import request, abort
import jwt
import datetime
import calendar
from project.exceptions import Unauthorized, ItemNotFound


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(
        __generate_password_digest(password)).decode('utf-8')

# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)


def compose_passwords(password_hash: Union[str, bytes], password: str) -> bool:
    return hmac.compare_digest(
        base64.b64decode(password_hash),
        hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt=current_app.config["PWD_HASH_SALT"],
            iterations=current_app.config["PWD_HASH_ITERATIONS"],
        )
    )


def auth_required(func):
    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            abort(401)

        user_data = request.headers['Authorization']
        token = user_data.split('Bearer ')[-1]

        if not token:
            raise Unauthorized('Токен не найден!')

        try:
            playload = jwt.decode(
                token, BaseConfig.SECRET_KEY, algorithms=[
                    BaseConfig.JWT_ALGORITHM])
            user_id = playload.get('id')
            request.user = {'id': user_id}

        except jwt.ExpiredSignatureError:
            raise Unauthorized('Токен истек!')
        except jwt.InvalidTokenError:
            raise Unauthorized('Неверный токен!')

        return func(*args, **kwargs)

    return wrapper


def generate_token(user_data) -> dict:
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    user_data['exp'] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(
        user_data, BaseConfig.SECRET_KEY, BaseConfig.JWT_ALGORITHM)

    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    user_data['exp'] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(
        user_data, BaseConfig.SECRET_KEY, BaseConfig.JWT_ALGORITHM)

    tokens = {'access_token': access_token, 'refresh_token': refresh_token}

    return tokens


def refresh_token(refresh_token) -> dict:

    user_data = jwt.decode(
        jwt=refresh_token,
        key=BaseConfig.SECRET_KEY,
        algorithms=BaseConfig.JWT_ALGORITHM
    )

    if user_data:
        return generate_token(user_data)

    raise ItemNotFound


def auth_user(user_json, user_db):
    email = user_json.get('email')
    password = user_json.get('password')

    if email and password:
        hashed_password = user_db.password

        if compose_passwords(hashed_password, password):
            return generate_token(user_json)

    raise ItemNotFound('Пользователь не найден.')
