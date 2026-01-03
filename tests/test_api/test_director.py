# tests for /directors/
class TestDirectorsView:
    def test_get_all(self, test_app):
        response = test_app.get('/directors/')
        assert response.status_code == 200

    def test_get_one(self, test_app):
        response = test_app.get('/directors/1')
        assert response.status_code == 200

    def test_get_not_exist(self, test_app):
        response = test_app.get('/directors/0')
        assert response.status_code == 404
        response = test_app.get('/directors/5')
        assert response.status_code == 404