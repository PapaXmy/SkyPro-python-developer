from flask import Blueprint, render_template, request
from functions import add_post, check_extension
from config import UPLOAD_FOLDER
import logging

lb = Blueprint("loader", __name__, template_folder="templates")


@lb.route("/post", methods=["GET", "POST"])
def load_post():
    return render_template("post_form.html")


@lb.route("/uploaded", methods=["POST"])
def page_load_post():
    content = request.form["content"]
    picture = request.files.get("picture")

    if not content:
        return "Пост не написан."

    filename = picture.filename

    if filename == "":
        return "Картинка не выбрана!"

    if check_extension(filename):
        picture.save(f"./uploads/images/{filename}")
    else:
        extention = filename.split(".")[-1]
        return f"Файлы с расширением {extention} не поддерживаются."
        logging.info("Загрузка не поддерживаемого рнасширения файла")
    path_picture_json = UPLOAD_FOLDER + "/" + filename
    new_post = add_post(path_picture_json, content)
    return render_template("post_uploaded.html", new_post=new_post)
