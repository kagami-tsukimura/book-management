# flake8: noqa: E402
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)

from services.config import get_settings

DATABASE_URL = get_settings().database_url

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
