from unittest.mock import patch
import pytest
from project.exceptions import ItemNotFound, DuplicateMovie
from project.models import User
from project.services import UsersService


class TestUserService:
    @pytest.fixture()
    @patch('project.dao.UsersDAO')
    def users_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = User(
            id=1, email='test@mail.ru', password='test_password',
            name='test_user', surname='test_surname', favorite_genre=7
        )
        dao.get_all_users.return_value = [
            User(
                id=1, email='test_1@mail.ru', password='test_password_1',
                name='test_user_1', surname='test_surname_1', favorite_genre=7
            ),


            User(
                id=2, email='test_2@mail.ru', password='test_password_2',
                name='test_user_2', surname='test_surname_2', favorite_genre=5
            )
        ]

        return dao

    @pytest.fixture()
    def user_service(self, users_dao_mock):
        return UsersService(dao=users_dao_mock)

    @pytest.fixture
    def user(self, db):
        obj_user = User(
            email='email', password='password', name='user',
            surname='surname', favorite_genre=7)
        db.session.add(obj_user)
        db.session.commit()
        return obj_user

    def test_get_user(self, user_service, user):
        assert user_service.get_item(user.id)

    def test_user_not_found(self, users_dao_mock, user_service):
        users_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            user_service.get_item(7)

    def test_user_by_email(self, user_service, user):
        assert user_service.get_user_by_email('test_1@mail.ru')

    def test_user_by_email_not_found(self, users_dao_mock, user_service):
        users_dao_mock.get_user_by_email.return_value = None

        with pytest.raises(ItemNotFound):
            user_service.get_user_by_email('test_7@mail.ru')

    def test_add_favirite_movie(self, user_service, users_dao_mock):
        user_id = 7
        movie_id = 5
        user_service.add_favorite_movie(user_id, movie_id)
        users_dao_mock.add_favorite_movie.assert_called_once_with(
            user_id, movie_id)

    def test_delete_favorite_movie(self, user_service, users_dao_mock):
        user_id = 7
        movie_id = 5
        user_service.delete_favorite_movie(user_id, movie_id)
        users_dao_mock.delete_favorite_movie.assert_called_once_with(
            user_id, movie_id)
