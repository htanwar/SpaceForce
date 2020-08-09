#####################################
#     Background and Character      #
#####################################

import pygame
import math
import os

# os.chdir("..")
# print(os.path.abspath(os.curdir))
pygame.init()
base_image_dir = "images"
background = pygame.image.load(base_image_dir + "/background/main_back.png")
background = pygame.transform.scale(background, (1280, 720))


def background_(img_x, win):
    rel_x = img_x % background.get_rect().width
    win.blit(background, (rel_x - background.get_rect().width, 0))
    if rel_x < 1280:
        win.blit(background, (rel_x, 0))


class player_(object):
    def __init__(self, grayscaleBool):
        if grayscaleBool:
            self.base_image_dir = 'grayscaleImages'
        else:
            self.base_image_dir = 'images'
        self.x = 150
        self.y = 360
        self.height = 125
        self.width = 125
        self.msec_to_climb = 2
        self.image = pygame.transform.scale(
            pygame.image.load(self.base_image_dir + "/character/player1.png").convert_alpha(),
            (self.width, self.height))
        self.original = pygame.transform.scale(
            pygame.image.load(self.base_image_dir + "/character/player1.png").convert_alpha(),
            (self.width, self.height))
        self.mask = pygame.mask.from_surface(
            pygame.image.load(self.base_image_dir + "/character/player1.png").convert_alpha())
        self.animation = [pygame.image.load(self.base_image_dir + "/animation/f1.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f2.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f3.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f4.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f5.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f6.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f7.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f8.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f9.png")]

    def update_display(self, win, climb_duration, climb_speed, sink_speed, frames=1.0):
        '''
        Display the character and includes jumping mechanic
        '''
        if self.msec_to_climb > 0:
            frac_climb = 1 - self.msec_to_climb / climb_duration
            self.y -= (climb_speed * self.frames_to_msec(frames) * (1 - math.cos(frac_climb * math.pi)))
            self.msec_to_climb -= self.frames_to_msec(frames)
        else:
            self.y += sink_speed * self.frames_to_msec(frames)
        win.blit(self.image, (self.x, self.y))

    def frames_to_msec(self, frames, fps=60):
        """Convert frames to milliseconds at the specified framerate.
        Arguments:
        frames: How many frames to convert to milliseconds.
        fps: The framerate to use for conversion.  Default: FPS.
        """
        return 1000.0 * frames / fps

    def msec_to_frames(self, milliseconds, fps=60):
        """Convert milliseconds to frames at the specified framerate.
        Arguments:
        milliseconds: How many milliseconds to convert to frames.
        fps: The framerate to use for conversion.  Default: FPS.
        """
        return fps * milliseconds / 1000.0

    def explosion_fx(self, win, backg, img_x, i):
        self.image = pygame.transform.scale(self.animation[i], (210, 210))
        win.blit(self.image, (self.x, self.y))

    def player_restart(self):
        self.x = 150
        self.y = 360
        self.height = 125
        self.width = 125
        self.msec_to_climb = 2
        self.image = self.original

    def grayscale(self):
        if self.base_image_dir == 'images':
            self.base_image_dir = 'grayscaleImages'
        else:
            self.base_image_dir = 'images'
        self.animation = [pygame.image.load(self.base_image_dir + "/animation/f1.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f2.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f3.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f4.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f5.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f6.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f7.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f8.png"),
                          pygame.image.load(self.base_image_dir + "/animation/f9.png")]

    def choose_character(self, color_blind, p1, p2):
        if color_blind:
            if p1:
                self.image = pygame.transform.scale(
                    pygame.image.load(self.base_image_dir + "/character/cb_player1.png").convert_alpha(),
                    (self.width, self.height))
                self.original = pygame.transform.scale(
                    pygame.image.load(self.base_image_dir + "/character/cb_player1.png").convert_alpha(),
                    (self.width, self.height))
            elif p2:
                self.image = pygame.transform.scale(
                    pygame.image.load(self.base_image_dir + "/character/cb_player2.png").convert_alpha(),
                    (self.width, self.height))
                self.original = pygame.transform.scale(
                    pygame.image.load(self.base_image_dir + "/character/cb_player2.png").convert_alpha(),
                    (self.width, self.height))
        else:
            if p2:
                self.image = pygame.transform.scale(
                    pygame.image.load(self.base_image_dir + "/character/player2.png").convert_alpha(),
                    (self.width, self.height))
                self.original = pygame.transform.scale(
                    pygame.image.load(self.base_image_dir + "/character/player2.png").convert_alpha(),
                    (self.width, self.height))
            else:
                self.image = pygame.transform.scale(
                    pygame.image.load(self.base_image_dir + "/character/player1.png").convert_alpha(),
                    (self.width, self.height))
                self.original = pygame.transform.scale(
                    pygame.image.load(self.base_image_dir + "/character/player1.png").convert_alpha(),
                    (self.width, self.height))
