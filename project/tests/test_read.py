from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/items/primary", headers={"X-Token": "correcttoken"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "primary",
        "title": "Primary",
        "description": "The primary response",
    }


def test_read_item_bad_token():
    response = client.get("/items/primary", headers={"X-Token": "incorrecttoken"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid X-Token header",
    }

def test_read_inexistent_item():
    response = client.get("/items/unknown", headers={"X-Token": "correcttoken"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found",
    }

