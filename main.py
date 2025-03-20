from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from . import schemas, models
from .database import SessionLocal, engine

from .CRUD import locations

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def get_root():
    return {"Hello": "World"}

@app.post("/location", response_model=schemas.Location)
def add_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    db_location = locations.create_location(db, location)
    if not db_location:
        raise HTTPException(status_code=404, detail="Unable To Create Location")
    
    return db_location

@app.delete("/location", response_model=bool)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = locations.delete_location(db, location_id=location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="No Location Found")
    return True


@app.get("/location", response_model= schemas.Location)
def get_location(location_id: int, db: Session = Depends(get_db)):
    db_location = locations.get_location(db, location_id=location_id)
    
    if db_location is None:
        raise HTTPException(status_code=404, detail="No Location Found")

    return db_location

@app.get("/location_all", response_model= list[schemas.Location])
def get_all_locations(db: Session = Depends(get_db)):

    db_locations = locations.get_all_locations(db)

    if db_locations is None:
        raise HTTPException(status_code=404, detail="No Locations Found")
    
    return db_locations