import pytest
from project.models import User
from unittest.mock import patch
from project.tools.security import generate_password_hash


class TestAuthView:
    @pytest.fixture
    def user(self, db):
        obj_user = User(
            email='test_mail@mail.ru',
            password=generate_password_hash('test_password'),
        )
        db.session.add(obj_user)
        db.session.commit()
        return obj_user

    def test_register_user(self, db, client):
        response = client.post('/auth/register', json={
            "email": "test@mail.ru",
            "password": "test_password"
        })

        assert response.status_code == 200
        assert response.json['email'] == 'test@mail.ru'

    def test_register_not_email(self, db, client):
        response = client.post('/auth/register', json={
            'email': 'test@mail.ru'
        })

        assert response.status_code == 400
        assert response.json['message'] == 'Не введены почта или пароль.'

    def test_user_login_user_not_found(self, db, client):
        response = client.post('/auth/login', json={
            'email': 'not_existing@mail.ru',
            'password': 'test_password'
        })

        assert response.status_code == 404

    def test_user_login(self, user, db, client):
        response = client.post('/auth/login', json={
            'email': 'test_mail@mail.ru',
            'password': 'test_password'
        })
        assert response.status_code == 200
        assert 'access_token' in response.json
        assert 'refresh_token' in response.json
