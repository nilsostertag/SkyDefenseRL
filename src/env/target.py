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
RED = (255, 0, 0)

class Target:
    def __init__(self):
        self.x = random.randint(200, WIDTH - 100)
        self.y = random.randint(HEIGHT - 800, HEIGHT - 400)
        self.vx = random.choice([-1, 1]) * random.uniform(1, 2)

    def update(self):
        self.x += self.vx
        if self.x <= 0 or self.x >= WIDTH:
            self.vx *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (int(self.x), int(self.y)), 8)