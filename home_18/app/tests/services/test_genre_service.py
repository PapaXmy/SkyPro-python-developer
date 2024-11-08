import pytest
from ...service.genre_service import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_genre(self):
        genre = self.genre_service.get_genre(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_genres(self):
        genres = self.genre_service.get_genres()
        assert len(genres) > 0

    def test_create(self):
        genre_data = {"name": "Триллер"}
        genre = self.genre_service.create_genre(genre_data)
        assert genre.id is not None

    def test_delete_genre(self):
        self.genre_service.delete_genre(3)

    def test_update_genre(self):
        genre_data = {"id": 4, "name": "Триллер"}
        self.genre_service.update_genre(genre_data)
