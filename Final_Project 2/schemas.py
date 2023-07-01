from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Ad(BaseModel):

    class Config:
        orm_mode = True

    id: int
    title: str
    description: str
    listed_date: Optional[datetime] = Field(default_factory=datetime.now)
    seller: str
    price: int
    phone_number: str

class CreateAd(BaseModel):

    title: str
    description: str
    seller: str
    price: int
    phone_number: str

class DeleteAd(BaseModel):

    id: int