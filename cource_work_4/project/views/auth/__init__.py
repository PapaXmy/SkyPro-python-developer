from .auth import api as auth_ns
from .user import api as user_ns
from .favorite_movie_view import api as favorite_ns

__all__ = [
    'auth_ns',
    'user_ns',
    'favorite_ns'
]
