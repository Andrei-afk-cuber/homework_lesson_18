import pytest
from unittest.mock import MagicMock

from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO

from app.dao.models.directors_model import Director
from app.dao.models.genres_model import Genre
from app.dao.models.movies_model import Movie

from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService

# fixture for get mocked director dao
@pytest.fixture
def director_dao():
    dao = DirectorDAO(None)
    dao.get_all = MagicMock(return_value=[Director(id=1, name="Director 1"), Director(id=2, name="Director 2")])
    dao.get_one = MagicMock(return_value=Director(id=1, name="Director 1"))
    return dao

# fixture for get mocked genre dao
@pytest.fixture
def genre_dao():
    dao = GenreDAO(None)
    dao.get_all = MagicMock(return_value=[Genre(id=1, name="Genre 1"), Genre(id=2, name="Genre 2")])
    dao.get_one = MagicMock(return_value=Genre(id=1, name="Genre 1"))
    return dao

# fixture for get mocked movie dao
@pytest.fixture
def movie_dao():
    dao = MovieDAO(None)
    dao.get_all = MagicMock(
        return_value=[
            Movie(id=1),
            Movie(id=2),
        ]
    )
    dao.get_one = MagicMock(return_value=Movie(id=1, title="Movie 1"))
    dao.update = MagicMock()
    dao.delete = MagicMock(return_value="Obj was deleted")
    return dao

# fixture for get director service
@pytest.fixture
def director_service(director_dao):
    return DirectorService(director_dao)

# fixture for get genre service
@pytest.fixture
def genre_service(genre_dao):
    return GenreService(genre_dao)

# fixture for get movie service
@pytest.fixture
def movie_service(movie_dao):
    service = MovieService(movie_dao)
    return service