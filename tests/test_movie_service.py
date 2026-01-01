import pytest


class TestMovieService:
    def test_get_all(self, movie_service):
        movies = movie_service.get_all()
        assert len(movies) > 0
        assert type(movies) == list
        assert movies[0]['id'] == 1

    def test_get_one(self, movie_service):
        movie = movie_service.get_one(1)
        assert type(movie) == dict
        assert set(movie.keys()) == {"id", "title", "description", "trailer", "year", "rating", "genre_id", "genre",
                                     "director_id", "director"}
        assert movie['id'] == 1

    def test_create(self, movie_service):
        with pytest.raises(TypeError):
            movie_service.create(1)

        with pytest.raises(TypeError):
            movie_service.create()

    def test_delete(self, movie_service):
        assert movie_service.delete(2) == "Obj was deleted"

        with pytest.raises(TypeError):
            movie_service.delete()