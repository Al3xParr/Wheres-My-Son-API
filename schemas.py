from pydantic import BaseModel
from datetime import datetime


class LocationBase(BaseModel):
    time: datetime
    long: float
    lat: float

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

