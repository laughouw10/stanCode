"""
File: drawing line
Name: Peter
-------------------------
TODO:
Draw line by two clicks
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
w = GWindow()
n = 1
x = 0
y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(point)
    pass


def point(m):
    global n
    global x
    global y
    #  use "n" to figure out this is the first click or second click
    if n == 1:
        #  add a point on the window
        hole = GOval(SIZE, SIZE)
        hole.filled = True
        hole.fill_color = 'white'
        w.add(hole, m.x - 0.5 * SIZE, m.y - 0.5 * SIZE)
        x = m.x
        y = m.y
        n -= 1
    else:
        #  in the second click, remove the point made by first click and draw the line
        obj = w.get_object_at(x, y)
        w.remove(obj)
        line = GLine(x, y, m.x, m.y)
        w.add(line, x, y)
        x = 0
        y = 0
        n += 1






if __name__ == "__main__":
    main()
