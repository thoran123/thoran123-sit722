import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

# Mock the database before importing app
with patch('app.db.engine'):
    with patch('app.db.SessionLocal'):
        from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_health_check(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200

def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get('/')
    assert response.status_code == 200
