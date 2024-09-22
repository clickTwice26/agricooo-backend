from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    uId = Column(String(50), unique=True)
    fullName = Column(String(100), unique=False, nullable=False)
    phoneNumber = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=False, nullable=False)
    currentLocation =Column(String(100), unique=False, nullable=True)
    accountStatus = Column(String(20), unique=False, nullable=True) #["active", "blocked", "timedOut"]
    accessToken = Column(String(100), unique=True, nullable=False)
    accountCreationIp = Column(String(100), unique=False, nullable=True)
    clientDeviceInfo = Column(String(300), unique=False, nullable=True)
    lastAccessedIp = Column(String(100), unique=False, nullable=True)
    creationTime = Column(String(200), unique=False, nullable=True)
    fields = Column(Text, unique=False, nullable=True, default="[]")

class ApiToken(Base):
    __tablename__ = 'apiToken'
    id = Column(Integer, primary_key=True)
    uId = Column(String(50), unique=True)
    creationTime = Column(String(100), nullable=True)
    tokenStr = Column(String(100), unique=True, nullable=False)
    expireTime = Column(String(100), nullable=True)
    threshold = Column(Integer, nullable=False, default=60) #per 60 seconds
    tokenLevel = Column(Integer, nullable=False, default=3)
    requestLimit = Column(Integer, nullable=False, default=10000)
    useCount = Column(Integer, nullable=False, default=0)


class aiResponse(Base):
    __tablename__ = 'aiResponse'
    id = Column(Integer, primary_key=True)
    accessToken = Column(String(100), unique=False, nullable=False)
    chatId = Column(String(100), unique=False, nullable=True)
    creationTime = Column(String(200), unique=False, nullable=True)
    promptStr = Column(String(1000), unique=False, nullable=True)

class Sensors(Base):
    __tablename__ = 'sensors'
    id = Column(Integer, primary_key=True)
    uId = Column(String(50), unique=True)
    accessToken = Column(String(100), unique=True, nullable=False)
    type = Column(String(50), unique=False, nullable=True)
    sensorsSchemas = Column(Text, unique=False, nullable=True, default="[]")
    status = Column(String(50), unique=False, nullable=True)
    belongsTo = Column(String(50), unique=False, nullable=True)

class SensorData(Base):
    __tablename__ = 'sensordata'
    id = Column(Integer, primary_key=True)
    uId = Column(String(50), unique=True)
    sensorData = Column(Text, unique=False, nullable=True)
    lastUpdatedTime = Column(String(200), unique=False, nullable=True)
    belongsTo = Column(String(50), unique=False, nullable=True)

class Fields(Base):
    __tablename__ = 'fields'
    id = Column(Integer, primary_key=True)
    uId = Column(String(50), unique=True)
    cropType = Column(String(50), unique=False, nullable=True)
    area = Column(Float(50), unique=False, nullable=True)
