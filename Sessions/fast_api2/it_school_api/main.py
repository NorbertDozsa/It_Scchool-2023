import logging
from datetime import datetime
from typing import List

from db import crud
from db.base import Base, SessionLocal, engine
from fastapi import Depends, FastAPI
from fastapi.exceptions import HTTPException
from schemas import Course, CoursePatch, CreateCourse, GreetResponse
from sqlalchemy.orm import Session

# logging.root.setLevel(logging.INFO)
logging.basicConfig(
    filename="log.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


# Debug
# Info
# Warning
# Error
# Critical

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get("/hello")
def read_root():
    return {
        "greet_msg": "Hello",
        "name": "George"
    }


@app.get("/hello/{name}")
def greet_user(name: str) -> GreetResponse:
    """Get a greeting message and user name."""
    logging.debug("Hello method called.")
    logging.info("Hello method called.")
    logging.warning("Hello method called.")
    logging.error("Hello method called.")
    logging.critical("Hello method called.")
    return GreetResponse(greet_msg="Hello", name=name.title())


@app.get("/courses")
def list_courses(db: Session = Depends(get_db)) -> List[Course]:
    return crud.get_courses(db)


@app.get("/courses/{id}")
def course_detail(id: int, db: Session = Depends(get_db)) -> Course:
    db_course = crud.get_course(db, id)
    if db_course:
        return db_course
    raise HTTPException(status_code=404, detail="Course not found")


@app.post("/courses", status_code=201)
def create_course(course: CreateCourse, db: Session = Depends(get_db)) -> Course:
    db_course = crud.create_course(db, course)
    return db_course


# @app.put("/courses/{id}")
# def update_course(id: int, course: Course) -> Course:
#     for i, v in enumerate(external_data):
#         if v.id == id:
#             external_data[i] = course
#             return external_data[i]
#     raise HTTPException(status_code=404, detail="Course not found")


# @app.patch("/courses/{id}")
# def update_course_seats(id: int, data: CoursePatch) -> Course:
#     for i, v in enumerate(external_data):
#         if v.id == id:
#             external_data[i].seats = data.seats
#             return external_data[i]
#     raise HTTPException(status_code=404, detail="Course not found")


# @app.delete("/courses/{id}")
# def delete_course(id: int):
#     for i, v in enumerate(external_data):
#         if v.id == id:
#             del external_data[i]
#             return {"deleted": True}
#     raise HTTPException(status_code=404, detail="Course not found")
