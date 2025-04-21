from app import app, tasks
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def test_homepage(client):
    tasks.clear()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"My Tasks" in resp.data
