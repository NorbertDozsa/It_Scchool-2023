from pydantic import BaseModel
from datetime import datetime


class GreetResponse(BaseModel):

    greet_msg: str
    name:str

class Course(BaseModel):

    name: str
    description: str
    listed_date: datetime = datetime.now()
    start_date: datetime
    trainer: str
    seats: int
