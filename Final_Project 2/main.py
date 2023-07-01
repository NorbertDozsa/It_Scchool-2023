from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.schema import MetaData
from typing import List
from db import crud
from db.base import SessionLocal, engine, Base
from schemas import Ad, CreateAd, DeleteAd
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



@app.get("/ads")
def list_ads(db: Session = Depends(get_db)) -> List[Ad]:
    """Lists all the ads from the database. """
    logging.info("Ads listed successfully!")
    try:
        return crud.get_ads(db)
    except HTTPException as err:
        print(err)
        


@app.get("/ads/{id}")
def get_ad(id: int, db:Session = Depends(get_db)) -> Ad:
    """Lists the detailed advertising with the given id"""
    db_ad = crud.get_ad(db, id)
    if db_ad:
        logging.info(f"Ad {id} listed successfully!")
        return db_ad
    raise HTTPException(status_code=404, detail="Add not found!")


@app.post("/ads", status_code=201)
def create_ad(ad: CreateAd, db: Session = Depends(get_db)) -> Ad:
    """Creates a new advertising in the database"""
    db_ad = crud.create_ad(db, ad)
    logging.info(f"Ad created successfully!")
    return db_ad
    
@app.delete("/ads/{id}")
def delete_ad(id: int, db: Session = Depends(get_db)) -> DeleteAd:
    """Deletes the advertising with the given id"""
    success = crud.delete_ad(db, id)
    if success:
        logging.info(f"Ad {id} deleted successfully!")
        return {"message": "Ad deleted"}
    raise HTTPException(status_code=404, detail="Ad not found!")

@app.put("/ads/{id}")
def update_ad(id: int, ad: CreateAd, db: Session = Depends(get_db)) -> Ad:
    """Updates the advertising with the given id"""
    db_ad = crud.update_ad(db, id, ad)
    if db_ad:
        logging.info(f"Ad {id} updated successfully!")
        return db_ad
    raise HTTPException(status_code=404, detail="Ad not found!")
