from sqlalchemy.orm import Session
from db import models
import schemas
from datetime import datetime

def get_add(db: Session, add_id: int):
    return db.query(models.Adds).filter(models.Adds.id == add_id).first()

def get_adds(db: Session):
    return db.query(models.Adds).all()

def create_add(db: Session, add: schemas.CreateAdd):
    db_add = models.Adds(
        title=add.title,
        description=add.description,
        listed_date=datetime.now(),
        seller=add.seller,
        price=add.price,
        phone_number=add.phone_number
    )
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add

def delete_add(db: Session, add: schemas.DeleteAdd):
    db_add = models.Adds(
        title=add.title,
        description=add.description,
        seller=add.seller,
        price=add.price,
        phone_number=add.phone_number
    )
    db.delete(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add