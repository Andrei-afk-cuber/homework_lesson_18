import pytest

# import app: FLask
from main import app

# fixture for getting test app
@pytest.fixture
def test_app():
    return app.test_client()