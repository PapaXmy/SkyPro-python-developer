import pytest
from unittest.mock import patch
from project.exceptions import ItemNotFound
from project.models import Movie
from project.services import MoviesService


class TestMovieService:

    @pytest.fixture()
    @patch('project.dao.MoviesDAO')
    def movie_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = Movie(
            id=1,
            title='test_movie',
            description='test_description',
            trailer='test_trailer',
            year=1990,
            rating=7.7,
            genre_id=7,
            director_id=4
        )
        dao.get_all.return_value = [
            Movie(
                id=1,
                title='test_movie_1',
                description='test_description_1',
                trailer='test_trailer_1',
                year=1990,
                rating=7.7,
                genre_id=7,
                director_id=4
            ),
            Movie(
                id=2,
                title='test_movie_2',
                description='test_description_2',
                trailer='test_trailer_2',
                year=1992,
                rating=6.7,
                genre_id=6,
                director_id=5
            )
        ]
        return dao

    @pytest.fixture()
    def movies_service(self, movie_dao_mock):
        return MoviesService(dao=movie_dao_mock)

    @pytest.fixture
    def movie(self, db):
        obj_movie = Movie(
            id=1,
            title='test_title',
            description='test_description',
            trailer='test_trailer',
            year=1992,
            rating=6.7,
            genre_id=6,
            director_id=5
        )
        db.session.add(obj_movie)
        db.session.commit()
        return obj_movie

    def test_get_movie(self, movies_service, movie):
        assert movies_service.get_item(movie.id)

    def test_get_movie_not_found(self, movie_dao_mock, movies_service):
        movie_dao_mock.get_by_id.return_value = None
        with pytest.raises(ItemNotFound):
            movies_service.get_item(27)

    @pytest.mark.parametrize(('status', 'page'),
                             [
                                 ('new', 1), ('new', None),
                                 (None, 1), (None, None)

    ], ids=[
                                 'new_with_page',
                                 'new_without_page',
                                 'with_page',
                                 'without_page'])
    def test_get_movies(self, movie_dao_mock, movies_service, status, page):
        movies = movies_service.get_all(status=status, page=page)
        assert len(movies) == 2
        assert movies == movie_dao_mock.get_all.return_value
        movie_dao_mock.get_all.assert_called_with(status=status, page=page)
