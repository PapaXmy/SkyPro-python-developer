import pytest
from project.models import FavoriteMovie, Movie, User
from project.tools.security import generate_token


class TestFavoriteMovieView:
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

    @pytest.fixture
    def favorite_movie(self, db):
        obj_favorite = FavoriteMovie(
            name_id=1,
            movie_id=1
        )
        db.session.add(obj_favorite)
        db.session.commit()
        return obj_favorite

    def test_add_favorite_movie(self, client, user, user_data_token):
        token = generate_token(user_data_token)
        response = client.post('/favorites/movie/1', json={
            "id": 1
        }, content_type='application/json', headers={
            'Authorization': f'Bearer {token["access_token"]}'})

        assert response.status_code == 201
        assert response.json['message'] == 'Фильм добавлен в избранное'

    def test_add_favorite_movie_without_id(self, client, user_data_token):

        token = generate_token(user_data_token)
        response = client.post('/favorites/movie/', json={

        },
            content_type='application/json',
            headers={
            'Authorization': f'Bearer {token["access_token"]}'})

        assert response.status_code == 404

    def test_delete_favorite_movie(
            self, client, user_data_token, favorite_movie):
        token = generate_token(user_data_token)
        response = client.delete('/favorites/movie/1', json={
        }, content_type='application/json',
            headers={'Authorization': f'Bearer {token["access_token"]}'})

        assert response.status_code == 200
        assert response.json['message'] == 'Фильм удален из избранного.'

    def test_delete_favorite_movie_without_id(self, client, user_data_token):
        token = generate_token(user_data_token)
        response = client.delete('/favorites/movie', headers={
            'Authorization': f'Bearer {token["access_token"]}'
        })
        assert response.status_code == 404
