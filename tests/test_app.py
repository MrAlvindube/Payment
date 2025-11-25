from fastapi.testclient import TestClient

from app.main import app
from app.database import init_db


client = TestClient(app)


def setup_module(module):
    init_db()


def test_create_and_get_payment():
    payload = {"amount": 10.5, "currency": "usd", "description": "Test order"}
    response = client.post("/payments", json=payload)
    assert response.status_code == 201
    created_payment = response.json()
    assert created_payment["currency"] == "USD"
    payment_id = created_payment["id"]

    get_response = client.get(f"/payments/{payment_id}")
    assert get_response.status_code == 200
    fetched_payment = get_response.json()
    assert fetched_payment["id"] == payment_id


def test_authorize_capture_refund_flow():
    payload = {"amount": 5, "currency": "EUR", "description": "Flow test"}
    created = client.post("/payments", json=payload).json()
    payment_id = created["id"]

    authorize = client.post(f"/payments/{payment_id}/authorize")
    assert authorize.status_code == 200
    assert authorize.json()["status"] == "authorized"

    capture = client.post(f"/payments/{payment_id}/capture")
    assert capture.status_code == 200
    assert capture.json()["status"] == "captured"

    refund = client.post(f"/payments/{payment_id}/refund")
    assert refund.status_code == 200
    assert refund.json()["status"] == "refunded"


def test_invalid_refund_before_capture():
    payload = {"amount": 7, "currency": "GBP"}
    created = client.post("/payments", json=payload).json()
    payment_id = created["id"]

    refund = client.post(f"/payments/{payment_id}/refund")
    assert refund.status_code == 400
    assert refund.json()["detail"] == "Only captured payments can be refunded"
