import requests
import json
from datetime import datetime

CITIES = {
    "yaounde": {"latitude": 3.848, "longitude": 11.5021},
    "douala": {"latitude": 4.0511, "longitude": 9.7679},
    "buea": {"latitude": 4.1533, "longitude": 9.3221},
    "lagos": {"latitude": 6.5244, "longitude": 3.3792},
    "abidjan": {"latitude": 5.3453, "longitude": -4.0244},
    "accra": {"latitude": 5.6037, "longitude": -0.1870},
}

# print("Available cities:", ", ".join(CITIES.keys()))

# print(CITIES["yaounde"])
def get_weather(city):
    city = city.lower()
    if city not in CITIES:
        print(f"City '{city}' not found. Available cities: {', '.join(CITIES.keys())}")
        return None
    
    coords = CITIES[city]
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": coords["latitude"],
        "longitude": coords["longitude"],
        "current_weather": True
    }
    try:
        reponse = requests.get(url, params=params, timeout=10)
        reponse.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching weather data for {city}: {e}")
        return None
    
def save_to_log(city, data):
    log_entry = {
        "city": city,
        "timestamp": datetime.now().isoformat(),
        "data": data
    }
    with open("weather_log.json", "a") as f:
        json.dump(log_entry, f)
        f.write("\n")  # Write each entry on a new line
    
def main():
    city = input("Enter a city name: ")
    weather_data = get_weather(city)
    if weather_data:
        print(f"Current temperature in {city}: {weather_data['current_weather']['temperature']} °C")
        save_to_log(city, weather_data)
        
if __name__ == "__main__":
    main()