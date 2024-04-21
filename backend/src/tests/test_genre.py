from fastapi.testclient import TestClient


def test_find_all(client_fixture: TestClient):
    response = client_fixture.get("/genre")
    assert response.status_code == 200
    genres = response.json()
    assert len(genres) == 2
