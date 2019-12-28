import pytest
from portfolio_app.portfolio import start_app


@pytest.fixture
def client():
    app = start_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    yield app


def test_homepage(client):
    with client.test_client() as c:
        rv = c.get('/')
        assert rv.status_code == 200


@pytest.mark.skip
def test_home(selenium):
    selenium.get('http://127.0.0.1:5000')
    assert "Luca Melis" in selenium.title
