def fibonacci_opt(number, memo={}):
    """
    Calculate the Fibonacci sequence up to the given number using memoization.

    Parameters:
    - number: An integer representing the position in the Fibonacci sequence to calculate.
    - memo: A dictionary containing previously calculated Fibonacci numbers.

    Returns:
    - The Fibonacci number at the given position.
    O(n) Place, O(n) runtime
    """
    if number == 0:
        return 0
    if number == 1:
        return 1

    memo[0] = 0
    memo[1] = 1

    for num in range(2, number + 1):
        memo[num] = memo[num - 1] + memo[num - 2]

    return memo


def fibonacci_recursive(number):
    """
    Calculate the Fibonacci sequence recursively.

    Parameters:
    - number: An integer representing the position in the Fibonacci sequence to calculate.

    Returns:
    - The Fibonacci number at the given position.
    """
    if number <= 1:
        return number
    else:
        return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


def fibonacci_bad(number, memo=[]):
    """
    Calculate the Fibonacci sequence up to the given number using a non-optimal approach.

    Parameters:
    - number: An integer representing the position in the Fibonacci sequence to calculate.
    - memo: A list containing previously calculated Fibonacci numbers.

    Returns:
    - A list containing the Fibonacci sequence up to the given number.
    O(n) Place, O(n* 2^n) runtime
    """
    for num in range(number + 1):
        memo.append(fibonacci_recursive(num))
    return memo










#
# import time
#
# import numpy as np
# from matplotlib import pyplot as plt
#
# from Fibonacci import *
#
#
# def calculate_results_opt(num):
#     start_time = time.perf_counter()
#     fibonacci_opt(num*100)
#     end_time = time.perf_counter()
#     total_time = round(end_time - start_time, 2)
#     return total_time
#
#
# def calculate_results_bad(num):
#     start_time = time.perf_counter()
#     fibonacci_bad(num)
#     end_time = time.perf_counter()
#     total_time = round(end_time - start_time, 2)
#     return total_time
#
#
# def draw_results(results_opt, results_bad):
#     list_size_opt = [val[0] for val in results_opt]
#     time_opt = [val[1] for val in results_opt]
#     list_size_bad = [val[0] for val in results_bad]
#     time_bad = [val[1] for val in results_bad]
#
#     plt.scatter(list_size_opt, time_opt, label='Optimal Fibonacci')
#     plt.scatter(list_size_bad, time_bad, label='Bad Fibonacci')
#
#     plt.xlabel('Size')
#     plt.ylabel('Time')
#     plt.title('Size vs Time')
#     plt.legend()
#     plt.grid(True)
#     plt.savefig('fib_comparison.png')  # Save the plot as PNG file
#     plt.show()
#
#
# if __name__ == "__main__":
#     powers = [x for x in range(30)]
#
#     # Results for optimal Fibonacci
#     results_opt = []
#     for num in powers:
#         result = calculate_results_opt(num)
#         results_opt.append((num, result))
#
#     # Results for bad Fibonacci
#     results_bad = []
#     for num in powers:
#         result = calculate_results_bad(num)
#         results_bad.append((num, result))
#
#     draw_results(results_opt, results_bad)
