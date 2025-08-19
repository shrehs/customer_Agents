import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_home_endpoint():
    """Test the home endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the AI Medical Appointment System"}


def test_doctors_endpoint():
    """Test the doctors endpoint."""
    response = client.get("/doctors/")
    assert response.status_code == 200
    assert "doctors" in response.json()


def test_health_check():
    """Test application health."""
    response = client.get("/")
    assert response.status_code == 200
    
    
def test_invalid_endpoint():
    """Test invalid endpoint returns 404."""
    response = client.get("/invalid-endpoint")
    assert response.status_code == 404