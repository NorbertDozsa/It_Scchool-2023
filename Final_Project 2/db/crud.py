from sqlalchemy.orm import Session
from db.models import Adds
import schemas
from datetime import datetime

def get_add(db: Session, add_id: int):
    return db.query(Adds).filter(Adds.id == add_id).first()

def get_adds(db: Session):
    return db.query(Adds).all()

def create_add(db: Session, add: schemas.CreateAdd) -> Adds:
    db_add = Adds(
        title=Adds.title,
        description=Adds.description,
        listed_date=datetime.now(),
        seller=Adds.seller,
        price=Adds.price,
        phone_number=Adds.phone_number
    )
    db.add(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add

def delete_add(db: Session, add: schemas.DeleteAdd):
    db_add = Adds(
        title=Adds.title,
        description=Adds.description,
        seller=Adds.seller,
        price=Adds.price,
        phone_number=Adds.phone_number
    )
    db.delete(db_add)
    db.commit()
    db.refresh(db_add)
    return db_add