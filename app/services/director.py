from app.dao.models.directors_model import DirectorSchema

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

class DirectorService:
    def __init__(self, director_dao):
        self.dao = director_dao

    def get_all(self):
        return directors_schema.dump(self.dao.get_all())

    def get_one(self, did):
        try:
            director = self.dao.get_one(did)

            if type(director) == str:
                raise Exception('Director not found')

            return director_schema.dump(director)
        except Exception as e:
            return str(e), 404