from app.dao.model.user import Users
from sqlalchemy.orm import Session


class UserDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_all_users(self):
        return self.session.query(Users).all()

    def get_user(self, uid):
        user = self.session.query(Users).get(uid)
        if not user:
            return None
        return user

    def get_user_username(self, username):
        return self.session.query(Users).filter(Users.username == username)

    def create_user(self, data):
        user = Users(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update_user(self, user):

        self.session.add(user)
        self.session.commit()

        return user

    def delete_user(self, uid):
        user = self.get_user(uid)

        self.session.delete(user)
        self.session.commit()
