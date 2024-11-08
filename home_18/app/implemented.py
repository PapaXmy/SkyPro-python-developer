from app.setup_db import db
from app.service.movie_serice import MovieService
from app.dao.movie_dao import MovieDAO
from app.service.director_service import DirectorService
from app.dao.director_dao import DirectorDAO
from app.service.genre_service import GenreService
from app.dao.genre_dao import GenreDAO
from app.service.user_service import UserService
from app.dao.user_dao import UserDAO
from app.service.auth_service import AuthService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_service)