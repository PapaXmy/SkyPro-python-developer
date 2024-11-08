from flask import Flask
from app.posts.views import pb
from app.api.views import api_b

app = Flask(__name__)

app.register_blueprint(pb)
app.register_blueprint(api_b)


if __name__ == "__main__":
    app.run(debug=True)
