"""FastAPI Weather API"""

from typing import List, Literal
import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from weather import get_weather_by_city, get_weather_by_zip
from storage import save_last_location, load_last_location, add_favorite, delete_favorites

app = FastAPI(title="Weather API")
FAVORITES_FILE = "favorites.json"

class LocationRequest(BaseModel):
    """Model representing a weather location request by city or zip code."""
    type: Literal["city", "zip"]
    value: str

class FavoriteLocation(BaseModel):
    """Model representing a favorite location."""
    type: str
    value: str

@app.get("/")
def home():
    """Root endpoint to check if the API is running."""
    return {"message": "🌦️ Welcome to the Weather API"}

@app.get("/weather/city/{city}")
def get_city_weather(city: str):
    """Fetch weather data by city name."""
    data = get_weather_by_city(city.title())
    if data:
        save_last_location("city", city.title())
        return data
    raise HTTPException(status_code=404, detail="City not found")

@app.get("/weather/zip/{zip_code}")
def get_zip_weather(zip_code: str):
    """Fetch weather data by zip code."""
    data = get_weather_by_zip(zip_code)
    if data:
        save_last_location("zip", zip_code)
        return data
    raise HTTPException(status_code=404, detail="Zip code not found")

@app.get("/last-location")
def get_last_saved_location():
    """Retrieve and return weather data for the last saved location."""
    location_type, location_value = load_last_location()
    if not location_type:
        raise HTTPException(status_code=404, detail="No last location saved")

    if location_type == "city":
        data = get_weather_by_city(location_value)
    elif location_type == "zip":
        data = get_weather_by_zip(location_value)
    else:
        raise HTTPException(status_code=400, detail="Invalid location type")

    if data:
        return data
    raise HTTPException(status_code=404, detail="Weather data not found for last location")

@app.get("/favorites", response_model=List[FavoriteLocation])
def list_favorites():
    """Return a list of saved favorite locations."""
    try:
        with open(FAVORITES_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data or []
    except FileNotFoundError:
        return []

@app.post("/favorites")
def save_favorite(location: LocationRequest):
    """Save a new favorite location."""
    add_favorite(location.type, location.value)
    return {"message": "New favorite saved."}

@app.delete("/favorites")
def remove_all_favorites():
    """Delete all saved favorite locations."""
    delete_favorites()
    return {"message": "All favorites deleted."}
