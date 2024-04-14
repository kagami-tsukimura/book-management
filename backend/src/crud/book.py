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


def find_by_id(db: Session, book_id: int) -> Book:
    """
    指定したIDの本を取得します。

    Args:
        db (Session): データベースセッション
        book_id (int): 取得する本のID

    Returns:
        Book: 指定したIDの本
    """

    return db.query(Book).filter(Book.book_id == book_id).first()


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


def update(db: Session, book_id: int, update_book: BookUpdate) -> Book:
    """
    本を更新します。

    Args:
        db (Session): データベースセッション
        update_book (BookUpdate): 更新する本
        book_id (int): 更新する本のID

    Returns:
        Book: 更新した本
    """

    target_book = find_by_id(db, book_id)

    if not target_book:
        raise HTTPException(status_code=404, details="Book not found.")

    target_book.title = update_book.title if update_book.title else target_book.title
    target_book.author = (
        update_book.author if update_book.author else target_book.author
    )
    target_book.genre_id = (
        update_book.genre_id if update_book.genre_id else target_book.genre_id
    )
    target_book.status = (
        update_book.status if update_book.status else target_book.status
    )

    db.add(target_book)
    db.commit()

    return target_book
