#####################################
#             Main Menu             #
#####################################

import pygame
import os
import sys


class mainMenu(object):
    def __init__(self):
        self.base_image_dir = 'grayscaleImages'
        self.logo = pygame.image.load(self.base_image_dir + "/background/spaceForceLogo.png").convert_alpha()
        self.bkg = pygame.transform.scale(pygame.image.load(self.base_image_dir + "/background/main_back.png").convert_alpha(),
                                          (2713, 720))
        self.playScreenIntro = False
        self.gameOver = False
        self.highScore = 0

    def tutorial(self, win, scale):
        """
        Shows the intro screen before playing
        """
        self.fontPlayScreen = pygame.font.Font("fonts/ALBAS.ttf", 20 * scale)
        self.playScreenIntro = True
        continue_ = self.fontPlayScreen.render("Press [ Space ] to Start!", True, (255, 255, 255))

        while self.playScreenIntro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            win.fill((0, 0, 0))

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.playScreenIntro = False
            win.blit(continue_, (400, 360))
            pygame.display.update()

    def game_over(self, win, restart, menu, scale):
        """
        Shows the gameover screen

        """
        self.gameOver = True
        continue_ = self.fontPlayScreen.render("Game Over!", True, (255, 255, 255))
        click = False
        while self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            mx, my = pygame.mouse.get_pos()

            win.blit(continue_, (520, 360))
            pygame.display.update()

            if restart.collidepoint((mx, my)) and click:
                return True, False
            if menu.collidepoint((mx, my)) and click:
                return False, True

    def score(self, win, s, scale):
        """
        Displays the score
        """
        self.fontPlayScreen = pygame.font.Font("fonts/ALBAS.ttf", 20 * scale)
        if s > self.highScore:
            self.highScore = s

        continue_ = self.fontPlayScreen.render("Score: " + str(s), True, (255, 255, 255))
        win.blit(continue_, (20, 20))

    def high_score(self, win, scale):
        self.fontPlayScreen = pygame.font.Font("fonts/ALBAS.ttf", 20 * scale)
        continue_ = self.fontPlayScreen.render("High Score: " + str(self.highScore), True, (255, 255, 255))
        win.blit(continue_, (510, 450))
