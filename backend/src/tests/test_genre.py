from fastapi.testclient import TestClient


def test_find_all(client_fixture: TestClient):
    response = client_fixture.get("/genre")
    assert response.status_code == 200
    genres = response.json()
    assert len(genres) == 2


def test_find_by_id(client_fixture: TestClient):
    response = client_fixture.get("/genre/1")
    assert response.status_code == 200
    genre = response.json()
    assert genre["genre_id"] == 1
    assert genre["main_genre_name"] == "IT"
    assert genre["sub_genre_name"] == "Python"


def test_find_by_name(client_fixture: TestClient):
    response = client_fixture.get("/genre/?main_genre_name=IT")
    assert response.status_code == 200
    genres = response.json()
    assert len(genres) == 2
