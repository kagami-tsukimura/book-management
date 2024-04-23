# flake8: noqa: E402
import os
import sys

current_dir = os.path.join(os.path.dirname(__file__), "../")
sys.path.append(current_dir)

import pytest
from models import Base, Genre
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


@pytest.fixture()
def session():
    """
    テストのためのセッションオブジェクトを作成するfixtureです。

    戻り値:
        Session: データベースとのやりとりに使用するセッションオブジェクトです。
    """

    engine = create_engine(
        url="sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    # modelsで定義したテーブルをDBに作成
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal()


# @pytest.fixture()
# def session_fixture(session: pytest.Session):
#     """
#     url: sqliteを指定してメモリ上で動作
#     """

#     db = session

#     try:
#         genre1 = Genre(main_genre_name="IT", sub_genre_name="Python")
#         genre2 = Genre(main_genre_name="IT", sub_genre_name="Rust")
#         db.add(genre1)
#         db.add(genre2)
#         db.commit()
#         yield db
#     finally:
#         db.close()
