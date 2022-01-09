import pygame as py
import random
from math import sqrt

py.init()  # initilizing pygame  #imp


# color
black = (0, 0, 0)
blue = (76, 0, 255)
green=(105, 134, 86)
red=(255, 0, 0, 0.541)
yellow=(229, 255, 0, 0.918)
white = (255, 255, 255)

# screen
screen_width = 600
screen_height = 600
game_display = py.display.set_mode((screen_width, screen_height))  # imp

# Game Title
py.display.set_caption("universe")  # imp
py.display.update()  # imp

# variables
exit_game = False
fps = 120
x1 = 200
x2 = 200
x3 = 200
increment1 = 1
increment2 = 2
increment3 = 4
multiply1=1
multiply2=1
multiply3=1
clock = py.time.Clock()

# Game Loop
while not exit_game:
    game_display.fill(black)
    for event in py.event.get():
        if event.type == py.QUIT:
            exit_game = True

    
    x1 = x1+(increment1)
    x2 = x2+(increment2)
    x3 = x3+(increment3)
    # x4 = x4+(increment4)
    if (x1 == 400 or x1==200):
        increment1 = ((-1)*(increment1))
        multiply1 = ((-1)*(multiply1))
    if  (x2 == 400 or x2 == 200):
        increment2 = ((-1)*(increment2))    
        multiply2 = ((-1)*(multiply2))
    if  (x3 == 400 or x3 == 200):
        increment3 = ((-1)*(increment3))    
        multiply3 = ((-1)*(multiply3))
    y1 = (int((10000-(x1-300)**2)**(1/2))*(multiply1)+300)
    y2 = (int((10000-(x2-300)**2)**(1/2))*(multiply2)+300)
    y3 = (int((10000-(x3-300)**2)**(1/2))*(multiply3)+300)
    
    print("value",x1,y1,"value",x2,y2,"value",x3,y3,"incre",increment1,"incre",increment2,"incre",increment3)

    py.draw.circle(game_display,white,[300,300],30)
    py.draw.circle(game_display,blue,(x1,y1),10)
    py.draw.circle(game_display,red,(x2+30,y2+30),10)
    py.draw.circle(game_display,green,(x3+60,y3),10)
    py.display.update()
    clock.tick(fps)

py.quit()
quit()
