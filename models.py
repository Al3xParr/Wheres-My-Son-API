from sqlalchemy import Float, Column, ForeignKey, Integer, String, DateTime
import datetime

from .database import Base


class Location(Base):
    __tablename__ = "Locations"

    id = Column(Integer, primary_key=True, nullable=False)
    time = Column(DateTime, unique=True, nullable=False)
    lat = Column(Float, unique=False, nullable=False)
    long = Column(Float, unique=False, nullable=False)
