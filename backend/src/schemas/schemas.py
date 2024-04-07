from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class GenreCreate(BaseModel):
    main_genre_name: str = Field(max_length=255, examples=["プログラミング"])
    sub_genre_name: str = Field(max_length=255, examples=["Python"])


class GenereUpdate(BaseModel):
    main_genre_name: str = Field(max_length=255, examples=["プログラミング"])
    sub_genre_name: str = Field(max_length=255, examples=["Python"])


class GenereResponse(BaseModel):
    genre_id: int = Field(gt=0, examples=[1])
    main_genre_name: str = Field(max_length=255, examples=["プログラミング"])
    sub_genre_name: str = Field(max_length=255, examples=["Python"])
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
