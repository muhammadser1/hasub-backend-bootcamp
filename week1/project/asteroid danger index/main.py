import requests
from ApiKeyReader import *
from AsteroidDataFetcher import *
import json
from JSONHandler import *
from GraphPlotter import *
import asyncio
import time
from datetime import datetime, timedelta


async def process_and_store_data(start_time, date, filename):
    original_date = datetime.strptime(date, "%Y-%m-%d")
    new_date = original_date + timedelta(days=7)
    new_date = new_date.strftime("%Y-%m-%d")

    # Perform file I/O asynchronously
    await asyncio.to_thread(JSONHandler.write_data_to_json, AsteroidDataFetcher.get_asteroid_data(api_key_nasa, date, new_date), filename, date)

    elapsed_time = time.time() - start_time
    print(f"Task for {date}-{new_date} completed in {elapsed_time:.0f} seconds. started in {start_time:.0f}  finished in {time.time():.0f}")


async def fun():
    start_time = time.time()
    task1 = asyncio.create_task(process_and_store_data(start_time,"2015-09-01", "response_data1.json"))
    task2 = asyncio.create_task(process_and_store_data(start_time,"2015-09-08", "response_data2.json"))
    task3 = asyncio.create_task(process_and_store_data(start_time,"2015-09-15", "response_data3.json"))
    task4 = asyncio.create_task(process_and_store_data(start_time,"2015-09-22", "response_data4.json"))
    await asyncio.gather(task1, task2, task3,task4)


if __name__ == '__main__':
    api_key_nasa = ApiKeyReader("nasa_ipi_key.txt")
    api_key_nasa = api_key_nasa.read_api_key()

    astroid = AsteroidDataFetcher()
    asyncio.run(fun())

    data1 = JSONHandler.read_data_from_json("response_data1.json")
    data2 = JSONHandler.read_data_from_json("response_data2.json")
    data3 = JSONHandler.read_data_from_json("response_data3.json")
    data4 = JSONHandler.read_data_from_json("response_data4.json")
    data=data1+data2+data3+data4
    print(len(data1))
    a = int(input("Enter the value of parameter A: "))
    b = int(input("Enter the value of parameter B: "))
    c = int(input("Enter the value of parameter C: "))

    output = GraphPlotter(a, b, c)
    output.plot_asteroid_data(data1)