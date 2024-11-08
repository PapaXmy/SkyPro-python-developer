from flask import Flask, send_from_directory
from main.routes import mb
from loader.routes import lb
from config import UPLOAD_FOLDER
import logging

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.register_blueprint(mb)
app.register_blueprint(lb)


@app.route("/uploads/images/<path:path>")
def static_dir(path):
    return send_from_directory(app.config["UPLOAD_FOLDER"], path)


if __name__ == "__main__":
    app.run()
