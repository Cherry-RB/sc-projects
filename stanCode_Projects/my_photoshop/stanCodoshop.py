"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
1.get_pixel_dist：計算某一點的紅綠藍與平均數紅綠藍的距離
2.get_average：得出N張圖中同一個點的平均數紅綠藍list
3.get_best_pixel：比較從1.中得到的距離，得出距離最小的pixel
4.solve： (1). 建立pixels list 收集3張圖中的同1個點
         (2). 建立for loop(在1.的外面，讓每個點可以被找到)
        (3). 用get_best_pixel的function所得到的best pixel(x,y)，讓該pixels[0/1/2].red&green&blue取代result中的每個點


"""
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
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
    color_dis = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** 0.5
    return color_dis


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    avg_red = 0
    avg_green = 0
    avg_blue = 0
    # 在pixels list上一個個找過去，獲得它的rgb值
    for i in range(len(pixels)):
        avg_red += pixels[i].red
        avg_green += pixels[i].green
        avg_blue += pixels[i].blue
    # 獲得平均數
    avg_red /= len(pixels)
    avg_green /= len(pixels)
    avg_blue /= len(pixels)
    rgb_list = [int(avg_red), int(avg_green), int(avg_blue)]
    return rgb_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # 從pixels list中各自得到rgb的平均數，儲存在3個變數中
    red_avg = get_average(pixels)[0]
    green_avg = get_average(pixels)[1]
    blue_avg = get_average(pixels)[2]
    # 一個個找pixels list上的點，找出其與平均數距離是最小的值，並把該「位置」用另一個變數儲存起來
    distance = get_pixel_dist(pixels[0], red_avg, green_avg, blue_avg)
    index = 0
    for i in range(1, len(pixels)):
        if get_pixel_dist(pixels[i], red_avg, green_avg, blue_avg) <= distance:
            distance = get_pixel_dist(pixels[i], red_avg, green_avg, blue_avg)
            index = i
    # 回饋最小距離的pixel
    best = pixels[index]
    return best


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

    # (2). 建立for loop(在1.的外面，讓每個點可以被找到)
    for x in range(width):  # 平面上每一點都找
        for y in range(height):
            pixel_new = result.get_pixel(x, y)  # 設立好新圖的座標
            # (1). 建立pixels list 收集3張圖中的同1個點
            pixels = []
            for i in range(len(images)):  # 有N 張圖...所以要找 N 次
                pixels += [images[i].get_pixel(x, y)]  # 擁有不同圖、同一個座標的pixels之list，要記得[]!!!!!
                # 也可以變成：
                # p = images[i].get_pixel(x, y)
                # pixels.append(p)  ~~卡題關鍵
            # (3). 用get_best_pixel的function所得到的best pixel(x,y)，讓該pixels[0/1/2].red&green&blue取代result中的每個點
            best = get_best_pixel(pixels)  # the best pixel(x, y)距離最小的座標  # 找到在pixels中最適合的座標(N張圖的其中一張)
            pixel_new.red = best.red
            pixel_new.green = best.green
            pixel_new.blue = best.blue
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    # green_pixel = SimpleImage.blank(20, 20, "green").get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, "red").get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, "blue").get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    # green_pixel = SimpleImage.blank(20, 20, "green").get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, "red").get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, "blue").get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)
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
