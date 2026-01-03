from typing import Optional, List, Union, Tuple, Dict

from app.dao.models.movies_model import Movie, MovieSchema

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

# service class for movies
class MovieService:
    def __init__(self, movie_dao) -> None:
        self.dao = movie_dao

    def get_all(self, data=None) -> Optional[List[Movie]]:
        return movies_schema.dump(self.dao.get_all(data))

    def get_one(self, mid) -> Union[Dict[str, str], Tuple[str, int]]:
        try:
            movie = self.dao.get_one(mid)
            if type(movie) == str:
                raise TypeError

            return movie_schema.dump(movie)
        except Exception as e:
            return str(e), 404

    def create(self, data: dict) -> None:
        movie = Movie(**data)
        return self.dao.create(movie)

    def update(self, data: dict) -> None:
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

    def delete(self, mid: int) -> None:
        movie = self.dao.get_one(mid)
        return self.dao.delete(movie)