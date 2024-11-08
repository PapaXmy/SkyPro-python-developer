import pytest
from app.comments.dao_comments.dao_comments import CommentsDAO
from app.posts.dao_posts.dao_posts import PostDAO


@pytest.fixture
def dao_comments():
    return CommentsDAO("../app/data/comments.json")


@pytest.fixture
def dao_posts():
    return PostDAO("../app/data/posts.json")
