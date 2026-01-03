from typing import Optional, List, Union, Dict

from app.setup_db import db
from app.dao.models.genres_model import Genre, GenreSchema

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

# DAO for genres
class GenreDAO:
    def __init__(self, session: db.session) -> None:
        self.session = session

    # method for getting all genres
    def get_all(self) -> Optional[List[Genre]]:
        return self.session.query(Genre)

    # method for getting genre by id
    def get_one(self, gid: int) -> Union[str, Dict[str, str]]:
        try:
            genre = self.session.query(Genre).filter(Genre.id == gid).one()

            return genre
        except Exception as e:
            return str(e)