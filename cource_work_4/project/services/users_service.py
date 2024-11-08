from project.exceptions import ItemNotFound
from project.models import User
from project.dao.main import UsersDAO
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_all(self):
        return self.dao.get_all_user()

    def get_user_by_email(self, email: str):

        if user := self.dao.get_user_by_email(email):
            return user
        raise ItemNotFound(f'Пользователь с почтой {email} не существует!')

    def get_item(self, pk: int) -> User:

        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(
            f'Пользователь с порядковым номером {pk} не существует!')

    def create_user(self, data):
        password = data.get('password')

        if password:
            data['password'] = generate_password_hash(data.get('password'))
        else:
            raise ItemNotFound(
                'При создании пользователя нужно обязательно указать пароль!')
        return self.dao.create_user(data)

    def update_user(self, user_data, new_password=None):
        uid = user_data['id']
        user = self.get_item(uid)

        if not user:
            raise ItemNotFound('Пользователь не найден!')

        if new_password is None:
            user.email = user_data.get('email')
            user.name = user_data.get('name')
            user.surname = user_data.get('surname')
            user.favorite_genre = user_data.get('favorite_genre')

            if user_data.get('password'):
                user.password = generate_password_hash(user_data['password'])

        else:
            user.password = generate_password_hash(new_password)

        self.dao.update_user(user)

        return user

    def add_favorite_movie(self, user_id: int, movie_id: int):
        return self.dao.add_favorite_movie(user_id, movie_id)

    def delete_favorite_movie(self, user_id, movie_id):
        return self.dao.delete_favorite_movie(user_id, movie_id)
