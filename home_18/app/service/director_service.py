from ..dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_director(self, did):
        return self.director_dao.get_director(did)

    def get_directors(self):
        return self.director_dao.get_all_directors()

    def create_director(self, data):
        return self.director_dao.create_director(data)

    def update_director(self, data):
        did = data.get("id")
        director = self.get_director(did)

        if director:
            director.name = data.get("name")

            self.director_dao.update_director(director)
        else:
            print(f"Режисер с id {did} не найден!")

    def delete_director(self, did):
        director = self.get_director(did)

        if director:
            self.director_dao.delete_director(did)
        else:
            print(f"Режисер с id {did} не найден!")
