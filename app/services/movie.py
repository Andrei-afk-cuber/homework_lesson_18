from app.dao.models.movies_model import Movie, MovieSchema

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

class MovieService:
    def __init__(self, movie_dao):
        self.dao = movie_dao

    def get_all(self, data=None):
        return movies_schema.dump(self.dao.get_all(data))

    def get_one(self, mid):
        return movie_schema.dump(self.dao.get_one(mid))

    def create(self, data):
        movie = Movie(**data)
        return self.dao.create(movie)

    def update(self, data):
        mid = data.get("mid")
        movie = self.dao.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        return self.dao.update(movie)

    def delete(self, mid):
        movie = self.dao.get_one(mid)
        return self.dao.delete(movie)