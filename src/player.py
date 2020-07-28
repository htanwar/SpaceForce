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
        self.msec_to_climb = 2
        self.image = pygame.transform.scale(pygame.image.load("images/character/player1.png"), (self.width, self.height))
        self.animation = []

    def update_display(self, win, climb_duration, climb_speed, sink_speed, frames = 1.0):
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
