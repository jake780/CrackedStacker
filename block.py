import random
import pygame
from random import randint, choice

class Block():
    def __init__(self, game, level):
        self.game = game
        self.width = 50
        self.height = 20
        self.x = choice([0, (self.game.width - self.width)])
        self.y = (self.game.height-self.height) - (level * self.height)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.velocity = 1

        self.level = level
        self.frozen = False

    def draw(self):
        pygame.draw.rect(self.game.window, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        if not self.frozen:
            self.x += self.velocity
            if ((self.x + self.width) > self.game.width) or (self.x < 0):
                self.velocity *= -1

