from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Numeric,Date
from sqlalchemy.orm import relationship
from .db import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key = True)
    username = Column(String(255),nullable = True)
    password = Column(String(255),nullable = True)


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer,primary_key = True)
    title = Column(Text, nullable = True, index = True)
    link = Column(Text, nullable = True, index = True)
    type = Column(Integer, nullable = True)
    push_date = Column(DateTime, nullable = True)
    content = Column(DateTime)
    source = Column(String(50), nullable = True)


class Locations(Base):
    __tablename__ = 'locations'

    location_id = Column(Integer,primary_key = True)
    region = Column(String(255), nullable = True)
    country = Column(String(255))
    latitude = Column(Numeric(9,6))
    longitude = Column(Numeric(9,6))

    weathers = relationship("Weather", back_populates="location")


class Weather(Base):
    __tablename__ = "weather"

    weather_id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey("locations.location_id"), nullable=False)
    type = Column(String(255), nullable=False)
    forecast_date = Column(Date, nullable=False)
    suggestion = Column(Text)

    location = relationship("Locations", back_populates="weathers")