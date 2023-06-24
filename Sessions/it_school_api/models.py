from db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from datetime import datetime

class Course(Base):

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str]
    listed_date: Mapped[datetime]
    trainer: Mapped[str]
    seats: Mapped[int]
    