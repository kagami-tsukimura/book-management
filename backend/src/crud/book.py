# flake8: noqa: E402
import os
import sys
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)

from models import Book
from schemas.schemas import BookCreate, BookUpdate


def find_all(db: Session) -> List[Book]:
    """
    全ての本を取得します。

    Args:
        db (Session): データベースセッション

    Returns:
        List[Book]: 取得した全本のリスト
    """

    return db.query(Book).order_by(Book.book_id).all()


def create(db: Session, create_book: BookCreate) -> Book:
    """
    本を新規登録します。

    Args:
        db (Session): データベースセッション
        create_book (BookCreate): 登録する本

    Returns:
        Book: 登録した本
    """

    new_book = Book(**create_book.model_dump())
    db.add(new_book)
    db.commit()

    return new_book
