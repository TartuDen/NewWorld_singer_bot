import pyautogui as pg
import time
from pynput.keyboard import Key, Controller



# for i in range(4):
#     time.sleep(10)
#     print(pg.position())



keyboard=Controller()


# def cast():
#     start_time = time.time()
#     r = (0,0,2000,1000)
#     pg.mouseDown(button="left")
#     start_t=time.time()
#     for _ in range(100):
#         for c in range(9,6,-1):
#             c = c / 10
#             arrow = pg.locateCenterOnScreen("img_fish\\cast_arrow.png",confidence=c, region=r)
#             point = pg.locateCenterOnScreen("img_fish\\point.png",confidence=c,region=r)
#             if arrow and point:
#                 r = (arrow.x-10, arrow.y-10,20,point.y+7-arrow.y)
#                 print("arrow: ",arrow, 'point: ', point, r, c,time.time() - start_t)
                
#                 if abs(arrow.y-point.y)<20:
#                     print("MAX: ", arrow, point)
#                     pg.mouseUp(button="left")
#                     return(True)

TIME_MAX = 1.90
def cast_initial():
    global TIME_MAX
    pg.mouseDown(button="left")
    time.sleep(TIME_MAX)
    pg.mouseUp(button="left")

def cast1():
    r = (0,0,2000,1000)
    for _ in range(100):
        for c in range(9,6,-1):
            c = c / 10
            floater = pg.locateCenterOnScreen("img_fish\\cast1.png",confidence=c, region=r)
            if floater:
                r = (floater.x-30, floater.y-30,60,60)
                return(r)

def cast2(r):
    while True:
        for c in range(9,6,-1):
            c=c/10
            time_to_hook = pg.locateCenterOnScreen("img_fish\\cast2.png",confidence=c, region=r)
            if time_to_hook:
                return(True)

def pool_the_fish():
    pg.mouseDown(button="left")
    time.sleep(8)
    pg.mouseUp(button="left")
    time.sleep(1)
    pg.mouseDown(button="left")


end_game=False
while not end_game:
    time.sleep(2)
    start = cast_initial()
    where_to_look = cast1()
    hook = cast2(where_to_look)
    if hook:
        pool_the_fish()
 

    end_game=True
    
