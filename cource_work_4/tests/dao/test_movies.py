import pytest
from project.dao import MoviesDAO
from project.models import Movie


class TestMovieDAO:

    @pytest.fixture
    def movie_dao(self, db):
        return MoviesDAO(db.session)

    @pytest.fixture
    def movie_1(self, db):
        movie = Movie(
            title="Омерзительная восьмерка",
            description="Хороший фильм",
            trailer="trailer.ru/film/Омерзительная восьмерка",
            year=2015,
            rating=7.8,
            genre_id=4,
            director_id=2
        )
        db.session.add(movie)
        db.session.commit()
        return movie

    @pytest.fixture
    def movie_2(self, db):
        movie = Movie(
            title="Сияние",
            description="Страшный фильм",
            trailer="trailer.ru/film/Сияние",
            year=1980,
            rating=8.4,
            genre_id=6,
            director_id=14
        )
        db.session.add(movie)
        db.session.commit()
        return movie

    def test_get_movie_by_id(self, movie_dao, movie_1):
        assert movie_dao.get_by_id(movie_1.id) == movie_1

    def test_get_movie_by_id_not_found(self, movie_dao):
        assert not movie_dao.get_by_id(1)

    def test_get_all_movies(self, movie_dao, movie_1, movie_2):
        assert movie_dao.get_all() == [movie_1, movie_2]

    def test_get_movies_by_page_status(self, app, movie_dao, movie_1, movie_2):
        app.config['ITEM_PER_PAGE'] = 1
        assert movie_dao.get_all(page=1) == [movie_1, movie_2]
        assert movie_dao.get_all(page=2) == []
        assert movie_dao.get_all(status='new')[0].year == 2015
