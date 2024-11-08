from app.dao.model.movie import Movies
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from sqlalchemy.orm import Session


class MovieDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movies).all()

    def get_movie(self, mid):
        movie = self.session.query(Movies).get(mid)
        if not movie:
            return None
        return movie

    def get_all_movies_by_director(self, did):
        return (
            self.session.query(Movies.title)
            .join(Director).filter(Director.id == did)
        ).all()

    def get_all_movies_by_genre(self, gid):
        return (
            self.session.query(Movies.title)
            .join(Genre).filter(Genre.id == gid).all()
        )

    def get_all_movies_by_year(self, year):
        return (
            self.session.query(Movies.title)
            .filter(Movies.year == year).all()
        )

    def create_movie(self, data):
        movie = Movies(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update_movie(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete_movie(self, mid):
        movie = self.get_movie(mid)

        self.session.delete(movie)
        self.session.commit()
