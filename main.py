import json

from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from agri.models import Base, User, ApiToken
from agri.program import uIdGen, getAccessToken

import agri.response as Response
import agri.models as Models
import agri.handler as Handler
import agri.constants as Constants
import agri.schemas as Schemas
import agri.input as InputSchemas


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLALCHEMY_DATABASE_URL = "sqlite:///./database/agricooo.db"
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

@app.post("/createAccount")
async def createAccount(newUserInfo : InputSchemas.accountCreationInfo, db: Session = Depends(get_db)):
    checkExist = db.query(User).filter(User.phoneNumber == newUserInfo.phoneNumber).first()
    if checkExist:
        return Response.FlashMessage(message="account already exists with this phone number", category="warning")
    try:
        uId = uIdGen(newUserInfo.fullName + newUserInfo.email + newUserInfo.phoneNumber)
        accessToken = getAccessToken()
        newUser = User(uId=uId, accessToken=accessToken, **newUserInfo.model_dump())
        db.add(newUser)
        try:
            db.commit()
            return Response.FlashMessage(message="account created", category="success")

        except Exception as error:
            return Response.ErrorMessage(errorMessage=f"database error {error}", errorType="error", errorCode=1)
    except Exception as error:
        return Response.ErrorMessage(errorMessage="something went wrong. account creation failed", errorType=f"{error}", errorCode=1)
@app.post("/getWeather")
async def get_weather(locationInfo : Schemas.LocationInfo):
    return Handler.getWeather(locationInfo)

@app.get("/getLanguagePack")
async def getInnerContent(language :str = "en"):

    if language not in ["en", "bn"]:
        return Response.ErrorMessage(errorMessage="invalid language", category="warning")
    else:
        return json.loads(open(f"languages/{language}.json", "r").read())