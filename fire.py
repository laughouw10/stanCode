"""
File: fire.py
Author name: Peter
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: original image
    :return: image with point on fire
    """
    img = SimpleImage(filename)
    for pixel in img:
        total = (pixel.red + pixel.blue + pixel.green) / 3
        if pixel.red > total * HURDLE_FACTOR:   # if the red element in pixel above the assigned value (avg*H)
            pixel.red = 255                     # change that pixel to a super red point
            pixel.green = 0
            pixel.blue = 0
        else:                                   # else, put gray on that pixel
            pixel.red = total
            pixel.green = total
            pixel.blue = total
    return img


def main():
    """
    TODO:
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
