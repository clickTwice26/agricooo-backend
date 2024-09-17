import agri.schemas as Schemas
import requests



def getWeather(locationInfo : Schemas.LocationInfo):
    # print(locationData.model_dump_json())
    WEATHER_API = f"""https://api.weatherapi.com/v1/forecast.json?key=ff9b41622f994b1287a73535210809&q={locationInfo.latitude},{locationInfo.longitude}&days=3"""
    response = requests.get(WEATHER_API)

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

# def nameToLocationInfo(locationName : str):
#