"""
File: bouncing ball
Name: Peter
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
n = 0
V = 0
time = 0
end = 0

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(bounce)
    pass


def bounce(m):
    global n, V, time, end
    if (time < 3) and (end == 0):
        window.clear()
        end = 1
        X = START_X
        Y = START_Y
        ball = GOval(SIZE, SIZE)
        ball.filled = True
        window.add(ball, X, Y)
        while X < 800:
            while Y < 500:
                n += 1
                pause(DELAY)
                window.clear()
                window.add(ball, X, Y)
                pause(DELAY)
                X = X + VX
                V = GRAVITY * n
                Y = Y + V
            V = V * 0.9
            n = 0
            while V > 0:
                n += 0.1
                X = X + VX
                V = V - GRAVITY * n
                Y = Y - V
                pause(DELAY)
                window.clear()
                window.add(ball, X, Y)
                pause(DELAY)
        window.add(ball, START_X, START_Y)
        time += 1
        end = 0





















if __name__ == "__main__":
    main()
