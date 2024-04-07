from database.database import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql.functions import current_timestamp


class Genre(Base):
    __tablename__ = "genre_master"

    genre_id = Column(Integer, primary_key=True)
    main_genre_name = Column(String, unique=True, nullable=False)
    sub_genre_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(
        DateTime, default=current_timestamp(), onupdate=current_timestamp()
    )
