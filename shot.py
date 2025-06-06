from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius)
