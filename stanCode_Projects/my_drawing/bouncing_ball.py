"""
File: bouncing_ball
Name:Cherry
-------------------------
TODO:
1. if the ball starts bouncing(mouse_click != 0), click is not useful
2. click to start bouncing until 3 times
3. if the ball leaves the window, it returns to original place
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
times = 0
mouse_click = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = "black"
    ball.color = "black"
    window.add(ball)
    onmouseclicked(click)


def click(mouse):
    global times
    global mouse_click
    # 1.if the ball starts bouncing(mouse_click != 0), click is not useful
    if mouse_click == 0:
        # 2.click to start bouncing until 3 times
        if times != 3:
            mouse_click += 1
            vy = 0
            # 3.if the ball leaves the window, it returns to original place
            while True:
                drop(vy)
                if ball.x >= window.width:
                    times += 1
                    break
            window.add(ball, x=START_X, y=START_Y)
            mouse_click -= 1


def drop(vy):
    while ball.y+ball.height <= window.height:
        vy += GRAVITY
        ball.move(VX, vy)
        pause(DELAY)
    jump(vy)


def jump(vy):
    vy = -vy*REDUCE
    while vy <= 0:
        vy += GRAVITY
        ball.move(VX, vy)
        pause(DELAY)


if __name__ == "__main__":
    main()
