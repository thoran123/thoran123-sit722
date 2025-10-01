import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200

def test_get_products(client):
    """Test get all products endpoint"""
    response = client.get('/products')
    assert response.status_code == 200
    assert isinstance(response.json, list)