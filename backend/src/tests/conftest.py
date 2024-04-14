# flake8: noqa: E402
import os
import sys

current_dir = os.path.join(os.path.dirname(__file__), "../")
sys.path.append(current_dir)

import pytest
from database.database import get_db
from fastapi.testclient import TestClient
from main import app
from models import Base, Genre
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool


@pytest.fixture()
def session_fixture():
    """
    url: sqliteを指定してメモリ上で動作
    """
    engine = create_engine(
        url="sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    # modelsで定義したテーブルをDBに作成
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        genre1 = Genre(main_genre_name="IT", sub_genre_name="Python")
        genre2 = Genre(main_genre_name="IT", sub_genre_name="Rust")
        db.add(genre1)
        db.add(genre2)
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
    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)
    yield client

    # 上書きしたDIを戻す
    app.dependency_overrides.clear()
