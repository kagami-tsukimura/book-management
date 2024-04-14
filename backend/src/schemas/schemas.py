from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class GenreCreate(BaseModel):
    main_genre_name: str = Field(max_length=255, examples=["プログラミング"])
    sub_genre_name: Optional[str] = Field(None, max_length=255, examples=["Python"])


class GenreUpdate(BaseModel):
    main_genre_name: str = Field(max_length=255, examples=["プログラミング"])
    sub_genre_name: Optional[str] = Field(None, max_length=255, examples=["Python"])


class GenreResponse(BaseModel):
    genre_id: int = Field(gt=0, examples=[1])
    main_genre_name: str = Field(max_length=255, examples=["プログラミング"])
    sub_genre_name: Optional[str] = Field(None, max_length=255, examples=["Python"])
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BookStatus(Enum):
    HAVE = "HAVE"
    WANT = "WANT"
    DONT_HAVE = "DONT_HAVE"


class BookCreate(BaseModel):
    title: str = Field(max_length=255, examples=["Effective Python"])
    author: str = Field(max_length=255, examples=["Brett Slatkin"])
    genre_id: int = Field(gt=0, examples=[1])


class BookUpdate(BaseModel):
    title: str = Field(max_length=255, examples=["Effective Python"])
    author: str = Field(max_length=255, examples=["Brett Slatkin"])
    genre_id: int = Field(gt=0, examples=[1])
