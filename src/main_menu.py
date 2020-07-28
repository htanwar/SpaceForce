#####################################
#             Main Menu             #
#####################################

import pygame
import os

class mainMenu(object):
    def __init__(self):
        self.fontPlayScreen = pygame.font.Font('freesansbold.ttf', 40)
        self.playScreenIntro = False

    def tutorial(self, win):
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