from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "environment": "production"}

def test_prediction_endpoint_positive_class():

    test_payload = {
        "feature_one": 0.8,
        "feature_two": 0.7
    }
    response = client.post("/predict", json=test_payload)
    assert response.status_code == 200
    
    data = response.json()
    assert data["prediction"] == 1
    assert "probability" in data

def test_prediction_endpoint_negative_class():

    test_payload = {
        "feature_one": 0.1,
        "feature_two": 0.2
    }
    
    response = client.post("/predict", json=test_payload)
    assert response.status_code == 200
    
    data = response.json()
    assert data["prediction"] == 0
    assert data["probability"] >= 0.0