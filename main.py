import pygame

from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from player import Player
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    font = pygame.font.Font(size=38)
    text_surface = font.render("score: ", False, "white")
    text_rect = text_surface.get_rect()
    text_rect.topleft = (0, 0)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    asteroidfield = AsteroidField()
    player = Player(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2)
    clock = pygame.time.Clock()

    dt = 0
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        text_surface = font.render(f"score: {score}", False, "white")
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    if points := asteroid.split():
                        score += points
                    shot.kill()
            if asteroid.collides_with(player):
                print("Game Over!")
                print(f"Final Score: {score}")
                return
        for d in drawable:
            d.draw(screen)
        screen.blit(source=text_surface, dest=text_rect)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
