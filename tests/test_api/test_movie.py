import pytest

# class for test /movies/
class TestMoviesView:
    def test_get_all(self, test_app) -> None:
        response = test_app.get('/movies/')
        assert response.status_code == 200

    def test_post(self, test_app) -> None:
        response = test_app.post('/movies/', json={"title":"New movie"})
        assert response.status_code == 201

    def test_post_with_error(self, test_app) -> None:
        with pytest.raises(TypeError):
            test_app.post('/movies/', json={"no_title":"New movie"})

# class for test /movies/<id>
class TestMovieView:
    def test_get_one(self, test_app) -> None:
        response = test_app.get('/movies/1')
        assert response.status_code == 200

    def test_get_by_incorrect_id(self, test_app) -> None:
        response = test_app.get('/movies/0')
        assert response.status_code == 404
        response = test_app.get('/movies/10')
        assert response.status_code == 404

    def test_put(self, test_app) -> None:
        response = test_app.put('/movies/1', json={"id":1, "title":"New movie"})
        assert response.status_code == 201

    def test_delete(self, test_app) -> None:
        response = test_app.delete('/movies/1')
        assert response.status_code == 202