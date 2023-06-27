from sqlalchemy.orm import Session
from db import models
import schemas
from datetime import datetime


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def get_courses(db: Session):
    return db.query(models.Course).all()


def create_course(db: Session, course: schemas.CreateCourse):
    db_course = models.Course(
        name=course.name,
        description=course.description,
        listed_date=datetime.now(),
        start_date=course.start_date,
        trainer=course.trainer,
        seats=course.seats
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course