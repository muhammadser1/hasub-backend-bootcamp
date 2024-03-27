import time


def calculate_average_execution_time(nums, func, *args, **kwargs):
    start_time = time.perf_counter()
    for _ in range(nums):
        func(*args, **kwargs)
    end_time = time.perf_counter()
    avg = (end_time - start_time) / nums
    return avg
