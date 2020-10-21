"""
File: blur.py
Author name: Peter
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(old_img):
    """
    :param img: old image
    :return: blurred image
    """
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    for y in range(old_img.height-1):
        for x in range(old_img.width-1):
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            sum = 0
            if old_img.width-1 > x > 0 and old_img.height-1 > y > 0:  # make the maximum and minimum
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):  # get the nine points around each pixels
                        old_pixel = old_img.get_pixel(i, j)
                        sum_red += old_pixel.red
                        sum_blue += old_pixel.blue
                        sum_green += old_pixel.green
                new_pixel = new_img.get_pixel(x, y)
                new_pixel.red = sum_red / 9
                new_pixel.green = sum_green / 9
                new_pixel.blue = sum_blue / 9
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(9):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
