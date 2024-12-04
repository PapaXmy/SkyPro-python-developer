import os

from flask import Flask, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def filter_query(data, value):
    return filter(lambda line: value in line, data)


def map_query(data, value):
    return map(lambda line: line.split()[int(value)], data)


def unique_query(data, value):
    return iter(set(data))


def sort_query(data, value):
    return iter(sorted(data, reverse=value == "desc"))


def limit_query(data, value):
    return (line for i, line in enumerate(data) if i < int(value))


commands = {
    "filter": filter_query,
    "map": map_query,
    "unique": unique_query,
    "sort": sort_query,
    "limit": limit_query,
}


@app.route("/perform_query", methods=["POST"])
def perform_query():
    cmd1 = request.json.get("cmd1")
    value1 = request.json.get("value1")
    cmd2 = request.json.get("cmd2")
    value2 = request.json.get("value2")
    filename = request.json.get("filename")
    filepath = os.path.join(DATA_DIR, filename)

    if not os.path.isfile(filepath):
        return (
            app.response_class(
                f"Файл {filename} не найден!", content_type="text/plain"
            ),
            404,
        )

    try:
        with open(filepath, "r") as file:
            data = file.readlines()

        if cmd1 in commands:
            data = commands[cmd1](data, value1)
        else:
            return (
                app.response_class(
                    f"Неизвестная конанда {cmd1}", content_type="text/plain"
                ),
                400,
            )
        if cmd2 in commands:
            data = commands[cmd2](data, value2)
        else:
            return (
                app.response_class(
                    f"Неизвестная конанда {cmd2}", content_type="text/plain"
                ),
                400,
            )

        result = "\n".join(data)
        return app.response_class(result, content_type="text/plain")
    except Exception as e:

        return app.response_class(f"Ошибка: {str(e)}", content_type="text/plain"), 500


if __name__ == "__main__":
    app.run(debug=True)
