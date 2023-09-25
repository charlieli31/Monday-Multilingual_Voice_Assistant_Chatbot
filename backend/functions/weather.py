import requests
from decouple import config

# Retrieve Variables
WEATHERMAP_API_KEY = config("OPEN_WEATHER_MAP_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name: str):
    complete_url = BASE_URL + "q=" + city_name + "&appid=" + WEATHERMAP_API_KEY
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]
        return f"{city_name} - {weather_data['description']}, Temp: {main_data['temp']}°K"
    else:
        return "Error fetching weather data!"