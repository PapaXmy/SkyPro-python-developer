from flask import request, abort
from app.constants import secret, algo
import jwt

def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        user_data = request.headers["Authorization"]
        token = user_data.split("Bearer ")[-1]
        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper

def admin_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        user_data = request.headers["Authorization"]

        # if not user_data.startswith("Bearer ")[-1]:
        #     abort(401)

        token = user_data.split("Bearer ")[-1]
        try:
            decoded_token = jwt.decode(token, secret, algorithms=[algo])
            user_role = decoded_token.get("role")
            if user_role != "admin":
                abort(403)
        except jwt.ExpiredSignatureError:
            abort(401)
        except jwt.InvalidTokenError:
            abort(401)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(403)

        return func(*args, **kwargs)

    return wrapper