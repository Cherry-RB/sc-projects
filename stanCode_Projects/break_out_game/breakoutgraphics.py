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

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-\
                                                                                paddle_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = "purple"
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.click_to_start)

        # Draw bricks
        self.row_times = 0
        for row in range(brick_rows):
            self.row_times += 1
            for col in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.color_brick()
                self.window.add(self.brick, x=(brick_width + brick_spacing) * col, y=brick_offset + \
                                                                            (brick_height + brick_spacing) * row)
        # for row in range(brick_rows):  # 列
        #     self.row_times += 1
        #     for col in range(brick_cols):  # 行
        #         self.brick = GRect(brick_width, brick_height)
        #         self.color_brick()
        #         self.window.add(self.brick, x=(brick_width + brick_spacing) * col, y=brick_offset + \
        #                                                                    (brick_height + brick_spacing) * row)
        #         # if row == 0 or 1:  # (row,col)==(0,0),(0,1),(0,2)...(0,brick_cols)
                    #                           (1,0),(1,1),(1,2)...(1,brick_cols)
                    # self.brick1 = GRect(brick_width, brick_height)
                    # self.brick1.filled = True
                    # self.brick1.color = "red"
                    # self.brick1.fill_color = "red"
                    # self.window.add(self.brick1, x=(brick_width + brick_spacing) * col, y=brick_offset + \
                    #                                                       (brick_height + brick_spacing) * row)
                # elif row == 2 or 3:  # (row,col)==(2,0),(2,1),(2,2)...(2,brick_cols)
                #     #                           (3,0),(3,1),(3,2)...(3,brick_cols)
                #     self.brick2 = GRect(brick_width, brick_height)
                #     self.brick2.filled = True
                #     self.brick2.color = "orange"
                #     self.brick2.fill_color = "orange"
                #     self.window.add(self.brick2, x=(brick_width + brick_spacing) * col, y=brick_offset + \
                #                                                         (brick_height + brick_spacing) * (row))
                # elif row == 4 or 5:
                #     self.brick3 = GRect(brick_width, brick_height)
                #     self.brick3.filled = True
                #     self.brick3.color = "yellow"
                #     self.brick3.fill_color = "yellow"
                #     self.window.add(self.brick3, x=(brick_width + brick_spacing) * col, y=brick_offset + \
                #                                                         (brick_height + brick_spacing) * (row))
                # elif row == 6 or 7:
                #     self.brick4 = GRect(brick_width, brick_height)
                #     self.brick4.filled = True
                #     self.brick4.color = "green"
                #     self.brick4.fill_color = "green"
                #     self.window.add(self.brick4, x=(brick_width + brick_spacing) * col, y=brick_offset + \
                #                                                          (brick_height + brick_spacing) * (row))
                # elif row == 8 or 9:
                #     self.brick5 = GRect(brick_width, brick_height)
                #     self.brick5.filled = True
                #     self.brick5.color = "blue"
                #     self.brick5.fill_color = "blue"
                #     self.window.add(self.brick5, x=(brick_width + brick_spacing) * col, y=brick_offset +\
                #                                                   (brick_height + brick_spacing) * (row))
        self.mouse_click = 0
        self.times = 0
    #
    def color_brick(self):
        self.brick.filled = True
        if self.row_times == 1 or 2:
            self.brick.color = "red"
            self.brick.fill_color = "red"
        elif self.row_times == 3 or 4:
            self.brick.color = "orange"
            self.brick.fill_color = "orange"
        elif self.row_times == 5 or 6:
            self.brick.color = "yellow"
            self.brick.fill_color = "yellow"
        elif self.row_times == 7 or 8:
            self.brick.color = "green"
            self.brick.fill_color = "green"
        elif self.row_times == 9 or 10:
            self.brick.color = "blue"
            self.brick.fill_color = "blue"

    def paddle_move(self, mouse):
        if self.paddle.width/2 <= mouse.x <= self.window.width-self.paddle.width/2:
            self.paddle.x = mouse.x-self.paddle.width/2

    def ball_move(self):  # 球碰到視窗會反彈
        self.ball.move(dx=self.__dx, dy=self.__dy)
        if not 0 <= self.ball.x <= self.window.width-self.ball.width:
            self.__dx = -self.__dx
        if not 0 <= self.ball.y <= self.window.height-self.ball.height:
            self.__dy = -self.__dy

    def set_dx(self):
        self.__dx *= -1

    def set_dy(self):
        self.__dy *= -1

    def click_to_start(self, mouse):
        if self.mouse_click == 0:  # 如果是滑鼠開關初始值
            if self.times != 3:  # 如果還有命
                self.mouse_click += 1  # 就把滑鼠開關打開!
                return self.mouse_click

    def ball_touch(self):  # 感應球是否碰到物件
        ball_vertex1 = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_vertex2 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        ball_vertex3 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        ball_vertex4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y+self.ball.height)
        # if ball_vertex1 and ball_vertex2 is not None:
        #     return ball_vertex1, ball_vertex2
        # if ball_vertex2 and ball_vertex4 is not None:
        #     return ball_vertex2, ball_vertex4
        # if ball_vertex4 and ball_vertex3 is not None:
        #     return ball_vertex4 and ball_vertex3
        # if ball_vertex4 and ball_vertex1 is not None:
        #     return ball_vertex4 and ball_vertex1
        if ball_vertex1 is not None:
            return ball_vertex1
        if ball_vertex2 is not None:
            return ball_vertex2
        if ball_vertex3 is not None:
            return ball_vertex3
        if ball_vertex4 is not None:
            return ball_vertex4

    # def get_dx(self):
    #     if random.random() > 0.5:
    #         self.__dx = -self.__dx
