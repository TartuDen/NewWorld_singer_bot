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

        if pg.locateCenterOnScreen("img\\w.PNG",confidence=c, region=(765,1030,300,60)):
            # print(c, 'w')
            keyboard.tap("w")
        elif pg.locateCenterOnScreen("img\\a.PNG",confidence=c, region=(765,1076,300,60)):
            # print(c, 'a')
            keyboard.tap("a")
        elif pg.locateCenterOnScreen("img\\s.PNG",confidence=c, region=(765,1120,300,60)):
            # print(c, 's')
            keyboard.tap("s")
        elif pg.locateCenterOnScreen("img\\d.PNG",confidence=c, region=(765,1164,300,60)):
            # print(c, 'd')
            keyboard.tap("d")
        elif pg.locateCenterOnScreen("img\\LR.PNG",confidence=c, region=(765,1108,150,70)):
            print(c, 'LR')
            pg.press("left")
            pg.press("right")
        elif pg.locateCenterOnScreen("img\\sp.PNG",confidence=c, region=(765,1200,150,60)):
            print(c, 'space')
            pg.press("space")
        elif pg.locateCenterOnScreen("img\\e.PNG",confidence=c, region=(1458,835,30,30)):
            print(c, 'e')
            keyboard.tap("e")


# while True:
#     for c in range(9,6,-1):
#         c = c / 10
#         w = pg.locateCenterOnScreen("img\\w.PNG",confidence=c)
#         if w:
#             print(c, 'w ',w)



# Point(x=765, y=1047)
# Point(x=866, y=1255)

# Point(x=778, y=1106) A
# Point(x=778, y=1150) S
# Point(x=783, y=1194) D
# Point(x=781, y=1228) SPACE
# Point(x=1458, y=839) E start again

