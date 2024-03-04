import requests

def fetch_weather(api_key, latitude, longitude):
    url = f"https://www.7timer.info/bin/api.pl?lon={longitude}&lat={latitude}&product=astro&output=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

def main():
    api_key = ""  # Replace "YOUR_API_KEY" with your actual API key
    latitude = 32.701580  # Latitude of the location (e.g., Earth coordinates)
    longitude = 35.298149  # Longitude of the location (e.g., Earth coordinates)
    weather_data = fetch_weather(api_key, latitude, longitude)
    if weather_data:
        print("Weather data:")

        print(weather_data["dataseries"][0])
    else:
        print("No weather data available")

if __name__ == "__main__":
    main()
