import time
import cv2

from writing_file import write_messages_to_file


def single_thread(height, width, img):
    reversed_img = img.copy()
    for y in range(height):
        for x in range(width):
            pixel_color = img[y, x]
            inverted_color = (255 - pixel_color[0], 255 - pixel_color[1], 255 - pixel_color[2])
            reversed_img[y, x] = inverted_color
    # cv2.imshow("Reversed Image", reversed_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def main():
    sum_total = 0
    num_iterations = 5
    for _ in range(num_iterations):
        start = time.perf_counter()
        img = cv2.imread('img1.jpg')
        height, width, _ = img.shape
        single_thread(height, width, img)
        end = time.perf_counter()
        total = end - start
        sum_total += total
        print('Iteration time:', total)
    print('Average time:', sum_total / num_iterations)
    write_messages_to_file(["single_thread avg of 5 iteration using cv2  ", str(sum_total / 5)])


if __name__ == "__main__":
    main()
