import requests
import json  # 👈 new import
from config import get_api_key, get_units

def get_weather_by_city(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": get_api_key(),
        "units": get_units()
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
        }
        return weather
    else:
        print("⚠️ API request failed with status code:", response.status_code)
        return None

def get_weather_by_zip(zip_code):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'zip': f'{zip_code},us',
        'appid' : get_api_key(),
        'units' : get_units(),
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        weather = {
            'city':data['name'],
            'temp':data['main']['temp'],
            'humidity':data['main']['humidity'],
            'feels_like':data['main']['feels_like'],
            'description':data['weather'][0]['description'],
        }
        return weather
    else:
        print('⚠️ API request failed with status code:', response.status_code)
        return None
