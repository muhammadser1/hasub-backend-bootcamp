import requests


class AsteroidDataFetcher:

    def get_asteroid_data(api_key_, start_date, end_date):
        """Fetches asteroid data from the NASA NEO API.

        Args:
            api_key (str): The API key required for accessing the NASA NEO API.
            start_date (str): The start date for the asteroid data (YYYY-MM-DD format).
            end_date (str): The end date for the asteroid data (YYYY-MM-DD format).

        Returns:
            dict: The asteroid data in JSON format.
        """
        url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key_}'
        response = requests.get(url)
        if response.status_code == 200:
            print("Success to fetch data from the nasa website.")
            response = response.json()
        else:
            print("Failed to fetch data from the nasa website.")
        return response
