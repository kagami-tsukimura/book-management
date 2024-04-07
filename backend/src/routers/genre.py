# flake8: noqa: E402
import os
import sys
from typing import List

from fastapi import APIRouter
from starlette import status

parent_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parent_dir)

from crud import genre as genre_cruds
from dependencies import Dependencies
from schemas.schemas import GenereResponse

dependencies = Dependencies()
DBDependency = dependencies.get_db_dependency()

router = APIRouter(prefix="/genre", tags=["genre"])


@router.get("", response_model=List[GenereResponse], status_code=status.HTTP_200_OK)
async def find_all(db: DBDependency):
    return genre_cruds.find_all(db)
