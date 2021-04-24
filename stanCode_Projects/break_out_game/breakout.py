"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!

    while True:
        # graphics.click_to_start(graphics.mouse_click)
        if graphics.mouse_click == 1:  # 如果滑鼠開關打開了
            while True:
                graphics.ball_move()  # 球就開始移動
                pause(FRAME_RATE)
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.times += 1  # 死了一次
                    break
                p1 = graphics.ball_touch()  # 在移動的過程中偵測是否撞到物體
                if graphics.ball.y <= graphics.window.height / 2:  # 當球在視窗上半部移動時
                    if p1 is not None:  # 撞到了物體
                        graphics.window.remove(p1)  # 移除掉物體
                        graphics.set_dy()  # 球反彈
                else:
                    if p1 is not None:  # 撞到了物體
                        graphics.set_dy()  # 球反彈
            graphics.window.remove(graphics.ball)  # 球重新從原始位置開始
            graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                y=(graphics.window.height - graphics.ball.height) / 2)
            graphics.mouse_click -= 1  # 開關回到初始值(0)
        pause(FRAME_RATE)


            # dx = graphics.get_dx()


if __name__ == '__main__':
    main()
