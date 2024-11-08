import pytest
from project.models import Movie


class TestMoviesView:
    @pytest.fixture
    def movie(self, db):
        obj_movie = Movie(
            id=1,
            title="title",
            description="description",
            trailer="trailer",
            year=2000,
            rating=5,
            genre_id=7,
            director_id=5
        )
        db.session.add(obj_movie)
        db.session.commit()
        return obj_movie

    def test_many(self, client, movie):
        response = client.get('/movies/')
        assert response.status_code == 200
        assert response.json == [
            {
                "id": movie.id,
                "title": movie.title,
                "description": movie.description,
                "trailer": movie.trailer,
                "year": movie.year,
                "rating": movie.rating,
                "genre_id": movie.genre_id,
                "director_id": movie.director_id
            }
        ]

    def test_director_pages(self, client, movie):
        response = client.get('/movies/?pages=1')
        assert response.status_code == 200
        assert len(response.json) == 1

    def test_director_status(self, client, movie):
        response = client.get('/movies/?status=new')
        assert response.status_code == 200
        assert len(response.json) == 1

    def test_director_pages_status(self, client, movie):
        response = client.get('/movies/?status=new&page=1')
        assert response.status_code == 200
        assert len(response.json) == 1

    def test_movie(self, client, movie):
        response = client.get('/movies/1')
        assert response.status_code == 200
        assert response.json == {
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "trailer": movie.trailer,
            "year": movie.year,
            "rating": movie.rating,
            "genre_id": movie.genre_id,
            "director_id": movie.director_id
        }

    def test_movie_not_found(self, client, movie):
        response = client.get('/movies/2/')
        assert response.status_code == 404
