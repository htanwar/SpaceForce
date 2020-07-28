#####################################
#     Background and Character      #
#####################################

import pygame
import os

#os.chdir("..")
#print(os.path.abspath(os.curdir))
pygame.init()
background = pygame.image.load("images/background/main_back.png")
background = pygame.transform.scale(background,(1280,720))

def background_(img_x, win):
    rel_x = img_x % background.get_rect().width
    win.blit(background,(rel_x - background.get_rect().width,0))
    if rel_x < 1280:
        win.blit(background, (rel_x,0))


class player_(object):
    def __init__(self):
        self.x = 150
        self.y = 360
        self.height = 125
        self.width = 125
        self.jumping = False
        self.image = pygame.transform.scale(pygame.image.load("images/character/player1.png"), (self.width, self.height))
        self.animation = []
    
    def update_display(self, win):
        win.blit(self.image, (self.x, self.y))
    
    def jumpAnimation(self, win):
        print()
