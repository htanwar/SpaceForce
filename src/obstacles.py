#####################################
#        Obstacle and Enemy         #
#####################################

import pygame
import random
import math
import os

class obstacles(object):
    def __init__(self):
        self.x1 = 1280
        self.x2 = 1280
        self.y1 = -100
        self.y2 = 520
        self.width = 200
        self.height = 200
        self.rock1 = pygame.transform.scale(pygame.image.load("images/obstacles/rock11.png"), (self.width, self.height))
        self.rock2 = pygame.transform.scale(pygame.image.load("images/obstacles/rock11.png"), (self.width, self.height))
        self.orig1 = pygame.transform.scale(pygame.image.load("images/obstacles/rock11.png"), (self.width, self.height))
        self.orig2 = pygame.transform.scale(pygame.image.load("images/obstacles/rock11.png"), (self.width, self.height))
        self.coordinates = (self.x1, self.x2, self.width, self.height)

    def display_object(self, win):
        self.x1 -= 5
        self.x2 -= 5
        win.blit(self.rock1, (self.x1, self.y1))
        win.blit(self.rock2, (self.x2, self.y2))

    def randomize_size(self):
        f  = random.randint(0, 90)
        s = random.randint(0, 90)
        sizeR = random.randint(200, 400)
        self.width = sizeR
        self.height = sizeR
        #self.rock1 = pygame.transform.rotate(pygame.transform.scale(self.orig1, (sizeR, sizeR)), f)
        #self.rock2 = pygame.transform.rotate(pygame.transform.scale(self.orig2, (sizeR, sizeR)), s)
        self.rock1 = pygame.transform.scale(self.orig1, (sizeR, sizeR))
        self.rock2 = pygame.transform.scale(self.orig2, (sizeR, sizeR))
    

