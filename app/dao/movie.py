from typing import List, Optional, Union, Dict

from app.setup_db import db
from app.dao.models.movies_model import Movie

# DAO for movie
class MovieDAO:
    def __init__(self, session: db.session):
        self.session = session

    # Method for getting all movies
    def get_all(self, query: dict) ->Optional[List[Movie]]:
        director_id = query.get("director_id")
        genre_id = query.get("genre_id")
        year = query.get("year")

        movies = db.session.query(Movie)

        if director_id:
            movies = movies.filter(Movie.director_id==director_id)
        if genre_id:
            movies = movies.filter(Movie.genre_id==genre_id)
        if year:
            movies = movies.filter(Movie.year==year)

        return movies.all()

    # Method for getting one movie
    def get_one(self, mid: int) -> Union[str, Dict[str, str]]:
        try:
            movie = self.session.query(Movie).filter(Movie.id == mid).one()

            return movie
        except Exception as e:
            return str(e)

    # Method for create movie
    def create(self, movie: Movie) -> None:
        with self.session.begin():
            self.session.add(movie)
            self.session.commit()

    # Method for update movie data
    def update(self, movie: Movie) -> None:
        self.session.add(movie)
        self.session.commit()

    # Method for deleting movie
    def delete(self, movie: Movie) -> Optional[str]:
        try:
            self.session.delete(movie)
            self.session.commit()
        except Exception as e:
            return str(e)