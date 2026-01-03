from flask_restx import Namespace, Resource
from flask import request

from app.container import movie_service

# creating namespace for api
movies_ns = Namespace('movies')

# Class for processing a lot of movies
@movies_ns.route('/')
class MoviesView(Resource):
    # Get all movies method
    def get(self):
        data = request.args
        return movie_service.get_all(data), 200

    # Create movie method
    def post(self):
        json_data = request.json
        return movie_service.create(json_data), 201

# Class for processing movie
@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    # Get movie by id
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie

    # Update movie
    def put(self, mid):
        data = request.json
        data['mid'] = mid
        return movie_service.update(data), 201

    # Delete movie
    def delete(self, mid):
        return movie_service.delete(mid), 202