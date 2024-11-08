import json
from config import ALLOWED_EXTENSIONS


def load_json_file():
    """Загрузка постов из json файла"""
    with open("posts.json", "r") as file:
        data = json.load(file)

    return data


# print(load_json_file()[1]["content"])


def get_post(word):
    """Поиск постов по слову"""
    found_posts = [post for post in load_json_file() if word.lower()
                   in post["content"]]
    #    for post in load_json_file():
    #   if word in post["content"]:
    #       found_posts.append(post)

    return found_posts


# print(get_post("остров"))


def add_post(picture_path, text_post):
    """Добавляет пост в json файл и возвращает его"""
    list_posts = load_json_file()
    json_post = {"pic": picture_path, "content": text_post}
    list_posts.append(json_post)

    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(list_posts, file, ensure_ascii=False, indent=4)

    return load_json_file()[-1]


# print(add_post("ssfssf", "ffdggsh"))


def check_extension(filename):
    """Проверка является ли файл картинкой по расширению"""
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


def load_picture(picture):
    """Загрузка картинки поста, возвращает путь к файлу"""
    filename = picture.filename
    if check_extension(filename):
        picture.save(f"./uploads/images/{filename}")
        return f"/uploads/images/{filename}"
