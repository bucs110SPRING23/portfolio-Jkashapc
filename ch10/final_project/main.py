from pyowm import OWM
import googlemaps
from dotenv import load_dotenv
import os

load_dotenv()

owm_api_key = os.getenv('OWM_API_KEY')
gmaps_api_key = os.getenv('GMAPS_API_KEY')


owm = OWM(owm_api_key)
gmaps = googlemaps.Client(key=gmaps_api_key)

class OpenWeatherMapAPI:
    def __init__(self):
        self.api_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather_data(self, city):
        
        mgr = owm.weather_manager()
        weather = mgr.weather_at_place(city).weather

        
        temp = weather.temperature('celsius')['temp']
        humidity = weather.humidity
        wind_speed = weather.wind()['speed']
        description = weather.detailed_status

        
        weather_data = {
            'temperature': temp,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'description': description
        }

        return weather_data

class GoogleMapsAPI:
    def __init__(self):
        self.api_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    def get_location(self, address):
        
        geocode_result = gmaps.geocode(address)

        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            lat, lng = location['lat'], location['lng']

            return lat, lng

        return None


if __name__ == '__main__':
   
    weather_api = OpenWeatherMapAPI()
    maps_api = GoogleMapsAPI()

    
    address = 'New York City'

    
    location = maps_api.get_location(address)

    if location:
        
        weather_data = weather_api.get_weather_data(f"{location[0]}, {location[1]}")

        
        print(f"Weather in {address}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind speed: {weather_data['wind_speed']} m/s")
        print(f"Description: {weather_data['description']}")

        
        map_url = f"https://www.google.com/maps/search/?api=1&query={location[0]},{location[1]}"
        print(f"Map: {map_url}")
    else:
        print(f"Could not find location for address: {address}")
