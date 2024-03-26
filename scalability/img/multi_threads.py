import time
from threading import Thread
from queue import Queue
from PIL import Image


def process_chunk(img, start_x, end_x, height, result_queue, memo):
    for y in range(height):
        for x in range(start_x, end_x):
            pixel_color = img.getpixel((x, y))
            inverted_color = (255 - pixel_color[0], 255 - pixel_color[1], 255 - pixel_color[2])
            # result_queue.put((x, y, inverted_color))
            memo[(x, y)] = inverted_color


if __name__ == '__main__':
    memo = {}
    img = Image.open('img1.jpg')
    width, height = img.size
    print(width, height)
    reversed_img = img.copy()
    reversed_pixels = reversed_img.load()
    start_time = time.time()

    num_threads = 10
    chunk_width = width // num_threads

    threads = []
    result_queue = Queue()

    for i in range(num_threads):
        start_x = i * chunk_width
        end_x = (i + 1) * chunk_width if i < num_threads - 1 else width
        print("Thread" + str(i) + "   ", start_x, end_x)
        thread = Thread(target=process_chunk, args=(img, start_x, end_x, height, result_queue, memo))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # Apply changes to the image using memo
    for key, value in memo.items():
        reversed_pixels[key[0], key[1]] = value

    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    reversed_img.show()
