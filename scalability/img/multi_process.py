import time
from PIL import Image
from multiprocessing import Process, Array

def process_chunk(img_data, start_x, end_x, height, output, width):
    img = Image.frombytes('RGB', (width, height), img_data)  # Convert shared array to image
    pixels = img.load()
    for y in range(height):
        for x in range(start_x, end_x):
            pixel_color = pixels[x, y]
            inverted_color = (255 - pixel_color[0], 255 - pixel_color[1], 255 - pixel_color[2])
            # Convert 2D coordinates to 1D index for shared memory array
            index = (y * width + x) * 3
            # Write inverted color to shared memory array
            output[index] = inverted_color[0]
            output[index + 1] = inverted_color[1]
            output[index + 2] = inverted_color[2]

if __name__ == '__main__':
    img = Image.open('img1.jpg')
    width, height = img.size
    print("Image size:", width, height)

    start_time = time.time()

    # Convert image to bytes and store it in a shared memory array
    img_bytes = img.tobytes()
    img_data = Array('B', img_bytes)

    output = Array('B', width * height * 3)

    num_processes = 5  # Number of processes to use
    chunk_width = width // num_processes

    processes = []

    for i in range(num_processes):
        start_x = i * chunk_width
        end_x = (i + 1) * chunk_width if i < num_processes - 1 else width
        process = Process(target=process_chunk, args=(img_data, start_x, end_x, height, output, width))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    processed_img = Image.new('RGB', (width, height))
    processed_pixels = processed_img.load()

    for y in range(height):
        for x in range(width):
            index = (y * width + x) * 3
            inverted_color = (output[index], output[index + 1], output[index + 2])
            processed_pixels[x, y] = inverted_color

    end_time = time.time()
    total_time = end_time - start_time
    print('Total time:', total_time)

    processed_img.show()
