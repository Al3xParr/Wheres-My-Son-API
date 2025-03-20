from sqlalchemy.orm import Session
from .. import models, schemas


def create_location(db: Session, location: schemas.LocationCreate) -> schemas.Location:
    db_location = models.Location(time = location.time, lat = location.lat, long=location.long)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def get_location(db: Session, location_id: int) -> schemas.Location:
    return db.query(models.Location).get(location_id)

def delete_location(db: Session, location_id: int) -> bool:
    db_location = db.query(models.Location).get(location_id)
    if not db_location:
        return False
    db.delete(db_location)
    db.commit()
    db.refresh(db_location)
    return True

def get_all_locations(db: Session) -> list[schemas.Location]:
    return db.query(models.Location).order_by(models.Location.time).all()