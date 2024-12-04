import os

from flask import Flask, jsonify, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

commands = {"filter": lambda data, value: filter(lambda line: value in line, data)}


@app.route("/perform_query", methods=["POST"])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    cmd1 = request.json.get("cmd")
    value1 = request.json.get("value1")
    cmd2 = request.json.get("cmd2")
    value2 = request.json.get("value2")
    filename = request.json.get("filename")
    filepath = os.path.join(DATA_DIR, filename)

    if not os.path.isfile(filepath):
        return jsonify({"error": f"Файл {filename} не найден!"}), 404

    try:
        with open(filepath, "r") as file:
            data = file.readlines()

        if cmd1 in commands:
            data = commands[cmd1](data, value1)
        else:
            return jsonify({"error": f"Неизвестная конанда {cmd1}"})

        # elif cmd2 in commands:
        #     data = commands[cmd2](data, value2)
        # else:
        #     return jsonify({"error": f"Неизвестная конанда {cmd2}"})

        result = list(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # return app.response_class("", content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
