import pygame
from random import uniform, choice, randint

class Particle():
    def __init__(self, game, x, y, width, height, color):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.xvel = 0
        self.yvel = 0
    
    def move(self):
        self.x += self.xvel
        self.y += self.yvel

    def draw(self):
        pygame.draw.rect(self.game.window, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.move()
        self.draw()

class Burst():
    def __init__(self, game, x, y, amount):
        self.game = game
        self.x = x
        self.y = y
        self.amount = amount
        self.particles = []
        self.add_particles()
        self.emmit()

    def remove_particles(self):
        for p in self.particles:
            if (p.x < -20) or (p.x > self.game.width) or (p.y > self.game.height) or (p.y < -20):
                self.particles.remove(p)

    def add_particles(self):
        for _ in range(self.amount):
            color = (randint(0,255), randint(0,255), randint(0,255))
            self.particles.append(Particle(self.game, randint(0,self.game.width-20), randint(0,self.game.height-20), 5, 5, color))

    def emmit(self):
        for p in self.particles:
            p.xvel = uniform(0.5, 3.0) * choice([-1, 1])
            p.yvel = uniform(0.5, 3.0) * choice([-1, 1])

    def update(self):
        self.remove_particles()
        for p in self.particles:
            p.update()