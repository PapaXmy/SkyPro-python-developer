from app.dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self, filters):
        if filters.get("director_id") is not None:
            movie = self.movie_dao.get_all_movies_by_director(
                filters.get("director_id")
            )
        elif filters.get("genre_id") is not None:
            movie = self.movie_dao.get_all_movies_by_genre(
                filters.get("genre_id"))
        elif filters.get("year") is not None:
            movie = self.movie_dao.get_all_movies_by_year(filters.get("year"))
        else:
            movie = self.movie_dao.get_all_movies()
        return movie

    def get_movie(self, mid):
        movie = self.movie_dao.get_movie(mid)
        if not movie:
            print(f"Фильм с id {mid}  не найден!")
        return movie

    def create_movie(self, data):
        return self.movie_dao.create_movie(data)

    def update_movie(self, data):
        mid = data.get("id")
        movie = self.get_movie(mid)

        if movie:
            movie.title = data.get("title")
            movie.description = data.get("description")
            movie.trailer = data.get("trailer")
            movie.year = data.get("year")
            movie.rating = data.get("rating")
            movie.genre_id = data.get("genre_id")
            movie.director_id = data.get("director_id")

            self.movie_dao.update_movie(movie)
        else:
            print(f"Фильм с id {mid}  не найден!")

    def delete_movie(self, mid):
        movie = self.get_movie(mid)
        if movie:
            self.movie_dao.delete_movie(mid)
        else:
            print(f"Фильм с id {mid}  не найден!")
