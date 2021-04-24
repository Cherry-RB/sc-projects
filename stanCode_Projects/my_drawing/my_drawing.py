"""
File: my_drawing
Name:Cherry
----------------------
TODO:
1.create the left side of my drawing
2.create the right side of my drawing
3.create the label
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    1.create the left side of my drawing
    2.create the right side of my drawing
    3.create the label
    """
    window = GWindow(512, 238, title="Life of π")
    # white hair
    white_hair = GRect(512, 238)
    white_hair.filled = True
    white_hair.fill_color = "moccasin"
    white_hair.color = "moccasin"
    window.add(white_hair)
    # 1.create the left side of my drawing
    # left side:
    # brown_hair,black_stripe_1~8,lower_eyelid,gold_eye,pupil,small_light,big_light,eyelid_white,eyelid_black.nose
    # brown hair
    brown_hair = GPolygon()
    brown_hair.add_vertex((0, 0))  # 1
    brown_hair.add_vertex((41, 0))
    brown_hair.add_vertex((64, 50))
    brown_hair.add_vertex((47, 84))
    brown_hair.add_vertex((60, 126))  # 5
    brown_hair.add_vertex((77, 158))
    brown_hair.add_vertex((123, 187))
    brown_hair.add_vertex((146, 212))
    brown_hair.add_vertex((183, 166))
    brown_hair.add_vertex((169, 135))  # 10
    brown_hair.add_vertex((191, 92))
    brown_hair.add_vertex((189, 41))
    brown_hair.add_vertex((162, 0))
    brown_hair.add_vertex((256, 0))
    brown_hair.add_vertex((256, 238))  # 15
    brown_hair.add_vertex((82, 238))
    brown_hair.add_vertex((40, 197))
    brown_hair.add_vertex((0, 197))  # 18
    brown_hair.filled = True
    brown_hair.fill_color = "darkorange"
    brown_hair.color = "darkorange"
    window.add(brown_hair)
    # black stripe
    # 1
    black_stripe_1 = GPolygon()
    black_stripe_1.add_vertex((0, 0))  # 1
    black_stripe_1.add_vertex((70, 0))
    black_stripe_1.add_vertex((59, 39))
    black_stripe_1.add_vertex((70, 52))
    black_stripe_1.add_vertex((59, 58))  # 5
    black_stripe_1.add_vertex((59, 80))  # 6
    black_stripe_1.add_vertex((63, 100))
    black_stripe_1.add_vertex((51, 110))
    black_stripe_1.add_vertex((28, 150))
    black_stripe_1.add_vertex((31, 103))  # 10
    black_stripe_1.add_vertex((41, 77))  # 11
    black_stripe_1.add_vertex((42, 52))
    black_stripe_1.add_vertex((20, 66))
    black_stripe_1.add_vertex((19, 107))
    black_stripe_1.add_vertex((0, 150))  # 15
    black_stripe_1.add_vertex((0, 57))
    black_stripe_1.add_vertex((32, 23))
    black_stripe_1.filled = True
    black_stripe_1.color = "black"
    window.add(black_stripe_1)
    # 2
    black_stripe_2 = GPolygon()
    black_stripe_2.add_vertex((30, 152))  # 1
    black_stripe_2.add_vertex((58, 208))
    black_stripe_2.add_vertex((83, 216))
    black_stripe_2.add_vertex((115, 208))
    black_stripe_2.add_vertex((79, 235))  # 5
    black_stripe_2.add_vertex((47, 226))  # 6
    black_stripe_2.filled = True
    black_stripe_2.color = "black"
    window.add(black_stripe_2)
    # 3
    black_stripe_3 = GPolygon()
    black_stripe_3.add_vertex((57, 165))  # 1
    black_stripe_3.add_vertex((73, 190))
    black_stripe_3.add_vertex((121, 188))
    black_stripe_3.add_vertex((85, 166))
    black_stripe_3.add_vertex((89, 178))  # 5
    black_stripe_3.filled = True
    black_stripe_3.color = "black"
    window.add(black_stripe_3)
    # 4
    black_stripe_4 = GPolygon()
    black_stripe_4.add_vertex((85, 167))  # 1
    black_stripe_4.add_vertex((60, 120))
    black_stripe_4.add_vertex((58, 146))
    black_stripe_4.filled = True
    black_stripe_4.color = "black"
    window.add(black_stripe_4)
    # 5
    black_stripe_5 = GPolygon()
    black_stripe_5.add_vertex((62, 100))  # 1
    black_stripe_5.add_vertex((102, 101))
    black_stripe_5.add_vertex((133, 112))
    black_stripe_5.add_vertex((153, 131))
    black_stripe_5.add_vertex((162, 148))  # 5
    black_stripe_5.add_vertex((170, 190))  # 6
    black_stripe_5.add_vertex((149, 212))
    black_stripe_5.add_vertex((141, 178))
    black_stripe_5.add_vertex((121, 176))
    black_stripe_5.add_vertex((101, 164))  # 10
    black_stripe_5.add_vertex((88, 146))  # 11
    black_stripe_5.add_vertex((82, 118))
    black_stripe_5.add_vertex((61, 123))
    black_stripe_5.filled = True
    black_stripe_5.color = "black"
    window.add(black_stripe_5)
    # 6
    black_stripe_6 = GPolygon()
    black_stripe_6.add_vertex((192, 0))  # 1
    black_stripe_6.add_vertex((211, 5))
    black_stripe_6.add_vertex((180, 29))
    black_stripe_6.add_vertex((162, 33))
    black_stripe_6.add_vertex((160, 55))  # 5
    black_stripe_6.add_vertex((145, 61))  # 6
    black_stripe_6.add_vertex((133, 44))
    black_stripe_6.add_vertex((124, 62))
    black_stripe_6.add_vertex((154, 120))
    black_stripe_6.add_vertex((119, 100))  # 10
    black_stripe_6.add_vertex((99, 80))  # 11
    black_stripe_6.add_vertex((71, 67))
    black_stripe_6.add_vertex((92, 65))
    black_stripe_6.add_vertex((99, 47))
    black_stripe_6.add_vertex((104, 50))  # 15
    black_stripe_6.add_vertex((99, 65))  # 16
    black_stripe_6.add_vertex((127, 91))
    black_stripe_6.add_vertex((110, 62))
    black_stripe_6.add_vertex((121, 45))
    black_stripe_6.add_vertex((120, 31))  # 20
    black_stripe_6.add_vertex((130, 18))
    black_stripe_6.add_vertex((162, 19))  # 22
    black_stripe_6.filled = True
    black_stripe_6.color = "black"
    window.add(black_stripe_6)
    # 7
    black_stripe_7 = GPolygon()
    black_stripe_7.add_vertex((256, 0))  # 1
    black_stripe_7.add_vertex((231, 20))
    black_stripe_7.add_vertex((223, 8))
    black_stripe_7.add_vertex((192, 38))
    black_stripe_7.add_vertex((181, 65))  # 5
    black_stripe_7.add_vertex((190, 96))  # 6
    black_stripe_7.add_vertex((180, 126))
    black_stripe_7.add_vertex((191, 124))
    black_stripe_7.add_vertex((195, 102))
    black_stripe_7.add_vertex((211, 89))  # 10
    black_stripe_7.add_vertex((203, 81))  # 11
    black_stripe_7.add_vertex((199, 52))
    black_stripe_7.add_vertex((200, 43))
    black_stripe_7.add_vertex((222, 31))
    black_stripe_7.add_vertex((231, 56))  # 15
    black_stripe_7.add_vertex((225, 76))  # 16
    black_stripe_7.add_vertex((215, 89))
    black_stripe_7.add_vertex((226, 94))
    black_stripe_7.add_vertex((241, 68))
    black_stripe_7.add_vertex((250, 47))  # 20
    black_stripe_7.add_vertex((252, 81))
    black_stripe_7.add_vertex((234, 112))
    black_stripe_7.add_vertex((256, 123))  # 23
    black_stripe_7.filled = True
    black_stripe_7.color = "black"
    window.add(black_stripe_7)
    # 8
    black_stripe_8 = GPolygon()
    black_stripe_8.add_vertex((193, 126))  # 1
    black_stripe_8.add_vertex((189, 144))
    black_stripe_8.add_vertex((216, 121))
    black_stripe_8.add_vertex((225, 99))
    black_stripe_8.add_vertex((208, 117))  # 5
    black_stripe_8.filled = True
    black_stripe_8.color = "black"
    window.add(black_stripe_8)
    # lower-eyelid
    lower_eyelid = GPolygon()
    lower_eyelid.add_vertex((78, 107))  # 1
    lower_eyelid.add_vertex((84, 110))
    lower_eyelid.add_vertex((96, 150))
    lower_eyelid.add_vertex((114, 162))
    lower_eyelid.add_vertex((138, 164))  # 5
    lower_eyelid.add_vertex((154, 168))
    lower_eyelid.add_vertex((160, 150))
    lower_eyelid.add_vertex((159, 187))
    lower_eyelid.add_vertex((137, 167))
    lower_eyelid.add_vertex((114, 165))  # 10
    lower_eyelid.add_vertex((94, 153))
    lower_eyelid.add_vertex((82, 111))
    lower_eyelid.filled = True
    lower_eyelid.color = "thistle"
    lower_eyelid.fill_color = "thistle"
    window.add(lower_eyelid)
    # eye
    # eye-gold_eye
    gold_eye = GOval(52, 50, x=94, y=103)
    gold_eye.filled = True
    gold_eye.color = "gold"
    gold_eye.fill_color = "gold"
    window.add(gold_eye)
    # eye-pupil
    pupil = GOval(13, 12, x=113, y=122)
    pupil.filled = True
    pupil.fill_color = "black"
    window.add(pupil)
    # eye-small_light
    small_light = GOval(4, 4, x=124, y=124)
    small_light.filled = True
    small_light.color = "white"
    small_light.fill_color = "white"
    window.add(small_light)
    # eye-big_light
    big_light = GOval(10, 11, x=104, y=118)
    big_light.filled = True
    big_light.color = "white"
    big_light.fill_color = "white"
    window.add(big_light)
    # eyelid
    # eyelid_white
    eyelid_white = GPolygon()
    eyelid_white.add_vertex((105, 97))
    eyelid_white.add_vertex((133, 101))
    eyelid_white.add_vertex((155, 117))
    eyelid_white.add_vertex((154, 142))
    eyelid_white.add_vertex((126, 115))
    eyelid_white.add_vertex((93, 107))
    eyelid_white.filled = True
    eyelid_white.fill_color = "burlywood"
    eyelid_white.color = "burlywood"
    window.add(eyelid_white)
    # eyelid_black
    eyelid_black = GPolygon()
    eyelid_black.add_vertex((91, 100))
    eyelid_black.add_vertex((129, 108))
    eyelid_black.add_vertex((157, 132))
    eyelid_black.add_vertex((156, 147))
    eyelid_black.add_vertex((126, 120))
    eyelid_black.add_vertex((91, 111))
    eyelid_black.add_vertex((87, 104))
    eyelid_black.filled = True
    eyelid_black.fill_color = "black"
    window.add(eyelid_black)
    # nose
    nose = GPolygon()
    nose.add_vertex((256, 170))
    nose.add_vertex((256, 238))
    nose.add_vertex((163, 238))
    nose.filled = True
    nose.fill_color = "chocolate"
    nose.color = "chocolate"
    window.add(nose)
    # 2.create the right side of my drawing
    # right side:
    # brown_hair,black_stripe_1~8,lower_eyelid,gold_eye,pupil,small_light,big_light,eyelid_white,eyelid_black,nose
    # brown hair
    brown_hair = GPolygon()
    brown_hair.add_vertex((window.width-1-0, 0))  # 1
    brown_hair.add_vertex((window.width-1-41, 0))
    brown_hair.add_vertex((window.width-1-64, 50))
    brown_hair.add_vertex((window.width-1-47, 84))
    brown_hair.add_vertex((window.width-1-60, 126))  # 5
    brown_hair.add_vertex((window.width-1-77, 158))
    brown_hair.add_vertex((window.width-1-123, 187))
    brown_hair.add_vertex((window.width-1-146, 212))
    brown_hair.add_vertex((window.width-1-183, 166))
    brown_hair.add_vertex((window.width-1-169, 135))  # 10
    brown_hair.add_vertex((window.width-1-191, 92))
    brown_hair.add_vertex((window.width-1-189, 41))
    brown_hair.add_vertex((window.width-1-162, 0))
    brown_hair.add_vertex((window.width-1-256, 0))
    brown_hair.add_vertex((window.width-1-256, 238))  # 15
    brown_hair.add_vertex((window.width-1-82, 238))
    brown_hair.add_vertex((window.width-1-40, 197))
    brown_hair.add_vertex((window.width-1-0, 197))  # 18
    brown_hair.filled = True
    brown_hair.fill_color = "darkorange"
    brown_hair.color = "darkorange"
    window.add(brown_hair)
    # black stripe
    # 1
    black_stripe_1 = GPolygon()
    black_stripe_1.add_vertex((window.width-1-0, 0))  # 1
    black_stripe_1.add_vertex((window.width-1-70, 0))
    black_stripe_1.add_vertex((window.width-1-59, 39))
    black_stripe_1.add_vertex((window.width-1-70, 52))
    black_stripe_1.add_vertex((window.width-1-59, 58))  # 5
    black_stripe_1.add_vertex((window.width-1-59, 80))  # 6
    black_stripe_1.add_vertex((window.width-1-63, 100))
    black_stripe_1.add_vertex((window.width-1-51, 110))
    black_stripe_1.add_vertex((window.width-1-28, 150))
    black_stripe_1.add_vertex((window.width-1-31, 103))  # 10
    black_stripe_1.add_vertex((window.width-1-41, 77))  # 11
    black_stripe_1.add_vertex((window.width-1-42, 52))
    black_stripe_1.add_vertex((window.width-1-20, 66))
    black_stripe_1.add_vertex((window.width-1-19, 107))
    black_stripe_1.add_vertex((window.width-1-0, 150))  # 15
    black_stripe_1.add_vertex((window.width-1-0, 57))
    black_stripe_1.add_vertex((window.width-1-32, 23))
    black_stripe_1.filled = True
    black_stripe_1.color = "black"
    window.add(black_stripe_1)
    # 2
    black_stripe_2 = GPolygon()
    black_stripe_2.add_vertex((window.width-1-30, 152))  # 1
    black_stripe_2.add_vertex((window.width-1-58, 208))
    black_stripe_2.add_vertex((window.width-1-83, 216))
    black_stripe_2.add_vertex((window.width-1-115, 208))
    black_stripe_2.add_vertex((window.width-1-79, 235))  # 5
    black_stripe_2.add_vertex((window.width-1-47, 226))  # 6
    black_stripe_2.filled = True
    black_stripe_2.color = "black"
    window.add(black_stripe_2)
    # 3
    black_stripe_3 = GPolygon()
    black_stripe_3.add_vertex((window.width-1-57, 165))  # 1
    black_stripe_3.add_vertex((window.width-1-73, 190))
    black_stripe_3.add_vertex((window.width-1-121, 188))
    black_stripe_3.add_vertex((window.width-1-85, 166))
    black_stripe_3.add_vertex((window.width-1-89, 178))  # 5
    black_stripe_3.filled = True
    black_stripe_3.color = "black"
    window.add(black_stripe_3)
    # 4
    black_stripe_4 = GPolygon()
    black_stripe_4.add_vertex((window.width-1-85, 167))  # 1
    black_stripe_4.add_vertex((window.width-1-60, 120))
    black_stripe_4.add_vertex((window.width-1-58, 146))
    black_stripe_4.filled = True
    black_stripe_4.color = "black"
    window.add(black_stripe_4)
    # 5
    black_stripe_5 = GPolygon()
    black_stripe_5.add_vertex((window.width-1-62, 100))  # 1
    black_stripe_5.add_vertex((window.width-1-102, 101))
    black_stripe_5.add_vertex((window.width-1-133, 112))
    black_stripe_5.add_vertex((window.width-1-153, 131))
    black_stripe_5.add_vertex((window.width-1-162, 148))  # 5
    black_stripe_5.add_vertex((window.width-1-170, 190))  # 6
    black_stripe_5.add_vertex((window.width-1-149, 212))
    black_stripe_5.add_vertex((window.width-1-141, 178))
    black_stripe_5.add_vertex((window.width-1-121, 176))
    black_stripe_5.add_vertex((window.width-1-101, 164))  # 10
    black_stripe_5.add_vertex((window.width-1-88, 146))  # 11
    black_stripe_5.add_vertex((window.width-1-82, 118))
    black_stripe_5.add_vertex((window.width-1-61, 123))
    black_stripe_5.filled = True
    black_stripe_5.color = "black"
    window.add(black_stripe_5)
    # 6
    black_stripe_6 = GPolygon()
    black_stripe_6.add_vertex((window.width-1-192, 0))  # 1
    black_stripe_6.add_vertex((window.width-1-211, 5))
    black_stripe_6.add_vertex((window.width-1-180, 29))
    black_stripe_6.add_vertex((window.width-1-162, 33))
    black_stripe_6.add_vertex((window.width-1-160, 55))  # 5
    black_stripe_6.add_vertex((window.width-1-145, 61))  # 6
    black_stripe_6.add_vertex((window.width-1-133, 44))
    black_stripe_6.add_vertex((window.width-1-124, 62))
    black_stripe_6.add_vertex((window.width-1-154, 120))
    black_stripe_6.add_vertex((window.width-1-119, 100))  # 10
    black_stripe_6.add_vertex((window.width-1-99, 80))  # 11
    black_stripe_6.add_vertex((window.width-1-71, 67))
    black_stripe_6.add_vertex((window.width-1-92, 65))
    black_stripe_6.add_vertex((window.width-1-99, 47))
    black_stripe_6.add_vertex((window.width-1-104, 50))  # 15
    black_stripe_6.add_vertex((window.width-1-99, 65))  # 16
    black_stripe_6.add_vertex((window.width-1-127, 91))
    black_stripe_6.add_vertex((window.width-1-110, 62))
    black_stripe_6.add_vertex((window.width-1-121, 45))
    black_stripe_6.add_vertex((window.width-1-120, 31))  # 20
    black_stripe_6.add_vertex((window.width-1-130, 18))
    black_stripe_6.add_vertex((window.width-1-162, 19))  # 22
    black_stripe_6.filled = True
    black_stripe_6.color = "black"
    window.add(black_stripe_6)
    # 7
    black_stripe_7 = GPolygon()
    black_stripe_7.add_vertex((window.width-1-256, 0))  # 1
    black_stripe_7.add_vertex((window.width-1-231, 20))
    black_stripe_7.add_vertex((window.width-1-223, 8))
    black_stripe_7.add_vertex((window.width-1-192, 38))
    black_stripe_7.add_vertex((window.width-1-181, 65))  # 5
    black_stripe_7.add_vertex((window.width-1-190, 96))  # 6
    black_stripe_7.add_vertex((window.width-1-180, 126))
    black_stripe_7.add_vertex((window.width-1-191, 124))
    black_stripe_7.add_vertex((window.width-1-195, 102))
    black_stripe_7.add_vertex((window.width-1-211, 89))  # 10
    black_stripe_7.add_vertex((window.width-1-203, 81))  # 11
    black_stripe_7.add_vertex((window.width-1-199, 52))
    black_stripe_7.add_vertex((window.width-1-200, 43))
    black_stripe_7.add_vertex((window.width-1-222, 31))
    black_stripe_7.add_vertex((window.width-1-231, 56))  # 15
    black_stripe_7.add_vertex((window.width-1-225, 76))  # 16
    black_stripe_7.add_vertex((window.width-1-215, 89))
    black_stripe_7.add_vertex((window.width-1-226, 94))
    black_stripe_7.add_vertex((window.width-1-241, 68))
    black_stripe_7.add_vertex((window.width-1-250, 47))  # 20
    black_stripe_7.add_vertex((window.width-1-252, 81))
    black_stripe_7.add_vertex((window.width-1-234, 112))
    black_stripe_7.add_vertex((window.width-1-256, 123))  # 23
    black_stripe_7.filled = True
    black_stripe_7.color = "black"
    window.add(black_stripe_7)
    # 8
    black_stripe_8 = GPolygon()
    black_stripe_8.add_vertex((window.width-1-193, 126))  # 1
    black_stripe_8.add_vertex((window.width-1-189, 144))
    black_stripe_8.add_vertex((window.width-1-216, 121))
    black_stripe_8.add_vertex((window.width-1-225, 99))
    black_stripe_8.add_vertex((window.width-1-208, 117))  # 5
    black_stripe_8.filled = True
    black_stripe_8.color = "black"
    window.add(black_stripe_8)
    # lower-eyelid
    lower_eyelid = GPolygon()
    lower_eyelid.add_vertex((window.width-1-78, 107))  # 1
    lower_eyelid.add_vertex((window.width-1-84, 110))
    lower_eyelid.add_vertex((window.width-1-96, 150))
    lower_eyelid.add_vertex((window.width-1-114, 162))
    lower_eyelid.add_vertex((window.width-1-138, 164))  # 5
    lower_eyelid.add_vertex((window.width-1-154, 168))
    lower_eyelid.add_vertex((window.width-1-160, 150))
    lower_eyelid.add_vertex((window.width-1-159, 187))
    lower_eyelid.add_vertex((window.width-1-137, 167))
    lower_eyelid.add_vertex((window.width-1-114, 165))  # 10
    lower_eyelid.add_vertex((window.width-1-94, 153))
    lower_eyelid.add_vertex((window.width-1-82, 111))
    lower_eyelid.filled = True
    lower_eyelid.color = "thistle"
    lower_eyelid.fill_color = "thistle"
    window.add(lower_eyelid)
    # eye
    # eye-gold_eye
    gold_eye = GOval(52, 50, x=270+94, y=103)
    gold_eye.filled = True
    gold_eye.color = "gold"
    gold_eye.fill_color = "gold"
    window.add(gold_eye)
    # eye-pupil
    pupil = GOval(13, 12, x=270+113, y=122)
    pupil.filled = True
    pupil.fill_color = "black"
    window.add(pupil)
    # eye-small_light
    small_light = GOval(4, 4, x=255+124, y=124)
    small_light.filled = True
    small_light.color = "white"
    small_light.fill_color = "white"
    window.add(small_light)
    # eye-big_light
    big_light = GOval(10, 11, x=290+104, y=118)
    big_light.filled = True
    big_light.color = "white"
    big_light.fill_color = "white"
    window.add(big_light)
    # eyelid
    # eyelid_white
    eyelid_white = GPolygon()
    eyelid_white.add_vertex((window.width-1-105, 97))
    eyelid_white.add_vertex((window.width-1-133, 101))
    eyelid_white.add_vertex((window.width-1-155, 117))
    eyelid_white.add_vertex((window.width-1-154, 142))
    eyelid_white.add_vertex((window.width-1-126, 115))
    eyelid_white.add_vertex((window.width-1-93, 107))
    eyelid_white.filled = True
    eyelid_white.fill_color = "burlywood"
    eyelid_white.color = "burlywood"
    window.add(eyelid_white)
    # eyelid_black
    eyelid_black = GPolygon()
    eyelid_black.add_vertex((window.width-1-91, 100))
    eyelid_black.add_vertex((window.width-1-129, 108))
    eyelid_black.add_vertex((window.width-1-157, 132))
    eyelid_black.add_vertex((window.width-1-156, 147))
    eyelid_black.add_vertex((window.width-1-126, 120))
    eyelid_black.add_vertex((window.width-1-91, 111))
    eyelid_black.add_vertex((window.width-1-87, 104))
    eyelid_black.filled = True
    eyelid_black.fill_color = "black"
    window.add(eyelid_black)
    # nose
    nose = GPolygon()
    nose.add_vertex((window.width-1-256, 170))
    nose.add_vertex((window.width-1-256, 238))
    nose.add_vertex((window.width-1-163, 238))
    nose.filled = True
    nose.fill_color = "chocolate"
    nose.color = "chocolate"
    window.add(nose)
    # 3.create the label
    # label
    label = GLabel("Life", x=210, y=50)
    label.font = "Courier-30-bold"
    label.color = "white"
    window.add(label)
    label = GLabel("of", x=235, y=95)
    label.font = "Courier-25-bold"
    label.color = "white"
    window.add(label)
    label = GLabel("π", x=228, y=180)
    label.font = "Courier-70-bold"
    label.color = "white"
    window.add(label)


if __name__ == '__main__':
    main()
