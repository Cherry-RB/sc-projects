"""
File: draw_line
Name:Cherry
-------------------------
TODO:
1.click at the first time(times==0):a circle appears
2.click at the second time(times==1):the line appears and the circle disappears
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
circle = GOval(10, 10)
times = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(mouse):
    global times
    # 1.click at the first time(times==0):a circle appears
    if times == 0:
        window.add(circle, mouse.x - circle.width / 2, mouse.y - circle.height / 2)
        times += 1
    # 2.click at the second time(times==1):the line appears and the circle disappears
    elif times == 1:
        line = GLine(circle.x + circle.width/2, circle.y + circle.height/2, mouse.x, mouse.y)
        window.add(line)
        window.remove(circle)
        times -= 1


# wrong code:
#
#     circle_exist = window.get_object_at(circle.x, circle.y)
#     if circle_exist is None:
#         onmouseclicked(click_1)
#     if circle_exist is not None:
#         onmouseclicked(click_2)
#
#
# def click_1(m):
#     window.add(circle, m.x, m.y)
#
#
# def click_2(m):
#     line = GLine(m.x + circle.width / 2, m.y + circle.height / 2, m.x, m.y)
#     window.add(line)
#     window.remove(circle)


if __name__ == "__main__":
    main()
