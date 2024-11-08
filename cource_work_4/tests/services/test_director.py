from unittest.mock import patch
import pytest
from project.exceptions import ItemNotFound
from project.models import Director
from project.services import DirectorsService


class TestDirectorService:

    @pytest.fixture()
    @patch('project.dao.DirectorsDAO')
    def directors_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = Director(id=1, name='test_director')
        dao.get_all.return_value = [
            Director(id=1, name='test_director_1'),
            Director(id=2, name='test_director_2')
        ]
        return dao

    @pytest.fixture()
    def director_service(self, directors_dao_mock):
        return DirectorsService(dao=directors_dao_mock)

    @pytest.fixture
    def director(self, db):
        director = Director(name='Стенли Кубрик')
        db.session.add(director)
        return director

    def test_get_director(self, director_service, director):
        assert director_service.get_item(director.id)

    def test_director_not_found(self, director_service, directors_dao_mock):
        directors_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            director_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with_page', 'without_page'])
    def test_get_directors(self, directors_dao_mock, director_service, page):
        directors = director_service.get_all(page=page)
        assert len(directors) == 2
        assert directors == directors_dao_mock.get_all.return_value
        directors_dao_mock.get_all.assert_called_with(page=page)
