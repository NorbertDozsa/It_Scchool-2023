from sqlalchemy.orm import Session
from db import models
import schemas
from datetime import datetime

def get_ad(db: Session, ad_id: int):
    """Returns the advertising with the given id"""
    return db.query(models.Ads).filter(models.Ads.id == ad_id).first()

def get_ads(db: Session):
    """Returns the full list of advertising"""
    return db.query(models.Ads).all()

def create_ad(db: Session, ad: schemas.CreateAd):
    """Creates a new advertising"""
    db_ad = models.Ads(
        title=ad.title,
        description=ad.description,
        listed_date=datetime.now(),
        seller=ad.seller,
        price=ad.price,
        phone_number=ad.phone_number
    )
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def delete_ad(db: Session, ad_id: int) -> bool:
    """Deletes the advertising with the given id"""
    ad = db.query(models.Ads).get(ad_id)
    if ad:
        db.delete(ad)
        db.commit()
        return True
    return False

def update_ad(db: Session, ad_id: int, ad_data: schemas.CreateAd):
    """Updates the advertising's data"""
    ad = db.query(models.Ads).get(ad_id)
    if ad:
        for field, value in ad_data.dict().items():
            setattr(ad, field, value)
        db.add(ad)
        db.commit()
        db.refresh(ad)
        return ad
    return None