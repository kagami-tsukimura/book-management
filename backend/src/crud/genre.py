# flake8: noqa: E402
import os
import sys
from typing import List

from sqlalchemy.orm import Session

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)

from models import Genre


def find_all(db: Session) -> List[Genre]:
    """
    全てのジャンルを取得します。

    Args:
        db (Session): データベースセッション

    Returns:
        List[Genre]: 取得した全ジャンルのリスト
    """

    return db.query(Genre).order_by(Genre.genre_id).all()
