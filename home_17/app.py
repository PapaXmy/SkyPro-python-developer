from flask import Flask, request
from marshmallow import fields, Schema
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

api = Api(app)
movie_ns = api.namespace("movie")
director_ns = api.namespace("director")
genre_ns = api.namespace("genre")


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class Director(db.Model):
    __tablename__ = "director"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class SchemaMovie(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()


class SchemaDirector(Schema):
    id = fields.Int()
    name = fields.Str()


class SchemaGenre(Schema):
    id = fields.Int()
    name = fields.Str()


movie_schema = SchemaMovie()
movies_schema = SchemaMovie(many=True)
director_schema = SchemaDirector()
directors_schema = SchemaDirector(many=True)
genre_schema = SchemaGenre()
genres_schema = SchemaGenre(many=True)

with app.app_context():
    db.create_all()


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        query = db.session.query(Movie)
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")

        if director_id is not None:
            query = db.session.query(Movie).filter(
                Movie.director_id == director_id)

        if genre_id is not None:
            query = db.session.query(Movie).filter(Movie.genre_id == genre_id)

        all_movies = query.all()
        return movies_schema.dump(all_movies), 200


@movie_ns.route("/<int:id>")
class MovieView(Resource):
    def get(self, id: int):
        movie = db.session.query(Movie).get(id)
        if movie is None:
            return "Фильм не найден!", 404
        return movie_schema.dump(movie), 200

    def delete(self, id: int):
        movie = db.session.query(Movie).get(id)

        if movie is None:
            return "Фильм не найден", 404

        db.session.delete(movie)
        db.session.commit()

        return "Фильм удален", 204


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        all_directors = db.session.query(Director).all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)

        with app.app_context():
            db.session.add(new_director)
            db.session.commit()

            return "Режисер добавлен!", 201


@director_ns.route("/<int:id>")
class DirectorView(Resource):
    def get(self, id: int):
        director = db.session.query(Director).get(id)

        if director is None:
            return "Режисер не найден!", 404
        return director_schema.dump(director), 200

    def put(self, id: int):
        director = db.session.query(Director).filter(Director.id == id).first()

        if director is None:
            return "Режисер не найден!", 404
        req_json = request.json

        director.name = req_json.get("name")

        db.session.add(director)
        db.session.commit()

        return "Данные режисера обновлены!"

    def delete(self, id: int):
        director = db.session.query(Director).get(id)
        if director is None:
            return "Режисер не найден!", 404

        db.session.delete(director)
        db.session.commit()

        return "Режисер удален!", 202


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        all_genres = db.session.query(Genre).all()

        if all_genres is None:
            return "Жанр не найден!", 404

        return genres_schema.dump(all_genres), 200

    def post(self):
        gen_json = request.json
        new_genre = Genre(**gen_json)

        with app.app_context():
            db.session.add(new_genre)
            db.session.commit()

            return "Жанр добавлен", 201


@genre_ns.route("/<int:id>")
class GenreView(Resource):
    def get(self, id: int):
        genre = db.session.query(Genre).get(id)

        if genre is None:
            return "Жанр не найден!", 404

        return genre_schema.dump(genre), 200

    def put(self, id: int):
        genre = db.session.query(Genre).get(id)
        gen_json = request.json

        genre.name = gen_json.get("name")

        db.session.add(genre)
        db.session.commit()

        return "Данные жанра обновленны!", 201

    def delete(self, id: int):
        genre = db.session.query(Genre).get(id)

        if genre is None:
            return "Жанр не найден!", 404

        db.session.delete(genre)
        db.session.commit()

        return "Жанр удален!", 204


if __name__ == "__main__":
    app.run()
