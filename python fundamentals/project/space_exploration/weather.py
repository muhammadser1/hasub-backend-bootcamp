import requests
import json

def fetch_weather(api_key, latitude, longitude):
    url = f"https://www.7timer.info/bin/api.pl?lon={longitude}&lat={latitude}&product=astro&output=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

def save_weather_data(weather_data, filename):
    with open(filename, "w") as json_file:
        json.dump(weather_data, json_file)

def load_weather_data(filename):
    with open(filename, "r") as json_file:
        return json.load(json_file)

def main():
    api_key = ""
    latitude = 32.701580
    longitude = 35.298149
    weather_data = fetch_weather(api_key, latitude, longitude)
    if weather_data:

        save_weather_data(weather_data, "weather_data.json")
        loaded_weather_data = load_weather_data("weather_data.json")
        print(len(loaded_weather_data["dataseries"]))
    else:
        print("No weather data available")

if __name__ == "__main__":
    main()
