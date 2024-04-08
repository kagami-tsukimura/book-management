# flake8: noqa: E402
import os
import sys
from typing import List

from fastapi import APIRouter, HTTPException, Path, Query
from starlette import status

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)

from crud import genre as genre_cruds
from dependencies import Dependencies
from schemas.schemas import GenreCreate, GenreResponse, GenreUpdate

dependencies = Dependencies()
DBDependency = dependencies.get_db_dependency()

router = APIRouter(prefix="/genre", tags=["genre"])


@router.get("", response_model=List[GenreResponse], status_code=status.HTTP_200_OK)
async def find_all(db: DBDependency):

    return genre_cruds.find_all(db)


@router.get("/{genre_id}", response_model=GenreResponse, status_code=status.HTTP_200_OK)
async def find_by_id(db: DBDependency, genre_id: int = Path(gt=0)):
    found_genre = genre_cruds.find_by_id(db, genre_id)
    if not found_genre:
        raise HTTPException(status_code=404, detail="Genre not found.")

    return found_genre


@router.get(
    "/",
    response_model=List[GenreResponse],
    status_code=status.HTTP_200_OK,
)
async def find_by_name(db: DBDependency, main_genre_name: str = Query(max_length=255)):
    found_genre = genre_cruds.find_by_name(db, main_genre_name)
    if not found_genre:
        raise HTTPException(status_code=404, detail="Genre not found.")

    return found_genre


@router.post("", response_model=GenreResponse, status_code=status.HTTP_201_CREATED)
async def create(db: DBDependency, create_genre: GenreCreate):

    return genre_cruds.create(db, create_genre)


@router.put("/{genre_id}", response_model=GenreResponse, status_code=status.HTTP_200_OK)
async def update(
    db: DBDependency, update_genre: GenreUpdate, genre_id: int = Path(gt=0)
):

    updated_genre = genre_cruds.update(db, genre_id, update_genre)
    if not updated_genre:
        HTTPException(status_code=404, details="Genre not updated.")

    return updated_genre


@router.delete(
    "/{genre_id}", response_model=GenreResponse, status_code=status.HTTP_200_OK
)
async def delete(db: DBDependency, genre_id: int = Path(gt=0)):

    deleted_genre = genre_cruds.delete(db, genre_id)
    if not deleted_genre:
        HTTPException(status_code=404, details="Genre not deleted.")

    return deleted_genre
