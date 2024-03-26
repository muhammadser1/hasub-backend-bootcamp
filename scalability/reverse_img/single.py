import time

from PIL import Image

from writing_file import write_messages_to_file


def single_thread(height, width):
    for y in range(height):
        for x in range(width):
            pixel_color = img.getpixel((x, y))
            inverted_color = (255 - pixel_color[0], 255 - pixel_color[1], 255 - pixel_color[2])
            reversed_pixels[x, y] = inverted_color
sum_total=0
for _ in range(5):
    start = time.perf_counter()
    img = Image.open('img1.jpg')
    width, height = img.size
    print(width, height)
    reversed_img = img.copy()
    reversed_pixels = reversed_img.load()
    single_thread(height, width)
    reversed_img.show()
    end = time.perf_counter()
    total = end - start
    sum_total+=total
print('total: ', sum_total)
write_messages_to_file(["single_thread avg of 5 iteration ", str(sum_total/5)])
