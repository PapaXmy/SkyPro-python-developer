import pytest
from unittest.mock import MagicMock
from ...dao.director_dao import DirectorDAO
from ...setup_db import db
from ...dao.model.director import Director
from ...dao.genre_dao import GenreDAO
from ...dao.model.genre import Genre
from ...dao.movie_dao import MovieDAO
from ...dao.model.movie import Movies


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    kirill = Director(id=1, name="Кирил Серебрянников")
    teylor = Director(id=2, name="Тейлор Шеридан")
    vladimir = Director(id=3, name="Владимир Вайншток")

    director_dao.get_director = MagicMock(return_value=kirill)

    director_dao.get_all_directors = MagicMock(
        return_value=[kirill, teylor, vladimir])

    director_dao.create_director = MagicMock(
        return_value=Director(id=4, name="Декстер Флетчер"))

    director_dao.update_director = MagicMock()
    director_dao.delete_director = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    horror = Genre(id=1, name="Ужасы")
    musical = Genre(id=2, name="Мюзикл")
    detective = Genre(id=3, name="Детектив")

    genre_dao.get_one_genre = MagicMock(return_value=horror)

    genre_dao.get_all_genres = MagicMock(
        return_value=[horror, musical, detective])

    genre_dao.create_genre = MagicMock(
        return_value=Genre(id=4, name="Триллер"))

    genre_dao.update_genre = MagicMock()
    genre_dao.delete_genre = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    venom = Movies(
        id=1,
        title="Веном",
        description="Хороший фильм",
        trailer="https://www.youtube.com/watch?v=n7GlLxV_Igk",
        year=2018,
        rating=6.8,
        genre_id=7,
        director_id=13
    )

    duna = Movies(
        id=2,
        title="Дюна",
        description="Фантастический фильм",
        trailer="https://www.youtube.com/watch?v=DOlTmIhEsg0",
        year=2021,
        rating=8.4,
        genre_id=7,
        director_id=11
    )

    movie_dao.get_movie = MagicMock(return_value=duna)
    movie_dao.get_all_movies = MagicMock(return_value=[venom, duna])
    movie_dao.create_movie = MagicMock(
        return_value=Movies(
            id=3,
            title="Сияние",
            description="Страшный фильм",
            trailer="https://www.youtube.com/watch?v=NMSUEhDWXH0",
            year=1980,
            rating=8.4,
            genre_id=6,
            director_id=14

        )
    )
    movie_dao.get_all_movies_by_director = MagicMock(return_value=duna.title)
    movie_dao.get_all_movies_by_year = MagicMock(return_value=venom.title)
    movie_dao.get_all_movies_by_genre = MagicMock(return_value=[
        venom.title, duna.title])
    movie_dao.update_movie = MagicMock()
    movie_dao.delete_movie = MagicMock()

    return movie_dao
