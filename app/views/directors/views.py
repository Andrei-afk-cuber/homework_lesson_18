from flask_restx import Namespace, Resource

from app.views.directors.model import Director, DirectorSchema
from app.setup_db import db

directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

# Класс для представления всех режиссеров
@directors_ns.route('/')
class DirectorsView(Resource):
    # Метод получения всех режиссеров
    def get(self):
        all_directors = db.session.query(Director).all()

        return directors_schema.dump(all_directors)

# Класс для работы с одним директором
@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    # Метод для получения конкретного директора
    def get(self, did):
        try:
            director = db.session.query(Director).filter(Director.id==did).one()

            return director_schema.dump(director), 200

        except Exception as e:
            return str(e), 400