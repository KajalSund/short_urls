import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_generate_hash(client):
    # Test generating hash for a URL
    response = client.post('/generate', json={'url': 'https://example.com/'})
    assert response.status_code == 200
    data = response.json
    assert 'hashed_url' in data
    assert 'token' in data

def test_get_original_url(client):
    # Test accessing original URL from hashed URL
    response = client.get('/9b07f10b96ef22dc217a0e1bb9a2d732f56e5e8001f69f6f33109c70d09f7680')
    assert response.status_code == 200
    data = response.json
    assert 'original_url' in data

def test_track_click(client):
    # Test tracking click on hashed URL
    response = client.get('/track/9b07f10b96ef22dc217a0e1bb9a2d732f56e5e8001f69f6f33109c70d09f7680/f22d5e22-8b5d-4472-84f1-3e460ae1a5f5')
    assert response.status_code == 200
    data = response.json
    assert 'message' in data



