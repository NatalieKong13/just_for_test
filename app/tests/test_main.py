from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "2.0.0"}

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "The Pragmatic Programmer"},
        {"id": 2, "title": "Clean Code"}
    ]