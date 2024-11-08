import pytest


class TestPostsDAO:

    # все посты

    def test_path(self, dao_posts):
        """Тест пути к файлу"""
        assert dao_posts.path == "../app/data/posts.json", "Неправильный путь к файлу"

    def test_get_posts_all(self, dao_posts):
        """Тест получения всех постов"""
        posts = dao_posts.get_posts_all()
        assert type(posts) == list, "Посты должны быть списком"
        assert len(posts) == 8, "Неправильное колличество постов"

    def test_get_posts_all_structure(self, dao_posts):
        """Тест правильности списка комментариев"""
        posts = dao_posts.get_posts_all()
        sturcture_key_dict = {
            "poster_name",
            "poster_avatar",
            "pic",
            "content",
            "views_count",
            "likes_count",
            "pk",
        }
        assert set(posts[0].keys()) == sturcture_key_dict, "Неверный список кандидатов"

    # один пост

    get_posts_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    @pytest.mark.parametrize("post_pk", get_posts_by_pk)
    def test_get_post_by_pk(self, dao_posts, post_pk):
        """Тест получения поста по его id"""
        post = dao_posts.get_post_by_pk(post_pk)

    def test_get_post_by_pk_none(self, dao_posts):
        """Тест получения несуществующего поста"""
        no_post = dao_posts.get_post_by_pk(0)
        assert no_post == None

    # посты по пользователю

    post_by_user = [
        ("leo", {1, 5}),
        ("johnny", {2, 6}),
        ("hank", {3, 7}),
        ("larry", {4, 8}),
    ]

    @pytest.mark.parametrize("poster_name, post_pk", post_by_user)
    def test_get_post_by_user(self, dao_posts, poster_name, post_pk):
        """Тест поиска по пользователю"""

        posts = dao_posts.get_posts_by_user(poster_name)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pk

    # поиск постов

    post_search = [("пирог", {1}), ("птицы", {2}), ("свалка", {3}), ("пальто", {4})]

    @pytest.mark.parametrize("query, post_pk", post_search)
    def test_search_for_posts(self, dao_posts, query, post_pk):
        """Тест поиска постов"""

        posts = dao_posts.search_for_posts(query)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pk
