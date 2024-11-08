import pytest
from ...service.director_service import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_sevice(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_director(self):
        director = self.director_service.get_director(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_directors()
        assert len(directors) > 0

    def test_create(self):
        director_data = {"name": "Дестер Флетчер"}
        director = self.director_service.create_director(director_data)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete_director(1)

    def test_update(self):
        director_data = {"id": 4, "name": "Декстер Флетчер"}
        self.director_service.update_director(director_data)
