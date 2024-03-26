import time

from PIL import Image


def single_thread(height,width):
    start = time.perf_counter()
    for y in range(height):
        for x in range(width):
            pixel_color = img.getpixel((x, y))
            inverted_color = (255 - pixel_color[0], 255 - pixel_color[1], 255 - pixel_color[2])
            reversed_pixels[x, y] = inverted_color
    end = time.perf_counter()
    total = end - start
    print('total: ', total)


img = Image.open('img1.jpg')
width, height = img.size
print(width,height)
reversed_img = img.copy()
reversed_pixels = reversed_img.load()
single_thread(height,width)
reversed_img.show()