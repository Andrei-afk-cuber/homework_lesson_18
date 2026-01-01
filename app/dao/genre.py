from app.setup_db import db
from app.dao.models.genres_model import Genre, GenreSchema

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

# DAO получения фильмов
class GenreDAO:
    def __init__(self, session: db.session):
        self.session = session

    # метод получения всех фильмов
    def get_all(self):
        return self.session.query(Genre)

    # Метод получения одного фильма
    def get_one(self, gid):
        try:
            genre = self.session.query(Genre).filter(Genre.id == gid).one()

            return genre
        except Exception as e:
            return str(e)