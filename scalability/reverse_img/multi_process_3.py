import time

from PIL import Image
import numpy as np
import multiprocessing

from writing_file import write_messages_to_file


def process_image_chunk(chunk):
    # Apply image processing operations to the chunk
    # This function should contain your image processing logic
    # Here, we'll just invert the colors for demonstration purposes
    return 255 - chunk

def main():
    start=time.perf_counter()
    # Load the image
    image_path = 'img1.jpg'
    img = Image.open(image_path)

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Define the number of processors to use
    num_processors = 1

    # Split the image into horizontal sections according to the number of processors
    height, width, _ = img_array.shape
    chunk_height = height // num_processors
    chunks = [img_array[i*chunk_height:(i+1)*chunk_height] for i in range(num_processors)]
    # Process each chunk in parallel
    with multiprocessing.Pool(processes=num_processors) as pool:
        processed_chunks = pool.map(process_image_chunk, chunks)

    # Merge the processed chunks back into the final image
    processed_image = np.concatenate(processed_chunks, axis=0)

    # Display the processed image
    Image.fromarray(processed_image).show()
    end=time.perf_counter()
    print(end-start)
    write_messages_to_file(["multi_processing (1 processing)  ", str(end-start)])


if __name__ == "__main__":
    main()
