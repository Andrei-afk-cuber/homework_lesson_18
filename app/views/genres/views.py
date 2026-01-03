from flask_restx import Namespace, Resource

from app.container import genre_service

# creating namespace for api
genres_ns = Namespace('genres')

# All genres class
@genres_ns.route('/')
class GenresView(Resource):
    # Get all genres
    def get(self):
        return genre_service.get_all()

# One genre class
@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    # Get genre bu id
    def get(self, gid: int):
        return genre_service.get_one(gid)