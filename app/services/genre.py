from typing import Optional, List, Union, Tuple, Dict

from app.dao.models.genres_model import GenreSchema, Genre

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

# class for genre
class GenreService:
    def __init__(self, movie_dao) -> None:
        self.dao = movie_dao

    def get_all(self) -> Optional[List[Genre]]:
        return genres_schema.dump(self.dao.get_all())

    def get_one(self, mid: int) -> Union[Dict[str, str], Tuple[str, int]]:
        try:
            genre = self.dao.get_one(mid)

            if type(genre) == str:
                raise Exception('Genre is not found')

            return genre_schema.dump(self.dao.get_one(mid))
        except Exception as e:
            return str(e), 404