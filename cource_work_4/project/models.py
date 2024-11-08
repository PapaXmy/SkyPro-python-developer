from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'
    name = Column(String(100), unique=True, nullable=False)

    users = relationship('User', back_populates='genres')


class Director(models.Base):
    __tablename__ = 'directors'
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'
    title = Column(String())
    description = Column(String())
    trailer = Column(String())
    year = Column(Integer())
    rating = Column(Integer())
    genre_id = Column(Integer())
    director_id = Column(Integer())

    favorite_movies = relationship('FavoriteMovie', back_populates='movies')


class User(models.Base):
    __tablename__ = 'users'
    email = Column(String(), unique=True, nullable=False)
    password = Column(String())
    name = Column(String())
    surname = Column(String())
    favorite_genre = Column(Integer(), ForeignKey('genres.id'))

    genres = relationship('Genre', back_populates='users')
    favorite_movies = relationship('FavoriteMovie', back_populates='users')


class FavoriteMovie(models.Base):
    __tablename__ = 'favorite_movies'
    name_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))

    users = relationship('User', back_populates='favorite_movies')
    movies = relationship('Movie', back_populates='favorite_movies')
