import time
import numpy as np
from PIL import Image
from threading import Thread

from writing_file import write_messages_to_file

width, height = 6000, 4000


matrix = np.random.randint(0, 256, size=(height, width, 3), dtype=np.uint8)


def process_chunk(img, start_x, end_x, start_y, end_y):
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            pixel_color = img[x, y]
            inverted_color = (255 - pixel_color[0], 255 - pixel_color[1], 255 - pixel_color[2])
            matrix[y, x] = inverted_color


def multi_thread(height, width):
    threads = []
    num_threads = 8
    chunk_height = height // num_threads

    for i in range(num_threads):
        start_y = i * chunk_height
        end_y = (i + 1) * chunk_height if i < num_threads - 1 else height
        thread = Thread(target=process_chunk, args=(reversed_pixels, 0, width, start_y, end_y))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


total_sum = 0
for _ in range(5):
    start = time.perf_counter()

    img = Image.open('img1.jpg')

    reversed_pixels = img.load()

    multi_thread(height, width)


    # img = Image.fromarray(matrix)
    # img.show()
    end = time.perf_counter()
    total_time = end - start
    total_sum += total_time
write_messages_to_file(["multi_threads (8 threads) avg of 5 iteration using PIL Image", str(total_sum / 5)])
