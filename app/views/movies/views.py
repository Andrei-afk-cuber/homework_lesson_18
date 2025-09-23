from flask_restx import Namespace, Resource
from flask import request

from app.setup_db import db
from app.views.movies.model import Movie, MovieSchema

movies_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

# Класс обработки данных всех фильмов
@movies_ns.route('/')
class MoviesView(Resource):
    # Метод получения всех фильмов
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")

        # Условие на все фильмы
        movies = Movie.query

        if director_id:
            # Фильтруем фильмы по режиссеру
            movies = movies.filter(Movie.director_id == director_id)
        if genre_id:
            # Фильтруем фильмы по жанру
            movies = movies.filter(Movie.genre_id == genre_id)
        if year:
            # Фильтруем фильмы по году
            movies = movies.filter(Movie.year == year)

        # Получаем все фильмы
        movies = movies.all()

        return movies_schema.dump(movies)

    # Метод создания фильма
    def post(self):
        json_data = request.json
        movie = Movie(**movie_schema.load(json_data))

        with db.session.begin():
            db.session.add(movie)

# Класс обработки данных одного фильма
@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    # Метод получения фильма по его id
    def get(self, mid):
        try:
            movie = db.session.query(Movie).filter(Movie.id==mid).one()

            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 400


    # Метод полного изменения информации о фильме
    def put(self, mid):
        json_data = request.json
        movie = db.session.query(Movie).get(mid)

        movie.title = json_data.get("title")
        movie.description = json_data.get("description")
        movie.trailer = json_data.get("trailer")
        movie.year = json_data.get("year")
        movie.rating = json_data.get("rating")
        movie.genre_id = json_data.get("genre_id")
        movie.director_id = json_data.get("director_id")

        db.session.add(movie)
        db.session.commit()

    # Метод для удаления данных о фильме
    def delete(self, mid):
        movie = db.session.query(Movie).get(mid)
        try:
            db.session.delete(movie)
            db.session.commit()
        except Exception as e:
            return str(e), 400