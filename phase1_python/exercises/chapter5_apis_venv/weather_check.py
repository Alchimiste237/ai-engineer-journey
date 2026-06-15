import requests

#Yaounde coordinates as an example
latitude = 3.848
longitude = 11.5021

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

reponse = requests.get(url, params=params)

print("Status code:", reponse.status_code)

if reponse.status_code == 200:
    data = reponse.json()
    # print(data)
    print("Current temperature:", data["current_weather"]["temperature"], "°C")
else:
    print("Error fetching weather data:", reponse.text)