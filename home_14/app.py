from flask import Flask, jsonify
from function import *

app = Flask(__name__)


@app.get("/movie/<title>/")
def page_movie(title):
    return get_movie_by_title(title)


@app.get("/movie/<int:year_1>/to/<int:year_2>")
def page_movie_by_year_release(year_1, year_2):
    return get_movies_by_year_release(year_1, year_2)


@app.get("/movie/rating/<rating>")
def page_movie_by_rating(rating):
    return get_movie_by_rating(rating)


@app.get("/genre/<genre>")
def page_movie_by_genre(genre):
    return get_movie_by_genre(genre)
