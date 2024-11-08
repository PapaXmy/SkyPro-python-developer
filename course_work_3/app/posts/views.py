from flask import Blueprint, render_template, request
from .dao_posts.dao_posts import PostDAO
from ..comments.dao_comments.dao_comments import CommentsDAO
from config import POST_PATH, COMMENTS_PATH

pb = Blueprint("pb", __name__, template_folder="templates", static_folder="static")
post_dao = PostDAO(POST_PATH)
comments_dao = CommentsDAO(COMMENTS_PATH)


@pb.route("/")
def index_page():
    posts = post_dao.get_posts_all()
    return render_template("index.html", posts=posts)


@pb.route("/post/<int:post_id>")
def posts_page(post_id):
    post = post_dao.get_post_by_pk(post_id)
    comments = comments_dao.get_comments_post_id(post_id)
    comments_len = len(comments)
    return render_template(
        "post.html", post=post, comments=comments, comments_len=comments_len
    )


@pb.route("/search")
def seach_page():
    s = request.args.get("s", "")
    posts = post_dao.search_for_posts(s)
    post_count = len(posts)
    return render_template("search.html", posts=posts, post_count=post_count, query=s)


@pb.route("/user/<username>")
def user_page(username):
    users = post_dao.get_posts_by_user(username)
    return render_template("user-feed.html", users=users)
