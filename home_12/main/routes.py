from flask import Blueprint, render_template, request
from functions import get_post
from json import JSONDecodeError
import logging


mb = Blueprint("main", __name__, template_folder="templates")


@mb.route("/")
def main_page():
    return render_template("index.html")


@mb.route("/search")
def search_posts():
    search_post = request.args["s"]
    logging.info("Выполняется поиск")
    try:
        list_post = get_post(search_post)
    except FileNotFoundError:
        logging.info("Файл с постами не найден")
        return "Файл с постами не найден!"
    except JSONDecodeError:
        logging.info("Файл с постами не открывается")
        return "Файл с постами не открывается"
    return render_template(
        "post_list.html", search_post=search_post, list_post=list_post
    )
