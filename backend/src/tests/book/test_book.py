from fastapi.testclient import TestClient


def test_find_all(client_fixture: TestClient):
    response = client_fixture.get("/book")
    assert response.status_code == 200
    books = response.json()
    assert len(books) == 2
    assert books[0]["book_id"] == 1
    assert books[0]["title"] == "Effective Python"
    assert books[0]["author"] == "Python Slatkin"
    assert books[0]["genre_id"] == 1


def test_find_by_id_success(client_fixture: TestClient):
    response = client_fixture.get("/book/2")
    assert response.status_code == 200
    book = response.json()
    assert book["book_id"] == 2
    assert book["title"] == "Effective Java"
    assert book["author"] == "Java Slatkin"
    assert book["genre_id"] == 2


def test_find_by_id_failure(client_fixture: TestClient):
    response = client_fixture.get("/book/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found."


def test_create(client_fixture: TestClient):
    response = client_fixture.post(
        "/book",
        json={"title": "Effective Rust", "author": "Rust Slatkin", "genre_id": 1},
    )
    assert response.status_code == 201
    book = response.json()
    assert book["book_id"] == 3
    assert book["title"] == "Effective Rust"
    assert book["author"] == "Rust Slatkin"
    assert book["genre_id"] == 1
    response = client_fixture.get("/book")
    assert response.status_code == 200
    books = response.json()
    assert len(books) == 3


def test_update_success(client_fixture: TestClient):
    response = client_fixture.put(
        "/book/1", json={"title": "Beginner Python", "author": "Python Beginning"}
    )
    assert response.status_code == 200
    book = response.json()
    assert book["book_id"] == 1
    assert book["title"] == "Beginner Python"
    assert book["author"] == "Python Beginning"
    assert book["genre_id"] == 1
    response = client_fixture.get("/book")
    assert response.status_code == 200
    books = response.json()
    assert len(books) == 2


def test_update_failure(client_fixture: TestClient):
    response = client_fixture.put(
        "/book/10", json={"title": "Beginner Python", "author": "Python Beginning"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found."


def test_delete_success(client_fixture: TestClient):
    response = client_fixture.delete("/book/1")
    assert response.status_code == 200
    book = response.json()
    assert book["book_id"] == 1
    assert book["title"] == "Effective Python"
    assert book["author"] == "Python Slatkin"
    assert book["genre_id"] == 1
    response = client_fixture.get("/book")
    assert response.status_code == 200
    books = response.json()
    assert len(books) == 1


def test_delete_failure(client_fixture: TestClient):
    response = client_fixture.delete("/book/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found."
    response = client_fixture.get("/book")
    assert response.status_code == 200
    books = response.json()
    assert len(books) == 2
