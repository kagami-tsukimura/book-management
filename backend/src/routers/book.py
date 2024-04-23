# type: ignore
# flake8: noqa: E402
import os
import sys
from typing import List

from fastapi import APIRouter, HTTPException, Path, Query
from starlette import status

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)

from crud import book as book_cruds
from dependencies import Dependencies
from schemas.schemas import BookCreate, BookResponse, BookStatus, BookUpdate

dependencies = Dependencies()
DBDependency = dependencies.get_db_dependency()

router = APIRouter(prefix="/book", tags=["book"])


@router.get("", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
async def find_all(db: DBDependency):

    return book_cruds.find_all(db)


@router.get("/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
async def find_by_id(db: DBDependency, book_id: int = Path(gt=0)):
    found_book = book_cruds.find_by_id(db, book_id)

    if not found_book:
        raise HTTPException(status_code=404, detail="Book not found.")

    return found_book


@router.post("", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create(db: DBDependency, create_book: BookCreate):

    return book_cruds.create(db, create_book)


@router.put("/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
async def update(db: DBDependency, update_book: BookUpdate, book_id: int = Path(gt=0)):

    return book_cruds.update(db, book_id, update_book)


@router.delete(
    "/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK
)
async def delete(db: DBDependency, book_id: int = Path(gt=0)):

    return book_cruds.delete(db, book_id)
