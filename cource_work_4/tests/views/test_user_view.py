import pytest
from project.models import User
from unittest.mock import patch
from project.tools.security import generate_token


class TestUsersView:
    @pytest.fixture
    def user(self, db):
        obj_user = User(
            id=1,
            email='test_mail@mail.ru',
            password='test_password',
            name='test_name',
            surname='test_surname',
            favorite_genre=7,
        )
        db.session.add(obj_user)
        db.session.commit()
        return obj_user

    @pytest.fixture
    def user_data_token(self):
        user = {
            "id": 1,
            "email": "test_mail@mail.ru",
            "password": "test_password"
        }
        return user

    def test_all_users(self, client, user):
        response = client.get('/users/')
        assert response.status_code == 200
        assert response.json == [
            {
                'id': user.id,
                'email': user.email,
                'password': user.password,
                'name': user.name,
                'surname': user.surname,
                'favorite_genre': user.favorite_genre
            }
        ]

    def test_user(self, client, user):
        response = client.get('/users/1')
        assert response.status_code == 200
        assert response.json == {
            'id': user.id,
            'email': user.email,
            'password': user.password,
            'name': user.name,
            'surname': user.surname,
            'favorite_genre': user.favorite_genre

        }

    def test_user_patch(self, client, user, user_data_token):
        token = generate_token(user_data_token)
        response = client.patch('/users/1', json={
            'id': 1,
            'email': 'test_mail@mail.ru',
            'password': 'test_password',
            'name': 'test_name_2',
            'surname': 'test_surname',
            'favorite_genre': 7
        }, content_type='application/json', headers={
            'Authorization': f'Bearer {token["access_token"]}'})

        assert response.status_code == 200
        assert response.json == {
            'id': user.id,
            'email': user.email,
            'password': user.password,
            'name': user.name,
            'surname': user.surname,
            'favorite_genre': user.favorite_genre
        }
        assert response.json['name'] == 'test_name_2'

    def test_update_password_success(self, client, user, user_data_token):
        token = generate_token(user_data_token)
        response = client.put('/users/password/1', json={
            'password_1': 'new_password',
            'password_2': 'new_password'
        }, content_type='application/json', headers={
            'Authorization': f'Bearer {token["access_token"]}'})

        assert response.status_code == 200

    def test_update_password_input_one(self, client, user, user_data_token):
        token = generate_token(user_data_token)
        response = client.put('/users/password/1', json={
            'password_1': 'new_password'
        }, content_type='application/json', headers={
            'Authorization': f'Bearer {token["access_token"]}'
        })
        assert response.status_code == 400
        assert response.json['message'] == 'Обязательно ввести два пароля для обновления!'

    def test_update_password_not_match(self, client, user, user_data_token):
        token = generate_token(user_data_token)
        response = client.put('/users/password/1', json={
            'password_1': 'new_password',
            'password_2': 'password'
        }, content_type='application/json', headers={
            'Authorization': f'Bearer {token["access_token"]}'
        })

        assert response.status_code == 400
        assert response.json['message'] == 'Пароли не совпадают.'
