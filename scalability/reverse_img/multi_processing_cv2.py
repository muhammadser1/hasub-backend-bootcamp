import time
import cv2
import numpy as np
import multiprocessing

from writing_file import write_messages_to_file


def process_image_chunk(chunk):
    height, width, _ = chunk.shape
    processed_chunk = np.zeros_like(chunk)

    for y in range(height):
        for x in range(width):
            pixel_value = chunk[y, x]

            processed_pixel = 255 - pixel_value

            processed_chunk[y, x] = processed_pixel

    return processed_chunk


def main():
    sum_total = 0
    for _ in range(5):
        start = time.perf_counter()
        image_path = 'img1.jpg'
        img = cv2.imread(image_path)

        num_processors = 5

        height, width, _ = img.shape
        chunk_height = height // num_processors
        chunks = [img[i * chunk_height:(i + 1) * chunk_height] for i in range(num_processors)]

        with multiprocessing.Pool(processes=num_processors) as pool:
            processed_chunks = pool.map(process_image_chunk, chunks)

        processed_image = np.concatenate(processed_chunks, axis=0)



        end = time.perf_counter()
        sum_total+=end-start
    write_messages_to_file(["multi_processing (5 processors) avg of 5 iteration using cv2 Image ", str(sum_total / 5)])


if __name__ == "__main__":
    main()
