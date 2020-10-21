"""
File: sierpinski.py
Name: Peter
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 9                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	make a recursion to draw triangles
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: control how many times of loop
	:param length: the length of the first triangle
	:param upper_left_x: the upper left x coordinate
	:param upper_left_y: the upper left y coordinate
	:return: nothing
	"""
	if order == 0:
		return
	else:
		# draw line to form a triangle
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		line2 = GLine(upper_left_x, upper_left_y, upper_left_x + 0.5 * length, upper_left_y + 0.866 * length)
		line3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5, upper_left_y + 0.866 * length)

		pause(20)
		# add line on window
		window.add(line1)
		window.add(line2)
		window.add(line3)

		# enter recursion
		# one at left, one at right, and one at the bottom
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + 0.5 * length, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + 0.25 * length, upper_left_y + 0.433 * length)


if __name__ == '__main__':
	main()