import pygame as py
import random
import math

# math.tan()

from pygame.constants import K_LEFT, K_RIGHT, K_a, K_d
py.init()


# Creating window
display_width = 1200
display_hight = 400
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
fps = 50
tank_x1 = 50
tank_y1 = 350
tank_x2 = 1100
tank_y2 = 350
x = 0
y = 350
theta = (math.pi)/6
u = 5
g = 9.8
# y= xtan@ + gx^2/(2u^2cos^2@)


clock = py.time.Clock()
# Creating a game loop
while exit_game:
    gameWindow.fill(green)
    for event in py.event.get():
        if event.type == py.QUIT:
            exit_game = False

    y = 250+((x*math.tan(theta)) +
           ((g*x*x)/(2*u*u*(math.cos(theta)*math.cos(theta)))))/6000
    print(y)
    py.draw.circle(gameWindow, white, (x-100, y), 10)
    x += 10

    py.display.update()
    clock.tick(fps)
