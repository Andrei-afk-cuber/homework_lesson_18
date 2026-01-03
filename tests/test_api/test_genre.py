# class for testing /genres/ and /genres/<id>
class TestGenreView:
    def test_get_all(self, test_app) -> None:
        response = test_app.get('/genres/')
        assert response.status_code == 200

    def test_get_one(self, test_app) -> None:
        response = test_app.get('/genres/1')
        assert response.status_code == 200

    def test_get_not_exist(self, test_app) -> None:
        response = test_app.get('/genres/0')
        assert response.status_code == 404
        response = test_app.get('/genres/20')
        assert response.status_code == 404