from flask import Blueprint, jsonify
from ..posts.dao_posts.dao_posts import PostDAO
from config import POST_PATH
import logging

api_b = Blueprint("api_b", __name__)
logging.basicConfig(
    filename="logs/api.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logging.info("Запрос")


dao_posts = PostDAO(POST_PATH)


@api_b.route("/api/posts")
def posts_api():
    logging.info("Запрос")
    posts = dao_posts.get_posts_all()
    return jsonify(posts), 200


@api_b.route("/api/posts/<int:post_id>")
def post_api(post_id):
    logging.info("Запрос")
    post = dao_posts.get_post_by_pk(post_id)
    return jsonify(post), 200
