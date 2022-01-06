import pygame as py
import random
import math

py.init()


# Creating window
display_width = 800
display_hight = 800
gameWindow = py.display.set_mode((display_width, display_hight))
py.display.set_caption("GAME")  # name
py.display.update()


# color
black = (0, 0, 0)
blue = (76, 0, 255)
green = (105, 134, 86)
red = (255, 0, 0, 0.541)
yellow = (229, 255, 0, 0.918)
white = (255, 255, 255)

# Game specific variables
exit_game = True
fps = 30
x1=350
y1=200
r1=20
x2=400
y2=600
r2=50
g=9.8
t=0
v1=5
v2=0
start_angle=math.pi
end_angle=0
linewidth=5

clock = py.time.Clock()
# Creating a game loop
while exit_game:
    gameWindow.fill(black)
    for event in py.event.get():
        if event.type == py.QUIT:
            exit_game = False
    
    # x=speed*time =g*t*t
    t+=0.1
    if (1>=(((x2-x1)*(x2-x1))/((r1+r2)*(r1+r2)))) and (y1) < y2-(r1+r2)*math.sqrt(1-(((x2-x1)*(x2-x1))/((r1+r2)*(r1+r2)))):
        y1=y1+(v1*t)
        # x1=x1+(v2*t)
    elif (1>(((x2-x1)*(x2-x1))/((r1+r2)*(r1+r2)))) and y2-(r1+r2)*math.sqrt(1-(((x2-x1)*(x2-x1))/((r1+r2)*(r1+r2)))) < (y1) < y2:
        v2=2*v1*(math.sqrt(1-(((x2-x1)*(x2-x1))/((r1+r2)*(r1+r2)))))*((x2-x1)/(r1+r2))
        v1=v1*(2*((x2-x1)**(2)/(r1+r2)**(2))-1)  
        x1=x1-(v2*t)
        y1=y1+(v1*t)
    if y1 >= y2:
        y1=y1+(v1*t)      
    py.draw.circle(gameWindow,green,(x1,y1),r1)
    py.draw.circle(gameWindow,white,(x2,y2),r2)
    py.display.update()
    clock.tick(fps)  


py.quit()
quit()
