from fastapi.testclient import TestClient


def test_find_all(client_fixture: TestClient):
    response = client_fixture.get("/genre")
    assert response.status_code == 200
    genres = response.json()
    assert len(genres) == 2


def test_find_by_id_success(client_fixture: TestClient):
    response = client_fixture.get("/genre/1")
    assert response.status_code == 200
    genre = response.json()
    assert genre["genre_id"] == 1
    assert genre["main_genre_name"] == "IT"
    assert genre["sub_genre_name"] == "Python"


def test_find_by_id_failure(client_fixture: TestClient):
    response = client_fixture.get("/genre/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "Genre not found."


def test_find_by_name(client_fixture: TestClient):
    response = client_fixture.get("/genre/?main_genre_name=IT")
    assert response.status_code == 200
    genres = response.json()
    assert len(genres) == 2


def test_find_by_name_failure(client_fixture: TestClient):
    response = client_fixture.get("/genre/?main_genre_name=Network")
    assert response.status_code == 404
    assert response.json()["detail"] == "Genre not found."


def test_create(client_fixture: TestClient):
    response = client_fixture.post(
        "/genre", json={"main_genre_name": "教養", "sub_genre_name": "簿記"}
    )
    assert response.status_code == 201
    genre = response.json()
    assert genre["main_genre_name"] == "教養"
    assert genre["sub_genre_name"] == "簿記"


def test_update_success(client_fixture: TestClient):
    response = client_fixture.put(
        "/genre/1", json={"main_genre_name": "Device", "sub_genre_name": "Mouse"}
    )
    assert response.status_code == 200
    genre = response.json()
    assert genre["main_genre_name"] == "Device"
    assert genre["sub_genre_name"] == "Mouse"


def test_update_failure(client_fixture: TestClient):
    response = client_fixture.put(
        "/genre/10", json={"main_genre_name": "Device", "sub_genre_name": "Mouse"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Genre not found."
