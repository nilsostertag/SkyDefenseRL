import env.configloader as configloader
import pygame
import random
import math
import numpy as np

from env.configloader import ConfigLoader

cfg = ConfigLoader()
WIDTH = cfg.config['width']
HEIGHT = cfg.config['height']
NUM_TARGETS = cfg.config['num_targets']

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
GRAY = (180, 180, 180)

class Turret():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 45  # Startwinkel

    def rotate(self, delta):
        self.angle = max(0, min(90, self.angle + delta))

    def draw(self, surface):
        base_pos = (int(self.x), HEIGHT - int(self.y))
        length = 100
        rad_angle = math.radians(self.angle)
        end_pos = (
            int(self.x + length * math.cos(rad_angle)),
            HEIGHT - int(self.y + length * math.sin(rad_angle)),
        )
        pygame.draw.line(surface, BLUE, base_pos, end_pos, 6)
        pygame.draw.circle(surface, GRAY, base_pos, 25)