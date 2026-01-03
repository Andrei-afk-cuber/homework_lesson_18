from app.setup_db import db
from app.dao.models.directors_model import Director

# DAO for directors
class DirectorDAO:
    def __init__(self, session: db.session):
        self.session = session

    # метод получения всех фильмов
    def get_all(self):
        return self.session.query(Director).all()

    # Метод получения одного фильма
    def get_one(self, did):
        try:
            director = self.session.query(Director).filter(Director.id == did).one()

            return director
        except Exception as e:
            return str(e)