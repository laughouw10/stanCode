"""
File: green_screen.py
Author name: Peter
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: background image
    :param figure_img: image of a person or character
    :return:
    """
    background_img.make_as_big_as(figure_img)
    for y in range(figure_img.height):
        for x in range(figure_img.width):
            pixel = figure_img.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue) / 3
            if pixel.green > avg:       # if the green element in pixel above the assigned value (avg*H)
                bg_pixel = background_img.get_pixel(x, y)   # consider it as a background, replace by background
                pixel.red = bg_pixel.red
                pixel.green = bg_pixel.green
                pixel.blue = bg_pixel.blue
    return figure_img


def main():
    """
    TODO:
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
