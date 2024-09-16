
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    uId = Column(String(50), unique=True)
    fullName = Column(String(100), unique=False, nullable=False)
    phoneNumber = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    currentLocation =Column(String(100), unique=False, nullable=True)
    apiToken = Column(String(100), unique=True, nullable=True)
    accountStatus = Column(String(20), unique=False, nullable=True) #["active", "blocked", "timedOut"]
    accessToken = Column(String(100), unique=True, nullable=False)