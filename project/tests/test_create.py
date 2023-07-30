from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "correcttoken"},
        json={
            "id": "third",
            "title": "Third",
            "description": "The third data point",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "third",
        "title": "Third",
        "description": "The third data point",
    }


def test_create_item_bad_token():
    response = client.post(
        "/items/",
        headers={"X-Token": "incorrecttoken"},
        json={
            "id": "third",
            "title": "Third",
            "description": "The third data point",
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid X-Token header",
    }


def test_create_existent_item():
    response = client.post(
        "items/",
        headers={"X-Token": "correcttoken"},
        json={
            "id": "secondary",
            "title": "Secondary",
            "description": "The secondary response",
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Item already exists",
    }
