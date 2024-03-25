import time


def calculate_average_execution_time(num_runs, func, *args, **kwargs):
    total_execution_time = 0
    for _ in range(num_runs):
        start_time = time.time()
        func(num_runs, *args, **kwargs)
        end_time = time.time()
        total_execution_time += end_time - start_time

    average_execution_time = total_execution_time / num_runs
    return average_execution_time
