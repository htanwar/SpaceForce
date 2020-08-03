###########################
#     Main - Playing      #
###########################
import pygame
import sys
import math
import random
import time
from src import player
from src import main_menu
from src import obstacles

def main():
    # Initialize Game
    pygame.init()
    WIDTH, HEIGHT = 1280, 720
    win = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Space Force")
    win.fill((0,0,0))

    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.3
    CLIMB_DURATION = 333.3

    #Initialize variables
    playing = False
    inmenu = True
    FPS = 60
    clock = pygame.time.Clock()
    img_x = 0

    music = pygame.mixer.music.load("sound/song.mp3")
    explosion_sound = pygame.mixer.Sound("sound/explosion.wav")
    jump_sound = pygame.mixer.Sound("sound/jump.wav")
    point_sound = pygame.mixer.Sound("sound/point.wav")

    jump_sound.set_volume(0.40)
    point_sound.set_volume(0.50)
    explosion_sound.set_volume(0.50)

    score = 0
    scoreCheck = True
    player1 = player.player_()

    mainMenu = main_menu.mainMenu()

    allObstacles = createObstacles()
    
    start_area = pygame.Rect(50,355, 180, 75)
    settings_area = pygame.Rect(50,435, 180, 75)
    quit_area = pygame.Rect(50,515, 180, 75)
    
    fontPlayScreen = pygame.font.Font("images/fonts/ALBAS.ttf", 40)
    logo = pygame.image.load("images/background/spaceForceLogo.png").convert_alpha()
    bkg = pygame.transform.scale(pygame.image.load("images/background/main_back.png").convert_alpha(), (2713, 720))
    button_sprite = pygame.image.load("images/ui/GreenBtn1.png").convert_alpha()
    
    start_ = fontPlayScreen.render("Start", True, (255,255,255))
    settings_ = fontPlayScreen.render("Options", True, (255,255,255))
    quit_game_ = fontPlayScreen.render("Exit", True, (255,255,255))

    
    click = False
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    while inmenu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1:
                    click = True
        win.fill((0,0,0))
        
        win.blit(bkg, (0,0))
        win.blit(logo, (-20, 50))
        win.blit(button_sprite, (50,355))
        win.blit(start_, (60, 360))
        win.blit(button_sprite, (50,435))
        win.blit(settings_, (60, 440))
        win.blit(button_sprite, (50,515))
        win.blit(quit_game_, (60, 520))
        pygame.display.update()
        
        mx, my = pygame.mouse.get_pos()
        if start_area.collidepoint((mx,my)) and click:
            mainMenu.tutorial(win)
            inmenu = False
            playing = True
        elif settings_area.collidepoint((mx,my)) and click:
            settings(win,clock)
        elif quit_area.collidepoint((mx,my)) and click:
            pygame.quit()
            sys.exit()
        click = False
        

    while playing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif (event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
                player1.msec_to_climb = CLIMB_DURATION
                jump_sound.play()

        player.background_(img_x, win)
        player1.update_display(win, CLIMB_DURATION, CLIMB_SPEED, SINK_SPEED)
        
        for r in allObstacles:
            if r.x1 < -300:
                r.x1 = 1500
                r.x2 = 1500
                r.randomize_size()
                scoreCheck = True
            if r.x1 < player1.x and scoreCheck == True:
                score += 1
                point_sound.play()
                scoreCheck = False
            r.display_object(win)
        mainMenu.score(win, score)

        img_x -= 5
        pygame.display.update()

        '''
        Checks for collision and adds collision fx
        '''
        if checkCollisions(player1, allObstacles):
            c_ = 0
            explosion_sound.play()
            time.sleep(.100)
            while (c_ < 40):
                player.background_(img_x, win)
                for r in allObstacles:
                    r.display_object2(win)
                player1.explosion_fx(win, player, img_x, c_//5)
                pygame.display.update()
                c_+=1
            mainMenu.game_over(win)

def settings(win,clock):
    running = True
    
    fontPlayScreen = pygame.font.Font("images/fonts/ALBAS.ttf", 40)
    
    bkg = pygame.transform.scale(pygame.image.load("images/background/main_back.png").convert_alpha(), (2713, 720))
    button_sprite = pygame.image.load("images/ui/GreenBtn1.png").convert_alpha()
    start_ = fontPlayScreen.render("Options", True, (255,255,255))
    back_ = fontPlayScreen.render("Back", True, (255,255,255))
    
    back_area = pygame.Rect(50,600, 180, 75)
    
    click = False
    
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1:
                    click = True

        win.fill((0,0,0))
        win.blit(bkg, (0,0))
        win.blit(start_, (60, 50))
        win.blit(button_sprite, (50,600))
        win.blit(back_, (60, 605))
        
        mx, my = pygame.mouse.get_pos()
        if back_area.collidepoint((mx,my)) and click:
            running = False
        
        click = False
        
        pygame.display.update()
        clock.tick(60)

def createObstacles():
    '''
    Creates initial list of obstacles

    '''
    rocks = obstacles.obstacles()

    rock2 = obstacles.obstacles()
    rock2.x1 = 1920
    rock2.x2 = 1920
    rock2.randomize_size()

    rock3 = obstacles.obstacles()
    rock3.x1 = 2560
    rock3.x2 = 2560
    rock3.randomize_size()

    return [rocks, rock2, rock3]

def checkCollisions(player, rocks):
    '''
    Checks if either of the obstacles collided with the player

    '''
    for r in rocks:
        dist1 = math.hypot( (int(player.x) + 63) - (r.x1 + r.width //2) , (int(player.y) + 63) - (r.y1 + r.width //2) )
        dist2 = math.hypot( (int(player.x) + 63) - (r.x2 + r.width //2), (int(player.y) + 63) - (r.y2 + r.width //2 ) )
        if (dist1 <= player.width // 2 + ((r.width - 10) // 2)) or (dist2 <= player.width // 2 + ((r.width - 10) // 2)):
            return True
    return False

main()