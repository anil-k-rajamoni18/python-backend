from fastapi import FastAPI
from weather_api.weather import get_weather

app = FastAPI()

@app.get("/weather/{city}")
async def fetch_weather(city: str):
    data = await get_weather(city)
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }