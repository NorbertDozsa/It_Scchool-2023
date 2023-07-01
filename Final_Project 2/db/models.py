from db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from datetime import datetime


class Ads(Base):
    __tablename__ = "ads"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    listed_date: Mapped[datetime]
    seller: Mapped[str]
    price: Mapped[int]
    phone_number: Mapped[str]

