from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.schema import MetaData
from typing import List
from db import crud
from db.base import SessionLocal, engine, Base
from schemas import Add, CreateAdd, DeleteAdd
import logging


logging.basicConfig(
    filename="log.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/adds")
def list_adds(db: Session = Depends(get_db)) -> List[Add]:
    logging.info("Adds listed successfully!")
    return crud.get_adds(db)


@app.get("/adds/{id}")
def get_add(id: int, db:Session = Depends(get_db)) -> Add:
    db_add = crud.get_add(db, id)
    if db_add:
        return db_add
    logging.info(f"Add {id} listed successfully!")
    raise HTTPException(status_code=404, detail="Add not found!")


@app.post("/adds", status_code=201)
def create_add(add: CreateAdd, db: Session = Depends(get_db)) -> Add:
    db_add = crud.create_add(db, add)
    logging.info(f"Add created successfully!")
    return db_add
    
@app.delete("/adds/{id}")
def delete_add(id: int, db: Session = Depends(get_db)) -> DeleteAdd:
    db_add = crud.delete_add(db, id)
    if db_add:
        logging.info(f"Add {id} deleted successfully!")
        return {"message": "Add deleted successfully!"}
    raise HTTPException(status_code=404, detail="Add not found!")
