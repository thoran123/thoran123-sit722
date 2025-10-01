import pytest # type: ignore
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
    assert response.json == {'status': 'healthy'}

def test_get_customers(client):
    """Test get all customers endpoint"""
    response = client.get('/customers')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_customer(client):
    """Test create customer endpoint"""
    customer_data = {
        'name': 'Test Customer',
        'email': 'test@example.com'
    }
    response = client.post('/customers', json=customer_data)
    assert response.status_code in [200, 201]