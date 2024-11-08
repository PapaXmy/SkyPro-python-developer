import json


class CommentsDAO:
    def __init__(self, path):
        """При создании экземпляра класса задается путь к файлу с данными"""
        self.path = path

    def load_comments(self):
        """Загружает все комментарии"""
        with open(self.path, "r") as file:
            comments = json.load(file)
            return comments

    def get_comments(self):
        """Возвращает список всех комментариев"""
        return self.load_comments()

    def get_comments_post_id(self, post_id):
        """Возвращает комментарии определенного поста"""
        list_comments = []
        for comment in self.get_comments():
            if comment["post_id"] == post_id:
                list_comments.append(comment)
        #        if not list_comments:
        #            raise ValueError("Нет такого комментария")

        return list_comments


# cd = CommentsDAO("../../data/comments.json")
# print(cd.get_comments_post_id('2'))
