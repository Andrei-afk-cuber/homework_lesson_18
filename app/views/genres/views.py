from flask_restx import Namespace, Resource
from flask import request

from app.views.genres.model import Genre, GenreSchema
from app.setup_db import db

genres_ns = Namespace('genres')

# Класс для представления всех жанров
@genres_ns.route('/')
class GenresView(Resource):
    # Метод получения жанров
    def get(self):
        all_genres = db.session.query(Genre).all()

        return GenreSchema(many=True).dump(all_genres), 200

# Класс для представления одного пользователя
@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    # Метод получения жанра
    def get(self, gid):
        try:
            genre = db.session.query(Genre).filter(Genre.id == gid).one()

            return GenreSchema().dump(genre), 200
        except Exception as e:
            return str(e), 400