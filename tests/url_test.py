import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_generate_hash(client):
    # Test generating hash for a URL
    response = client.post('/generate', json={'url': 'https://www.mongodb.com/solutions/use-cases/artificial-intelligence?utm_content=gdn-genairev&utm_source=gdn&utm_campaign=display_gd_pl_evergreen_atlas_general-incspend_retarget_mad_ww-in-kh_dev_desktop_eng_lead&utm_term=remarketing&utm_medium=display&utm_ad=aud-298632300231&utm_ad_campaign_id=21147741000&adgroup=162179116202&cq_cmp=21147741000&gclid=EAIaIQobChMI48ndjcKLhgMVfVKdCR0x0g9XEAEYASAAEgKu9PD_BwE'})
    assert response.status_code == 200
    data = response.json
    assert 'hashed_url' in data
    assert 'token' in data


def test_get_original_url(client):
    # Test accessing original URL from hashed URL
    response = client.get('/2adb05b46e6b2eb517a6184dab192812775f20b22d836a38be854a0d8d11df28')
    assert response.status_code == 200
    data = response.json
    assert 'original_url' in data


def test_track_click(client):
    # Test tracking click on hashed URL
    response = client.get('/track/2adb05b46e6b2eb517a6184dab192812775f20b22d836a38be854a0d8d11df28/bb26667d-37f9-4b47-b7ca-613894211339')
    assert response.status_code == 200
    data = response.json
    assert 'message' in data
