from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class GreetResponse(BaseModel):

    greet_msg: str
    name: str


class Course(BaseModel):

    class Config:
        orm_mode = True

    id: int
    name: str
    description: str
    listed_date: Optional[datetime] = Field(default_factory=datetime.now)
    start_date: datetime
    trainer: str
    seats: int = Field(default=0, description="The number of seats available")

class CoursePatch(BaseModel):
    seats: int


class CreateCourse(BaseModel):

    name: str
    description: str
    start_date: datetime
    trainer: str
    seats: int = Field(default=0, description="The number of seats available")