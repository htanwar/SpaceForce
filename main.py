###########################
#     Main - Playing      #
###########################
import pygame
import sys
import math
import random
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
    playing = True
    FPS = 60
    clock = pygame.time.Clock()
    img_x = 0

    score = 0

    player1 = player.player_()

    mainMenu = main_menu.mainMenu()
    mainMenu.tutorial(win)

    allObstacles = createObstacles()

    while playing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif (event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
                player1.msec_to_climb = CLIMB_DURATION

        player.background_(img_x, win)
        player1.update_display(win, CLIMB_DURATION, CLIMB_SPEED, SINK_SPEED)
        #pygame.draw.rect(win, (255,0,0), (player1.x, player1.y, player1.width, player1.height ),2)
        #pygame.draw.circle(win, (255,0,0), (int(player1.x) + 63, int(player1.y)+63), 63, 0) 
        for r in allObstacles:
            if r.x1 < -300:
                r.x1 = 1500
                r.x2 = 1500
                r.randomize_size()
                score += 1
            r.display_object(win)
            #pygame.draw.circle(win, (255,0,0), (r.x1+r.height//2, r.y1+r.height//2),r.height//2,0)
            #pygame.draw.circle(win, (255,0,0), (r.x2+r.height//2, r.y2+r.height//2),r.height//2,0)  
        mainMenu.score(win, score)
        if checkCollisions(player1, allObstacles):
            mainMenu.game_over(win)

        img_x -= 5
        pygame.display.update()


def createObstacles():
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
    for r in rocks:
        dist1 = math.hypot(player.x - r.x1, player.y - r.y1 )
        dist2 = math.hypot(player.x - r.x2, player.y - r.y2 )
        if (dist1 <= player.width // 2 + r.width // 2) or (dist2 <= player.width // 2 + r.width // 2):
            return True
    return False

main()