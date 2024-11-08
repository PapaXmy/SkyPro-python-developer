from .model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def get_one_genre(self, gid):
        return self.session.query(Genre).get(gid)

    def create_genre(self, data):
        genre = Genre(**data)

        self.session.add(genre)
        self.session.commit()

        return genre

    def update_genre(self, genre):
        self.session.add(genre)
        self.session.commit()

        return genre

    def delete_genre(self, gid):
        genre = self.get_one_genre(gid)

        self.session.delete(genre)
        self.session.commit()
