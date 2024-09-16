from fastapi import FastAPI

import agri.response as Response
import agri.models as Models
import agri.handler as Handler
import agri.constants as Constants
import agri.schemas as Schemas

app = FastAPI()

@app.get("/")
async def root():
    return Response.WelcomeMessage()

@app.post("/getWeather")
async def get_weather(locationInfo : Schemas.LocationInfo):
    return Handler.getWeather(locationInfo)

