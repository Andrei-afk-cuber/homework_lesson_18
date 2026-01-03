# class for testing genre service
class TestGenreService:
    def test_get_all(self, genre_service) -> None:
        genres = genre_service.get_all()
        assert len(genres) > 0
        assert genres[0]['id'] == 1

    def test_get_one(self, genre_service) -> None:
        genre = genre_service.get_one(1)
        assert genre['id'] == 1
        assert set(genre.keys()).issubset(('id', 'name'))

