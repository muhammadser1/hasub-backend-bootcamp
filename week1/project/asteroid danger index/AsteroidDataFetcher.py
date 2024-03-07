import requests


class AsteroidDataFetcher:

    def get_asteroid_data(api_key_, start_date, end_date):
        url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key_}'
        response = requests.get(url)
        if response.status_code == 200:
            print("Success to fetch data from the nasa website.")
            response = response.json()
        else:
            print("Failed to fetch data from the nasa website.")
        return response
