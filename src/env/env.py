import pygame
import random
import math
import numpy as np

from env.configloader import ConfigLoader
from env.turret import Turret
from env.target import Target

cfg = ConfigLoader()
WIDTH = cfg.config['width']
HEIGHT = cfg.config['height']
NUM_TARGETS = cfg.config['num_targets']

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
GRAY = (180, 180, 180)

class Environment():
    def __init__(self):
        self.turret = Turret(0, 0)
        self.targets = []
        self.step_count = 0
        self.max_steps = 500
        self.reset()

    def reset(self):
        self.turret = Turret(0, 0)
        self.targets = [Target() for _ in range(NUM_TARGETS)]
        self.step_count = 0
        return self.get_state()

    def step(self, action):
        # Aktion ausführen: 0 = links, 1 = nichts, 2 = rechts
        if action == 0:
            self.turret.rotate(-1)
        elif action == 2:
            self.turret.rotate(1)

        # Targets updaten
        for t in self.targets:
            t.update()

        # Belohnung & Termination
        reward = 0
        done = False
        self.step_count += 1

        # (Noch keine Trefferprüfung – später bei Schüssen)
        if self.step_count >= self.max_steps:
            done = True

        return self.get_state(), reward, done

    def get_state(self):
        # Zustand: Turret-Winkel + Target-Positionen & Geschwindigkeiten
        state = [self.turret.angle / 90.0]  # normiert
        for t in self.targets:
            state.extend([
                t.x / WIDTH,
                t.y / HEIGHT,
                (t.vx + 2) / 4  # normiert von [-2, 2]
            ])
        # Padding falls weniger als NUM_TARGETS
        while len(state) < 1 + NUM_TARGETS * 3:
            state.extend([0, 0, 0])
        return np.array(state, dtype=np.float32)

    def render(self, render_screen):
        render_screen.fill(WHITE)
        self.turret.draw(render_screen)
        for t in self.targets:
            t.draw(render_screen)
        pygame.display.flip()