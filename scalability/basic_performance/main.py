import random
import time
import matplotlib.pyplot as plt


from text.count_words import *


def calculate_results(arr):
    start_time = time.perf_counter()
    count_word_good(arr)
    end_time = time.perf_counter()
    return end_time - start_time


def draw_results(results):
    sizes = [val[0] for val in results]
    time_taken = [val[1] for val in results]
    plt.plot(sizes, time_taken, marker='o')
    plt.xlabel('Size of Input (Number of Elements)2^25')
    plt.ylabel('Time Taken (seconds)')
    plt.title('good count word Performance (25 points)')
    plt.savefig('text/good_count_words.png')
    plt.grid(True)
    plt.show()


def generate_random_text(length):
    return ' '.join(random.choices(words, k=length))


if __name__ == "__main__":
    words = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    sizes = [2 ** i for i in range(1, 25)]
    print(len(sizes))
    results = []
    i = 1
    for length in sizes:
        print(i)
        random_text = generate_random_text(length)
        i += 1
        time_taken = calculate_results(random_text)
        results.append((length, time_taken))
    draw_results(results)
