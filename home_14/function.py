import sqlite3
import json


def get_movie_by_title(title):
    """Поиск фильма по его названию"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""SELECT title, country, release_year, listed_in, description
                          FROM netflix
                          WHERE title = '{title.title()}'
                          AND `type` = 'Movie'
                          ORDER BY release_year DESC
                          LIMIT 1

    """
        result = cursor.execute(query).fetchall()
        movie_dict = {}
        for movie in result:
            movie_dict = {
                "title": movie[0],
                "country": movie[1],
                "release_year": movie[2],
                "genre": movie[3],
                "description": "".join(movie[4].split("\n")),
            }

        return movie_dict


def get_movies_by_year_release(year_1, year_2):
    """Поиск фильмов по годам в диапазоне от year_1 до year_2"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {year_1} AND {year_2}
                    LIMIT 100
    """
        result = cursor.execute(query).fetchall()
        movie_list = []
        for movie in result:
            movie_dict = {"title": movie[0], "release_year": movie[1]}
            movie_list.append(movie_dict)

        return movie_list


def get_movie_by_rating(rating):
    """Поиск фильмов по рейтингу"""
    dict_rating = {
        "children": ("G", "G"),
        "family": ("G", "PG", "PG-13"),
        "adult": ("R", "NC-17"),
    }
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""SELECT title, rating, description
                    FROM netflix
                    WHERE `type` = 'Movie'
                    AND `type` NOT NULL
                    AND rating in {dict_rating.get(rating.lower(), ("R", "R"))}
                    LIMIT 100
    """

        result = cursor.execute(query).fetchall()
        movie_list = []
        for movie in result:
            movie_dict = {
                "title": movie[0],
                "rating": movie[1],
                "description": "".join(movie[2].split("\n")),
            }

            movie_list.append(movie_dict)

        return movie_list


def get_movie_by_genre(genre):
    """Поиск фильмов по жанру"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""SELECT title, description
                    FROM netflix
                    WHERE `type` = 'Movie'
                    AND `type` NOT NULL
                    AND listed_in like '%{genre.title()}%'
                    ORDER BY release_year DESC
                    LIMIT 10
    """
        result = cursor.execute(query).fetchall()
        movie_list = []
        for movie in result:
            movie_dict = {
                "title": movie[0],
                "description": "".join(movie[1].split("\n")),
            }

            movie_list.append(movie_dict)

        return movie_list


def get_actor_play_pair(actor_1, actor_2):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""SELECT `cast`
                    FROM netflix
                    WHERE `cast` like '%{actor_1}%'
                    AND `cast` LIKE '%{actor_2}%'
        """
        result = cursor.execute(query).fetchall()

        name_dict = {}
        for value in result:
            cast_list = value[0].split(",")
            names = set(cast_list) - {actor_1, actor_2}
            for name in names:
                name_dict[(name).strip()] = name_dict.get((name).strip(), 0) + 1

        result_list = []
        for name in name_dict:
            result_list.append((name, name_dict[name]))

        actor_list = [name for name, count in result_list if count >= 2]
        return actor_list


def get_movies_by_type_year_genre(type, year_release, genre):
    """Поиск фильмов по типу: сериал, кино, году выпуска, жанру"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""SELECT title, description
                    FROM netflix
                    WHERE "type" NOT NULL
                    AND "type" LIKE "%{type}%"
                    AND release_year = "{year_release}"
                    AND listed_in like "%{genre}%"
        """
        result = cursor.execute(query).fetchall()
        movie_list = []
        for movie in result:
            movie_dict = {
                "title": movie[0],
                "description": "".join(movie[1].split("\n")),
            }
            movie_list.append(movie_dict)
        return json.dumps(movie_list)


# print(get_movie_by_title("evolution"))
# print(get_movies_by_year_release(2000, 2007))
# print(get_movie_by_rating("NC-17"))
# print(get_movie_by_genre("Dramas"))
# print(get_actor_play_pair("Rose McIver", "Ben Lamb"))
print(get_movies_by_type_year_genre("TV Show", 2007, "Dramas"))
