# flake8: noqa: E402
import os
import sys

import pytest

current_dir = os.path.join(os.path.dirname(__file__), "../../")
sys.path.append(current_dir)

from database.database import get_db
from fastapi.testclient import TestClient
from main import app
from models import Book, Genre
from sqlalchemy.orm import Session


@pytest.fixture()
def session_fixture(session: Session):
    """
    url: sqliteを指定してメモリ上で動作
    """

    db = session

    try:
        genre1 = Genre(main_genre_name="IT", sub_genre_name="Python")
        genre2 = Genre(main_genre_name="IT", sub_genre_name="Rust")
        book1 = Book(title="Effective Python", author="Python Slatkin", genre_id=1)
        book2 = Book(title="Effective Java", author="Java Slatkin", genre_id=2)
        db.add(genre1)
        db.add(genre2)
        db.add(book1)
        db.add(book2)
        db.commit()
        yield db
    finally:
        db.close()


@pytest.fixture()
# fixtureで別のfixtureを呼び出せる
def client_fixture(session_fixture: Session):
    def override_get_db():
        return session_fixture

    # appオブジェクトで使用するget_dbを今回のsqliteで上書き
    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)
    yield client

    # 上書きしたDIを戻す
    app.dependency_overrides.clear()
