import pytest


class TestCommentsDAO:

    def test_path(self, dao_comments):
        assert (
            dao_comments.path == "../app/data/comments.json"
        ), "Неправильный путь к файлу"

    def test_get_comments(self, dao_comments):
        """Тест получения всех комментариев: тип, колличество"""
        comments = dao_comments.get_comments()
        assert type(comments) == list, "Коментарии должны быть списком"
        assert len(comments) == 20, "Неверное колличество комментариев"

    def test_get_comments_structure(self, dao_comments):
        """Проверка правильности списка комментариев"""
        comments = dao_comments.get_comments()
        structure_keys_dict = {"post_id", "commenter_name", "comment", "pk"}
        assert type(comments) == list, "Комментарии должны быть списком"
        assert len(comments) > 0, "Список не должен быть пустым"
        assert (
            set(comments[0].keys()) == structure_keys_dict
        ), "Неверный список кандидатов"

    comments_id = map(int, [1, 2, 3])

    @pytest.mark.parametrize("post_id", comments_id)
    def test_get_comments_by_id_type(self, post_id, dao_comments):
        """Тест полученных комментариев к каждому посту"""

        comments = dao_comments.get_comments_post_id(post_id)

        for comment in comments:
            assert comment["post_id"] == post_id
