"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Peter.

-----------------------------------------------

TODO:
To make a App
which can make perfect photo
by several different photo shot at the same location but different time
(remove the part being intercepted by passerby and make a perfect photo
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    color_distance = ((red - pixel[0]) ** 2 + (green - pixel[1]) ** 2 + (blue - pixel[2]) ** 2) ** 0.5
    return color_distance
    # pick the red, green , and blue part in the single pixel and calculate the distance with given RGB
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """


def get_average(pixels):
    red = 0
    green = 0
    blue = 0
    for i in range(len(pixels)):
        red += pixels[i].red
        green += pixels[i].green
        blue += pixels[i].blue
    color_list = [red / len(pixels), green / len(pixels), blue / len(pixels)]
    return color_list
    # add up RGBs of every input, and divide with the length of the list to get average
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """


def get_best_pixel(pixels):
    pixels.append(get_average(pixels))
    n = 10000
    for i in range(len(pixels) - 1):
        if n > get_pixel_dist(pixels[-1], pixels[i].red, pixels[i].green, pixels[i].blue):
            pixels[0] = pixels[i]
            n = get_pixel_dist(pixels[-1], pixels[i].red, pixels[i].green, pixels[i].blue)
    return pixels[0]
    # use pixel[0] to store the best pixel
    # use get_average and add the average at the end of the list (the range will be: (len(pixels) - 1) at Line 70)
    # calculate the distance by get_distance
    # if the distance is smaller than n, we change pixel[0]
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(result.width):
        for y in range(result.height):
            pixel = get_best_pixel([images[0].get_pixel(x, y), images[1].get_pixel(x, y),
                                           images[2].get_pixel(x, y), images[3].get_pixel(x, y)])
            result.set_pixel(x, y, pixel)
    # use nested for loop to get and run through all pixels in all four images
    # use get_best_pixel to get the best pixel in each (x, y)
    # set that best pixel on the result

    """
    green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    best1 = get_best_pixel([green_pixel, green_pixel, green_pixel, blue_pixel])
    print(best1.red, best1.green, best1.blue)
    
    print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))
    
    green_im = SimpleImage.blank(20, 20, 'green')
    green_pixel = green_im.get_pixel(0 ,0)
    print(get_pixel_dist(green_pixel, 5, 255, 10))
    """
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
