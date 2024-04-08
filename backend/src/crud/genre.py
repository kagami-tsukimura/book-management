# flake8: noqa: E402
import os
import sys
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)

from models import Genre
from schemas.schemas import GenreCreate, GenreUpdate


def find_all(db: Session) -> List[Genre]:
    """
    全てのジャンルを取得します。

    Args:
        db (Session): データベースセッション

    Returns:
        List[Genre]: 取得した全ジャンルのリスト
    """

    return db.query(Genre).order_by(Genre.genre_id).all()


def find_by_id(db: Session, genre_id: int) -> Genre:
    """
    指定したIDのジャンルを取得します。

    Args:
        db (Session): データベースセッション
        genre_id (int): 取得するジャンルのID

    Returns:
        Genre: 指定したIDのジャンル
    """

    return db.query(Genre).filter(Genre.genre_id == genre_id).first()


def find_by_name(db: Session, main_genre_name: str) -> List[Genre]:
    """
    指定した名前のジャンルを部分一致で取得します。

    Args:
        db (Session): データベースセッション
        main_genre_name (str): 取得するジャンル名

    Returns:
        Genre: 指定した名前のジャンル
    """

    return (
        db.query(Genre)
        .filter(Genre.main_genre_name.contains(main_genre_name))
        .order_by(Genre.genre_id)
        .all()
    )


def create(db: Session, create_genre: GenreCreate) -> Genre:
    """
    ジャンルを新規登録します。

    Args:
        db (Session): データベースセッション
        create_genre (GenreCreate): 登録するジャンル

    Returns:
        Genre: 登録したジャンル
    """

    new_genre = Genre(**create_genre.model_dump())
    db.add(new_genre)
    db.commit()

    return new_genre


def update(db: Session, genre_id: int, update_genre: GenreUpdate) -> Genre:
    """
    ジャンルを更新します。

    Args:
        db (Session): データベースセッション
        update_genre (GenreCreate): 更新するジャンル
        genre_id (int): 更新するジャンルのID

    Returns:
        Genre: 更新したジャンル
    """

    target_genre = find_by_id(db, genre_id)

    if not target_genre:
        raise HTTPException(status_code=404, details="Genre not found.")

    target_genre.main_genre_name = (
        update_genre.main_genre_name
        if update_genre.main_genre_name
        else target_genre.main_genre_name
    )
    target_genre.sub_genre_name = (
        update_genre.sub_genre_name
        if update_genre.sub_genre_name
        else target_genre.sub_genre_name
    )

    db.add(target_genre)
    db.commit()

    return target_genre


def delete(db: Session, genre_id: int) -> Genre:
    """
    ジャンルを削除します。

    Args:
        db (Session): データベースセッション
        genre_id (int): 削除するジャンルのID

    Returns:
        Genre: 削除したジャンル
    """

    target_genre = find_by_id(db, genre_id)

    if not target_genre:
        raise HTTPException(status_code=404, details="Genre not found.")

    db.delete(target_genre)
    db.commit()

    return target_genre
