from flask_restx import Namespace, Resource

from app.container import director_service

# creating namespace for api
directors_ns = Namespace('directors')

# All director class
@directors_ns.route('/')
class DirectorsView(Resource):
    # Get all directors
    def get(self):
        return director_service.get_all()

# Class for working with one director
@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    # Get director by id
    def get(self, did: int):
        return director_service.get_one(did)