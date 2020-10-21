"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.__dx = 0
        self.__dy = 0
        self.paddle_height = paddle_height
        self.paddle_width = paddle_width
        self.paddle_offset = paddle_offset
        self.count = 0

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.window.add(self.paddle, 0.5 * self.window_width - 0.5 * paddle_width, \
                        self.window_height - paddle_offset - paddle_height)
        self.paddle.filled = True

        # Center a filled ball in the graphical window.
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.window.add(self.ball, 0.5 * self.window_width - ball_radius, 0.5 * self.window_height - ball_radius)
        self.ball.filled = True

        # Default initial velocity for the ball.

        # Initialize our mouse listeners.
        onmousemoved(self.move)
        onmouseclicked(self.start)

        # Draw bricks.
        n = brick_offset
        m = 0
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(brick_rows):
            n += brick_height + brick_spacing
            for j in range(brick_cols):
                m = j * (brick_width + brick_spacing)
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.fill_color = color[i // 2]
                #  why cannot use else at the end?
                self.window.add(brick, m, n)

        self.original_x = 0.5 * self.window_width - ball_radius
        self.original_y = 0.5 * self.window_height - ball_radius

    def move(self, mouse):
        if mouse.x > self.window_width:
            self.paddle.x = self.window_width - self.paddle_width
        elif mouse.x - 0.5 * self.paddle_width < 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle_width / 2
            self.paddle.y = self.window_height - self.paddle_offset - self.paddle_height

    def start(self, mouse):
        if self.original_x == self.ball.x and self.original_y == self.ball.y:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if (random.random() > 0.5):  # why有底線
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def get_ball(self):
        return self.ball

    # def bricks(self):
        """if self.window.get_object_at(self.ball.x+ BALL_RADIUS, self.ball.y-1) is not None or\
                self.window.get_object_at(self.ball.x+BALL_RADIUS, self.ball.y +2*BALL_RADIUS+1) is not None:
            self.__dy = -self.__dy
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y-1))
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y+2*BALL_RADIUS+1))

        """
        """
        else:
            self.window.remove(self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y))
            self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2))
            self.window.remove(self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2))
            self.__dy = -self.__dy
        """



    def bounce(self):
        """
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            self.bounce()
        if self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y) is not None:
            self.bounce()
        if self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2) is not None:
            self.bounce()
        if self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2) is not None:
            self.bounce()
        """
        if self.ball.x <= 0 or self.ball.x + BALL_RADIUS * 2 >= self.window_width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        if self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y+ 2*BALL_RADIUS+1) is not None and\
                self.ball.y + 2*BALL_RADIUS +1 >= self.paddle.y:
            self.__dy = -self.__dy
        else:
            if self.ball.y < self.window.height * 0.5:
                if self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y - 1) is not None or \
                        self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS + 1) is not None:
                    self.__dy = -self.__dy
                    self.window.remove(self.window.get_object_at(self.ball.x+1, self.ball.y - 1))
                    self.window.remove(self.window.get_object_at(self.ball.x+1, self.ball.y + 2 * BALL_RADIUS + 1))
                if self.window.get_object_at(self.ball.x-1, self.ball.y+BALL_RADIUS) is not None or \
                    self.window.get_object_at(self.ball.x+2*BALL_RADIUS+1, self.ball.y+BALL_RADIUS) is not None:
                    self.__dx = -self.__dx
                    self.window.remove(self.window.get_object_at(self.ball.x-1, self.ball.y+1))
                    self.window.remove(self.window.get_object_at(self.ball.x + 2*BALL_RADIUS +1, self.ball.y+1))

    def restart(self):
        if self.ball.y > self.window.height:
            if self.count == 2:
                print('end')
            else:
                self.window.add(self.ball, 0.5 * self.window_width -BALL_RADIUS, 0.5 * self.window_height - BALL_RADIUS)
                self.count += 1


