import pygame
import random
from env.env import Environment
from env.configloader import ConfigLoader

class Simulation:
    def __init__(self):
        self.cfg = ConfigLoader()
        self.width = self.cfg.config['width']
        self.height = self.cfg.config['height']
        self.fps = self.cfg.config.get('fps', 60)

        # Farben
        self.colors = {
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'blue': (0, 100, 255),
            'green': (0, 255, 0),
            'gray': (180, 180, 180),
        }

        # Pygame initialisieren
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Air Defense RL Simulation")
        self.clock = pygame.time.Clock()

        # Environment laden
        self.env = Environment()
        self.state = self.env.reset()
        self.done = False

    def step(self, action):
        self.state, self.reward, self.done = self.env.step(action)
        self.env.render(self.screen)
        return self.state, self.reward, self.done

    def reset(self):
        self.state = self.env.reset()
        self.done = False
        return self.state

    def render(self):
        self.env.render(self.screen)

    def get_state(self):
        return self.state

    def run_loop(self):
        running = True
        while running:
            self.clock.tick(self.fps)

            # Dummy: zufällige Aktion (später RL-Agent)
            action = random.randint(0, 2)
            self.step(action)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.done:
                self.reset()

        pygame.quit()
