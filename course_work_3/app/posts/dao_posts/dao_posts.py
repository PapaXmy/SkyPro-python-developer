import json


class PostDAO:
    def __init__(self, path):
        """При создании экземпляра класса указывается путь к файлу json"""
        self.path = path

    def get_posts_all(self):
        """Возвращает все посты"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_by_user(self, user_name):
        """Возвращает посты определенного пользователя"""
        list_post = []
        for post in self.get_posts_all():
            if post["poster_name"] == user_name:
                list_post.append(post)
            if post["content"] in ["", " "]:
                return []

        return list_post

    def search_for_posts(self, query):
        """Возвращает список постов по ключевому слову"""
        if query in [" ", ""]:
            return []

        search_post = []
        for post in self.get_posts_all():
            if query.lower() in post["content"].lower():
                search_post.append(post)
        return search_post

    def get_post_by_pk(self, pk):
        """Возвращает пост по его идентификатору"""
        for post in self.get_posts_all():
            if post["pk"] == pk:
                return post


# pd = PostDAO("../../data/posts.json")
# print(pd.get_post_by_pk(1))
