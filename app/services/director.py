from app.dao.models.directors_model import DirectorSchema

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

class DirectorService:
    def __init__(self, director_dao):
        self.dao = director_dao

    def get_all(self):
        return directors_schema.dump(self.dao.get_all())

    def get_one(self, mid):
        return director_schema.dump(self.dao.get_one(mid))