from db.base import Base, engine
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from datetime import datetime


class Adds(Base):
    __tablename__ = "adds"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    listed_date: Mapped[datetime]
    seller: Mapped[str]
    price: Mapped[int]
    phone_number: Mapped[str]