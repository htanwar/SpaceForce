###########################
#     Main - Playing      #
###########################
import pygame
import sys
import math
import random
from src import player

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

    player1 = player.player_()

    while playing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif (event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
                player1.msec_to_climb = CLIMB_DURATION

        player.background_(img_x, win)
        player1.update_display(win, CLIMB_DURATION, CLIMB_SPEED, SINK_SPEED)


        img_x -= 5
        pygame.display.update()

main()
