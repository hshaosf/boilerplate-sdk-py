# pylint: disable=redefined-outer-name
"""Tests for boilerplate/app.py"""
import json
import pytest
from falcon import testing
import examples.app

@pytest.fixture()
def client():
    """ client fixture """
    return testing.TestClient(examples.app.run())

def test_get_posts(client):
    """Test get_posts"""
    response = client.simulate_get('/page/get_posts')
    assert response.status_code == 200

    content = json.loads(response.content)

    assert content
    assert isinstance(content, list)

    response = content[0]
    # pylint: disable=line-too-long
    assert list(response.keys()) == ['userId', 'id', 'title', 'body']

def test_error(client):
    """Test error state"""
    response = client.simulate_get('/error')
    assert response.status_code == 404

def test_default_page(client):
    """Test default page"""
    response = client.simulate_get('/page/home')
    assert response.status_code == 200
