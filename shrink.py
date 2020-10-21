"""
File: shrink.py
Author name: Peter
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, image's name to be shrinked
    :return img: SimpleImage, shrinked image
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width//2, img.height//2)  # a blank with half width and half height
    for x in range(0, img.width, 2):
        for y in range(0, img.height, 2):  # from 0 to maximum, add by 2,
            pixel = img.get_pixel(x, y)    # get the pixels to be used to shrink, and get the pixels around, make avg
            pixel1 = img.get_pixel(x+1, y)
            pixel2 = img.get_pixel(x, y+1)
            pixel3 = img.get_pixel(x+1, y+1)
            new_pixel = new_img.get_pixel(x/2, y/2)
            new_pixel.red = (pixel.red + pixel1.red + pixel2.red + pixel3.red) / 4
            new_pixel.blue = (pixel.blue + pixel1.blue + pixel2.blue + pixel3.blue) / 4
            new_pixel.green = (pixel.green + pixel1.green + pixel2.green + pixel3.green) / 4
    return new_img


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
