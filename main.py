from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from agri.models import Base

import agri.response as Response
import agri.models as Models
import agri.handler as Handler
import agri.constants as Constants
import agri.schemas as Schemas

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./database/test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
async def root():
    return Response.WelcomeMessage()

@app.get("/createAccount")
@app.post("/getWeather")
async def get_weather(locationInfo : Schemas.LocationInfo):
    return Handler.getWeather(locationInfo)

