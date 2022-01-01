import pygame as py
import random
import math

py.init()
py.mixer.init()
# py.mixer.music.load('')
# py.mixer.music.play()


# Creating window
display_width = 600
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


def game_loop():
    # Game specific variables
    exit_game = True
    game_over = True
    fps = 60
    # for slab
    y_slab = random.randint(0,600)
    x_slab = 580
    init_slab_velocity = 5
    slab_velocity = 0
    comp_slab_y=random.randint(0,600)
    # for ball
    x = 20
    y = 200
    r = 10
    multiplier1= 1
    multiplier2= 1
    v_x = random.randint(5, 9)
    v_y = random.randint(5, 9)
    score=0

    clock = py.time.Clock()

    font = py.font.SysFont(None, 55)

    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, [x,y])

    def comp(x,y,comp_slab_y):
        if (comp_slab_y+50)>y:
            comp_slab_y-=20
        if (comp_slab_y+50)<y:
            comp_slab_y+=20
        return comp_slab_y        


    # Creating a game loop
    while exit_game:
        if not game_over:
            gameWindow.fill(black)
            text_screen("Game Over! bruh", white, 150, 250)
            text_screen("Score: " + str(score * 10), white, 150, 300)

            for event in py.event.get():
                if event.type == py.QUIT:
                    exit_game = False

                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:
                        game_loop() 
        else:
            gameWindow.fill(black)
            for event in py.event.get():
                if event.type == py.QUIT:
                    exit_game = False

                if event.type == py.KEYDOWN:
                    if event.key == py.K_UP:
                        slab_velocity = -init_slab_velocity

                    if event.key == py.K_DOWN:
                        slab_velocity = init_slab_velocity
            
            if x >= 580 and y_slab < y < y_slab + 200 :
                v_x= (-1)*v_x*(1.01)
                # py.mixer.music.load('')

            if x <= 10 and comp_slab_y < y < comp_slab_y + 200:
                v_x= (-1)*v_x*(1.01)
                # py.mixer.music.load('')

            if y <= 0: 
                v_y= (-1)*v_y*(1.01)    
                # py.mixer.music.load('')
            
            if y >= 580:
                v_y= (-1)*v_y*(1.01)
                # py.mixer.music.load('')

            x += v_x
            y += v_y

            comp_slab_y=comp(x,y,comp_slab_y)
            # y_slab=comp(x,y,comp_slab_y)
            y_slab = y_slab + slab_velocity
            if x == 580 or x == 581 or x == 582 or x == 583 or x == 584 or x == 585:
                score+=1
            text_screen("Score: " + str(score * 10), white, 5, 5)
            py.draw.rect(gameWindow, white, [0, comp_slab_y, 20, 100])
            py.draw.rect(gameWindow, white, [x_slab, y_slab, 20, 200])
            py.draw.circle(gameWindow, white, [x, y], r)

            if x>590:
                game_over = False
        py.display.update()
        clock.tick(fps)


    py.quit()
    quit()


game_loop()