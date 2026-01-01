class TestGenreService:
    def test_get_all(self, genre_service):
        genres = genre_service.get_all()
        assert len(genres) > 0
        assert genres[0]['id'] == 1

    def test_get_one(self, genre_service):
        genre = genre_service.get_one(1)
        assert genre['id'] == 1
        assert set(genre.keys()).issubset(('id', 'name'))

