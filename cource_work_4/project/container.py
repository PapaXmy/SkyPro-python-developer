from project.dao import GenresDAO, DirectorsDAO, MoviesDAO, UsersDAO
from project.services import GenresService, DirectorsService, MoviesService, UsersService
from project.setup.db import db

# DAO
director_dao = DirectorsDAO(db.session)
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)

# Services
director_service = DirectorsService(dao=director_dao)
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
