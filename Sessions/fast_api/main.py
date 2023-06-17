
from fastapi import FastAPI
from models import GreetResponse
from typing import List


app = FastAPI()

external_data = [
    Course(name="Python Online", description="Learn Python 3," start_date=datetime(2023, 12, 1))
]

class GreetResponse(BaseModel):

    greet_msg: str
    name:str

@app.get("/hello")
def read_root():
    return {
        "greet_msg": "Hello",
        "name": "George"
    }


@app.get("/items/{name}")
def read_item(name: str) -> GreetResponse:
    """Get a greeting message and user name."""
    return GreetResponse(greet_msg="hello", name=name.title())

@app.get("/courses")
def list_courses() -> List[Course]:
    return external_data