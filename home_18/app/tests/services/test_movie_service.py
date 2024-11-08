import pytest
from ...service.movie_service import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_movie(self):
        movie = self.movie_service.get_movie(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_movies(self):
        filter = {"director_id": 11, "genre_id": 7, "year": 2018}
        movies = self.movie_service.get_movies(filter)
        assert len(movies) > 0

    def test_create(self):
        movie_data = {
            "title": "Сияние",
            "description": "Страшный фильм",
            "trailer": "https://www.youtube.com/watch?v=NMSUEhDWXH0",
            "year": 1980,
            "rating": 8.4,
            "genre_id": 6,
            "director_id": 14
        }
        movie = self.movie_service.create_movie(movie_data)
        assert movie.id is not None

    def test_update_movie(self):
        movie_data = {
            "title": "Сияние",
            "description": "Страшный фильм",
            "trailer": "https://www.youtube.com/watch?v=NMSUEhDWXH0",
            "year": 1980,
            "rating": 8.4,
            "genre_id": 6,
            "director_id": 14
        }
        self.movie_service.update_movie(movie_data)
        self.movie_service.movie_dao.update_movie.assert_called_once()

    def test_delete_movie(self):
        self.movie_service.delete_movie(1)
        self.movie_service.movie_dao.delete_movie.assert_called_once_with(1)
