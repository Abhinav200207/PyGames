import pygame as py
import random

from pygame.constants import K_LEFT, K_RIGHT, K_a, K_d
py.init()


# Creating window
display_width = 1200
display_hight = 600
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
fps = 400
x=0
y=0


clock = py.time.Clock()
# Creating a game loop
while exit_game:
    gameWindow.fill(black)
    for event in py.event.get():
        if event.type == py.QUIT:
            exit_game = False
    
    # y+=((x-500)*(x-500))/100
    y=((x-500)*(x-500))/100
    print(y)
    x=x+1
    py.draw.circle(gameWindow,white,(x,y),10)
    py.display.update()
    clock.tick(fps)  


py.quit()
quit()
