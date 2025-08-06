import pytest
from fastapi.testclient import TestClient
from app.api.api import app

client = TestClient(app)

def test_create_customer():
    data = {
        "name": "John Doe",
        "engagement_score": 0.8,
        "claim_count": 2,
        "payment_history_score": 0.9
    }
    response = client.post("/customers", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_customers():
    response = client.get("/customers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_predict_churn():
    data = {
        "name": "Jane Doe",
        "engagement_score": 0.5,
        "claim_count": 1,
        "payment_history_score": 0.6
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "churn_risk" in response.json()
