import requests

def get_weather_details(city):
    res = requests.get(f"https://api.weather.com/v1/{city}")

    if res.status_code == 200:
        return res.json()
    else:
        raise ValueError("Could not fetch weather details")    