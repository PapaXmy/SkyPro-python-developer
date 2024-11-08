import pytest
from project.dao import UsersDAO
from project.models import User, Movie, FavoriteMovie
from project.exceptions import DuplicateMovie, ItemNotFound


class TestUserDAO:
    @pytest.fixture
    def user_dao(self, db):
        return UsersDAO(db.session)

    @pytest.fixture
    def user_1(self, db):
        user = User(
            email="test_user_email_1@mail.ru",
            password="test_password_1",
            name="test_user_name_1",
            surname="test_user_surname_1",
            favorite_genre=7
        )

        db.session.add(user)
        db.session.commit()
        return user

    @pytest.fixture
    def user_2(self, db):
        user = User(

            email="test_user_email_2@mail.ru",
            password="test_password_2",
            name="test_user_name_2",
            surname="test_user_surname_2",
            favorite_genre=5
        )

        db.session.add(user)
        db.session.commit()
        return user

    @pytest.fixture
    def movie(self, db):
        movie = Movie(
            title="Сияние",
            description="Страшный фильм",
            trailer="trailer.ru/film/Сияние",
            year=1980,
            rating=8.4,
            genre_id=6,
            director_id=14
        )
        return movie

    def test_get_movie_by_id(self, user_dao, user_1):
        assert user_dao.get_by_id(user_1.id) == user_1

    def test_get_user_by_id_not_found(self, user_dao):
        assert not user_dao.get_by_id(pk=1)

    def test_get_all_users(self, user_dao, user_1, user_2):
        assert user_dao.get_all_user() == [user_1, user_2]

    def test_get_user_by_email(self, user_dao, user_1, user_2):
        assert user_dao.get_user_by_email(
            "test_user_email_1@mail.ru").name == "test_user_name_1"

    def test_add_favorite_movie(self, db, user_dao, user_1, movie):
        user_dao.add_favorite_movie(user_1.id, movie.id)
        favorite_movie = db.session.query(FavoriteMovie).filter(
            FavoriteMovie.name_id == user_1.id,
            FavoriteMovie.movie_id == movie.id
        ).first()

        assert favorite_movie is not None
        assert favorite_movie.name_id == user_1.id
        assert favorite_movie.movie_id == movie.id

    def test_add_duplicate_favorite_movie_raises_error(
            self, user_dao, user_2, movie):
        user_dao.add_favorite_movie(user_2.id, movie.id)
        with pytest.raises(DuplicateMovie):
            user_dao.add_favorite_movie(user_2.id, movie.id)

    def test_delete_favorite_movie(self, db, user_dao, user_2, movie):
        user_dao.add_favorite_movie(user_2.id, movie.id)
        user_dao.delete_favorite_movie(user_2.id, movie.id)
        favorite_movie = db.session.query(FavoriteMovie).filter(
            FavoriteMovie.name_id == user_2.id,
            FavoriteMovie.movie_id == movie.id
        ).first()

        assert favorite_movie is None

    def test_delete_favorite_movie_raises_error(
            self, db, user_dao, user_2, movie):
        user_dao.add_favorite_movie(user_2.id, movie.id)
        with pytest.raises(ItemNotFound):
            user_dao.delete_favorite_movie(movie.id, user_2.id)
