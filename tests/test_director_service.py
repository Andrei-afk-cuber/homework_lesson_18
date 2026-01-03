# class for testing director service
class TestDirectorService:
    def test_get_all(self, director_service) -> None:
        directors = director_service.get_all()
        assert len(directors) == 2
        assert directors[0]['id'] == 1

    def test_get_one(self, director_service) -> None:
        director = director_service.get_one(1)
        assert director['id'] == 1
        assert set(director.keys()).issubset({'id', 'name'})

