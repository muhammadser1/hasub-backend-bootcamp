import requests
from ApiKeyReader import *
from AsteroidDataFetcher import *
import json
from JSONHandler import *
from GraphPlotter import *
if __name__ == '__main__':

    api_key_nasa=ApiKeyReader("nasa_ipi_key.txt")
    api_key_nasa=api_key_nasa.read_api_key()

    astroid=AsteroidDataFetcher()
    data = AsteroidDataFetcher.get_asteroid_data(api_key_nasa, "2015-09-07", "2015-09-07")

    filename = 'response_data.json'
    JSONHandler.write_data_to_json(data,filename)

    data=JSONHandler.read_data_from_json(filename)

    a = int(input("Enter the value of parameter A: "))
    b = int(input("Enter the value of parameter B: "))
    c = int(input("Enter the value of parameter C: "))

    output=GraphPlotter(a,b,c)
    output.plot_asteroid_data(data)
