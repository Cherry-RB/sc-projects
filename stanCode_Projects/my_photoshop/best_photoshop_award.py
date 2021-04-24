"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def main():
    """
    TODO:ps own figure
    """
    img = SimpleImage('image_contest/P_20201127_235437_001.jpg')
    bg = SimpleImage('image_contest/moon.jpg')
    print(img.height, img.width)
    print(bg.height, bg.width)
    bg.make_as_big_as(img)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            bg_pixel = bg.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue) / 3
            if 500 > x or x > 642:
                if 400 > y or y > 500:
                    if avg > 142:
                        pixel.red = bg_pixel.red
                        pixel.blue = bg_pixel.blue
                        pixel.green = bg_pixel.green
    img.show()


if __name__ == '__main__':
    main()
