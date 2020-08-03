#####################################
#             Main Menu             #
#####################################

import pygame
import os
import sys

class mainMenu(object):
    def __init__(self):
        self.fontPlayScreen = pygame.font.Font("images/fonts/ALBAS.ttf", 40)
        self.logo = pygame.image.load("images/background/spaceForceLogo.png").convert_alpha()
        self.bkg = pygame.transform.scale(pygame.image.load("images/background/main_back.png").convert_alpha(), (2713, 720))
        self.playScreenIntro = False
        self.gameOver = False

    def tutorial(self, win):
        '''
        Shows the intro screen before playing
        '''
        self.playScreenIntro = True
        continue_ = self.fontPlayScreen.render("Press [ Space ] to Start!", True, (255,255,255))

        while self.playScreenIntro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            win.fill((0,0,0))

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.playScreenIntro = False
            win.blit(continue_, (400, 360))
            pygame.display.update()
      
    
    def game_over(self, win):
        '''
        Shows the gameover screen

        '''

        self.gameOver= True
        continue_ = self.fontPlayScreen.render("Game Over!", True, (255,255,255))

        while self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            win.fill((0,0,0))
                        
            win.blit(continue_, (520, 360))
            pygame.display.update()
    
    def score(self, win, s):
        '''
        Displays the score
        '''
        continue_ = self.fontPlayScreen.render("Score: "+str(s), True, (255,255,255))
        win.blit(continue_, (20, 20))