import pyautogui as pg
import time
from pynput.keyboard import Key, Controller



# for i in range(4):
#     time.sleep(10)
#     print(pg.position())



keyboard=Controller()

while True:
    pg.leftClick()
    for c in range(8,6,-1):
        c = c / 10
        if pg.locateCenterOnScreen("img\\a.PNG",confidence=c, region=(765,1076,300,60)):
            print(c, 'a')
            keyboard.tap("a")
        elif pg.locateCenterOnScreen("img\\s.PNG",confidence=c, region=(765,1120,300,60)):
            print(c, 's')
            keyboard.tap("s")
        elif pg.locateCenterOnScreen("img\\d.PNG",confidence=c, region=(765,1164,300,60)):
            print(c, 'd')
            keyboard.tap("d")
        elif pg.locateCenterOnScreen("img\\LR.PNG",confidence=c, region=(765,1076,300,70)):
            print(c, 'LR')
            pg.click(button='left')
            pg.click(button='right')




# Point(x=765, y=1047)
# Point(x=866, y=1255)

# Point(x=778, y=1106) A
# Point(x=778, y=1150) S
# Point(x=783, y=1194) D
# Point(x=781, y=1228) SPACE
