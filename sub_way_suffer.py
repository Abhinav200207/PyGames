import pygame as py
import random 

py.init() #initilizing pygame  #imp

#display
screen_width = 600
screen_height = 750
game_display=py.display.set_mode((screen_width, screen_height)) #imp

# Game Title
py.display.set_caption("subwaysuffer")  #imp
py.display.update()  #imp

# py.Color
green=(105, 134, 86)
red=(255, 0, 0, 0.541)
yellow=(229, 255, 0, 0.918)


#some game specific variables
#
exit_game = False
game_over = False
#
obj_x = random.randint(0,600)
obj_y = 650
obj_size=50
steps=50
#
obsticles_y=0
obsticles_y1=0
obsticles_x=random.randint(0,500)
obsticles_x1=random.randint(0,500)
obsticles_size=100
obsticles_velocity=10
#
fps=60
score=0



clock = py.time.Clock()


#main game loop
while not exit_game:
    game_display.fill(green)  #background color
    for event in py.event.get():  #imp
        if event.type == py.QUIT:  #imp
            exit_game = True
        
        #obj moment
        
        if event.type == py.KEYDOWN:
            if event.key == py.K_RIGHT:
                obj_x=obj_x+steps
        
            if event.key == py.K_LEFT:
                obj_x=obj_x-steps
    
        ##############

    # obsticle moment  
    obsticles_y+=10
    obsticles_y1+=10
    #reset location of obsticle
    if obsticles_y==850:
        obsticles_y=0
        obsticles_y1=0
        obsticles_x=random.randint(0,600)
        obsticles_x1=random.randint(0,600)
        #update score
        score+=1
        print(score)

    if (abs(obsticles_y-obj_y)<50 and abs(obsticles_x-obj_x)<50) or (abs(obsticles_y1-obj_y)<50 and abs(obsticles_x1-obj_x)<50) :
        print("Touched")
    
    
    #obj creations
    num=random.randint(-30,30)
    num1=random.randint(-30,30)
    
    py.draw.rect(game_display, red, [obj_x, obj_y, obj_size, obj_size])
    py.draw.rect(game_display, yellow, [obj_x+17, obj_y+17, obj_size/3, obj_size/3])
    py.draw.rect(game_display, red, [obj_x-17, obj_y+17-num, obj_size/3, obj_size/3])
    py.draw.rect(game_display, red, [obj_x+51, obj_y+17+num, obj_size/3, obj_size/3])
    py.draw.rect(game_display, red, [obj_x, obj_y+num1, obj_size/3, obj_size/3])
    py.draw.rect(game_display, red, [obj_x+34, obj_y-num1, obj_size/3, obj_size/3])

    #############
   
    py.draw.rect(game_display, yellow, [obsticles_x, obsticles_y, obsticles_size, obsticles_size])
    py.draw.rect(game_display, yellow, [obsticles_x, obsticles_y-120, obsticles_size, obsticles_size])
    py.draw.rect(game_display, red, [obsticles_x+40, obsticles_y-23, obsticles_size/5, obsticles_size/5])

    py.draw.rect(game_display, yellow, [obsticles_x1, obsticles_y1, obsticles_size, obsticles_size])
    py.draw.rect(game_display, yellow, [obsticles_x1, obsticles_y1-120, obsticles_size, obsticles_size])
    py.draw.rect(game_display, red, [obsticles_x1+40, obsticles_y1-23, obsticles_size/5, obsticles_size/5])
    
    py.display.update()
    clock.tick(fps)

py.quit()
quit()   


