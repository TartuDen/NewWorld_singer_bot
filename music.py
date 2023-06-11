import pyautogui as pg
import time
from pynput.keyboard import Key, Controller



# for i in range(4):
#     time.sleep(10)
#     print(pg.position())



keyboard=Controller()

while True:
    for c in range(8,6,-1):
        c = c / 10

        if pg.locateCenterOnScreen("img\\w.PNG",confidence=c, region=(765,1030,200,60)):
            # print(c, 'w')
            keyboard.tap("w")
        elif pg.locateCenterOnScreen("img\\a.PNG",confidence=c, region=(765,1076,200,60)):
            # print(c, 'a')
            keyboard.tap("a")
        elif pg.locateCenterOnScreen("img\\s.PNG",confidence=c, region=(765,1120,200,60)):
            # print(c, 's')
            keyboard.tap("s")
        elif pg.locateCenterOnScreen("img\\d.PNG",confidence=c, region=(765,1164,200,60)):
            # print(c, 'd')
            keyboard.tap("d")
        # elif pg.locateCenterOnScreen("img\\LR.PNG",confidence=c, region=(765,1076,300,70)):
        #     print(c, 'LR')
        #     pg.press("left")
        #     pg.press("right")
        elif pg.locateCenterOnScreen("img\\sp.PNG",confidence=c, region=(765,1196,200,60)):
            print(c, 'space')
            pg.press("space")
        # elif pg.locateCenterOnScreen("img\\e.PNG",confidence=c, region=(1424,808,60,60)):
        #     # print(c, 'e')
        #     keyboard.tap("e")


# while True:
#     for c in range(9,6,-1):
#         c = c / 10
#         e = pg.locateCenterOnScreen("img\\e.PNG",confidence=c)
#         if e:
#             print(c, 'e ',e)



# Point(x=765, y=1047)
# Point(x=866, y=1255)

# Point(x=778, y=1106) A
# Point(x=778, y=1150) S
# Point(x=783, y=1194) D
# Point(x=781, y=1228) SPACE
# Point(x=1458, y=839) E start again
# 0.9 e  Point(x=1454, y=838)

# 0.8 w  Point(x=1820, y=1066)
# 0.7 sp  Point(x=705, y=1226)
# 0.9 a  Point(x=1304, y=1107)
# 0.9 sp  Point(x=708, y=1227)
# 0.9 LR  Point(x=1531, y=1108)
# 0.8 a  Point(x=783, y=1106)
# 0.8 s  Point(x=1561, y=1148)
# 0.8 d  Point(x=1728, y=1189)
# 0.8 sp  Point(x=707, y=1226)
# 0.7 s  Point(x=775, y=1148)
# 0.7 d  Point(x=935, y=1188)
# 0.7 sp  Point(x=1096, y=1227)
# 0.9 d  Point(x=1352, y=1189)
# 0.8 a  Point(x=1767, y=1106)
# 0.8 s  Point(x=1313, y=1148)
# 0.8 d  Point(x=841, y=1189)
# 0.8 sp  Point(x=1901, y=1227)
# 0.7 a  Point(x=962, y=1105)
# 0.7 s  Point(x=1131, y=1148)
# 0.7 d  Point(x=1573, y=1188)
# 0.7 sp  Point(x=1109, y=1227)
# 0.9 a  Point(x=1395, y=1107)
# 0.9 d  Point(x=774, y=1189)
# 0.7 sp  Point(x=1024, y=268)