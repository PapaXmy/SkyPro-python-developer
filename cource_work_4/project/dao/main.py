from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User, FavoriteMovie
from werkzeug.exceptions import NotFound
from typing import List, Optional, TypeVar
from project.setup.db.models import Base
from sqlalchemy import desc
from project.exceptions import ItemNotFound, DuplicateMovie

T = TypeVar('T', bound=Base)


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(
            self, page: Optional[int] = None, status: Optional[str] = None
    ) -> List[T]:
        stmt = self._db_session.query(self.__model__)
        if status == 'new':
            try:
                stmt = stmt.order_by(desc(self.__model__.year))
            except NotFound:
                return []

        if page:
            try:
                return stmt.paginate(
                    page=page, per_page=self._items_per_page, error_out=False
                ).items
            except NotFound:
                return []
        return stmt.all()


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def get_all_user(self):
        return self._db_session.query(self.__model__).all()

    def get_user_by_email(self, email: str):
        return self._db_session.query(User).filter(
            User.email == email).one_or_none()

    def create_user(self, user_data):
        user = User(**user_data)

        self._db_session.add(user)
        self._db_session.commit()

        return user

    def update_user(self, user):

        self._db_session.add(user)
        self._db_session.commit()

        return user

    def add_favorite_movie(self, user_id, movie_id):
        user = self.get_by_id(user_id)

        if user is None:
            raise ItemNotFound

        favorite_movie_duplicate = self._db_session.query(FavoriteMovie).filter(
            FavoriteMovie.name_id == user.id,
            FavoriteMovie.movie_id == movie_id).first()

        if favorite_movie_duplicate:
            raise DuplicateMovie
        else:
            favorite_movie_user = FavoriteMovie(
                name_id=user.id, movie_id=movie_id)

        self._db_session.add(favorite_movie_user)
        self._db_session.commit()

    def delete_favorite_movie(self, user_id, movie_id):
        favorite_movie = self._db_session.query(FavoriteMovie).filter(
            FavoriteMovie.name_id == user_id,
            FavoriteMovie.movie_id == movie_id).first()

        if favorite_movie:
            self._db_session.delete(favorite_movie)
            self._db_session.commit()
        else:
            raise ItemNotFound
