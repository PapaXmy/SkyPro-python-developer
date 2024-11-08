from ..dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genre(self, gid):
        return self.genre_dao.get_one_genre(gid)

    def get_genres(self):
        return self.genre_dao.get_all_genres()

    def create_genre(self, data):
        return self.genre_dao.create_genre(data)

    def update_genre(self, data):
        gid = data.get("id")
        genre = self.get_genre(gid)

        if genre:
            genre.name = data.get("name")

            self.genre_dao.update_genre(genre)

        else:
            print(f"Жанр с id {gid} не найден!")

    def delete_genre(self, gid):
        genre = self.get_genre(gid)

        if genre:
            self.genre_dao.delete_genre(gid)
        else:
            print(f"Жанр с id {gid} не найден!")
