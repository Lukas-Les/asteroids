import pygame

from circleshape import CircleShape

class Shot(CircleShape):
    containers: tuple

    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt: int):
        self.position += self.velocity * dt
