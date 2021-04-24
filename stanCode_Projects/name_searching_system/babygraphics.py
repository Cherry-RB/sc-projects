"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # width (int)：視窗的寬
    # year_index (int)：在YEARS這個list所屬的index
    # x_coordinate (int)：整數，year_index在canvas的x座標
    how_many_years = len(YEARS)
    table_width = width-GRAPH_MARGIN_SIZE*2
    one_col_width = table_width/how_many_years
    where_col_x = GRAPH_MARGIN_SIZE + one_col_width * year_index
    return where_col_x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # 1.畫邊框：
    # 上橫線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # 下橫線
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # 2.畫內部的線：
    # col line
    for year_index in range(len(YEARS)):
        col_x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(col_x, GRAPH_MARGIN_SIZE/4, col_x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE/4)
    # text
        canvas.create_text(col_x + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[year_index]),
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # 之前卡關的原因：至少可以畫出會變色線的線，但剩下的問題：y軸、text出不來

# 題目要點：
    # lookup_names(list)：範例['Kylie', 'Nicholas', 'Sonja']獲得使用者輸入的名字
    # 如果名字的排名在1000以外，把這份資料的排名用"*"代替
    # 每一筆資料(str)："名字 排名"
    # 資料在canvas上的x座標，應該與直線距離TEXT_DX
    # COLORS(list)：曲線顏色順序，循環使用

# 解題思路：
    # 1.從lookup_names(list)中，按照年分一個個找出提到的name在name_data字典裡所對應的排名rank
    #   三大重點：名字(決定線條顏色與數量)、年分(決定x座標)、排名(決定y座標)
    #   (1).一個個取lookup_names(list)中的名字(name)(決定線條顏色與數量)
    #   (2).這條線由有多少個點繪出==有多少個年分，透過兩個list分別儲存變動的x座標與y座標
    #       x座標：固定往右增加
    #       y座標：視該名字在該年分的rank值變動
    # 2.用儲存x座標與y座標的list，把一個個點畫到畫布上，再貼上每一筆對應的data_for_draw(str)："名字 排名"

# 開始解題：

    # 先設需要的變數
    one_col_width = (CANVAS_WIDTH-GRAPH_MARGIN_SIZE*2)/len(YEARS)
    one_col_height = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)
    color_turn = 0
# 1.從lookup_names(list)中，按照年分一個個找出提到的name在name_data字典裡所對應的排名rank
    # (1).一個個取lookup_names(list)中的名字(name)(決定線條顏色與數量)
    for name_num in range(len(lookup_names)):
        line_x_list = []
        line_y_list = []
        data_for_draw = []
        name = lookup_names[name_num]
        # (2).這條線由有多少個點繪出==有多少個年分，透過兩個list分別儲存變動的x座標與y座標
        for year_num in range(len(YEARS)):
            # x座標：固定往右增加
            line_x_list += [TEXT_DX + GRAPH_MARGIN_SIZE + one_col_width * year_num]
            # y座標：視該名字在該年分的rank值變動
            line_y_list_calculate = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            year = YEARS[year_num]  # 獲得要找的年份
            # 大卡關： 超出MAX_RANK & 不存在於name_data 的可能， 大卡關關鍵!!!要加str符號!!!!
            if str(year) in name_data[str(name)]:  # 判斷該年分是否在輸入的名字的資料中
                rank = int(name_data[str(name)][str(year)])  # 獲得排名
                if rank <= 1000:
                    data_for_draw += [str(name) + " " + str(rank)]  # list儲存：資料(str)"名字 排名"，到時候要在畫布上顯現
                    line_y_list_calculate -= ((MAX_RANK - rank) / MAX_RANK) * one_col_height
                else:
                    data_for_draw += [str(name) + " *"]  # 排名在1000以外的，以"*"代替
            else:
                data_for_draw += [str(name) + " *"]
            line_y_list += [line_y_list_calculate]

# 2.用儲存x座標與y座標的list，把一個個點畫到畫布上，再貼上每一筆對應的data_for_draw(str)："名字 排名"
    # 開始畫圖(一個名字一條線，四個點)
        for i in range(len(YEARS)):  # i = 0,1,2,3,4,5,6,7,8,9,10,11，總共12個
            if i >= 1:
                if color_turn > len(COLORS)-1:  # 控制線條顏色：0,1,2,3 vs. 3
                    color_turn = 0
                canvas.create_line(line_x_list[i-1], line_y_list[i-1], line_x_list[i], line_y_list[i],
                                   width=LINE_WIDTH, fill=str(COLORS[color_turn]))  # 0,1,2,3
            canvas.create_text(line_x_list[i]+TEXT_DX, line_y_list[i], text=str(data_for_draw[i]), anchor=tkinter.SW)
        color_turn += 1  # 控制線條顏色


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
