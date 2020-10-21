"""
File: mirror_lake.py
Author name: Peter
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: image to be reflected
    :return: reflected image
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width, img.height * 2)     # a blank with double height
    for x in range(img.width):
        for y in range(img.height):
            old_pixel = img.get_pixel(x, y)
            new_pixel = new_img.get_pixel(x,y)
            new_pixel_mirror = new_img.get_pixel(x, img.height*2 - y - 1)  # assign pixel in a mirror style
            new_pixel.red = old_pixel.red
            new_pixel.blue = old_pixel.blue
            new_pixel.green = old_pixel.green
            new_pixel_mirror.red = old_pixel.red
            new_pixel_mirror.blue = old_pixel.blue
            new_pixel_mirror.green = old_pixel.green
    return new_img




def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
