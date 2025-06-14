import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    containers: tuple

    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt: int):
        self.position += self.velocity * dt

    def split(self) -> int | None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 1
        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity =  vec1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vec2 * 1.2
