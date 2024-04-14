from database.database import Base
from schemas.schemas import BookStatus
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.sql.functions import current_timestamp


class Genre(Base):
    __tablename__ = "genre_master"

    genre_id = Column(Integer, primary_key=True)
    main_genre_name = Column(String, nullable=False)
    sub_genre_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(
        DateTime, default=current_timestamp(), onupdate=current_timestamp()
    )


class Book(Base):
    __tablename__ = "book_master"

    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre_id = Column(
        Integer, ForeignKey("genre_master.genre_id", ondelete="CASCADE"), nullable=False
    )
    status = Column(Enum(BookStatus), nullable=False, default=BookStatus.DONT_HAVE)
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(
        DateTime, default=current_timestamp(), onupdate=current_timestamp()
    )
