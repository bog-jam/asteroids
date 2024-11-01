# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import Player
from constants import *
from asteroidfield import *
from asteroid import *
from shots import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        # iterate through the updateable group and update each object
        for each in updatable:
            each.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    new_roids = asteroid.split()
                    if new_roids:
                        asteroids.add(new_roids[0])
                        asteroids.add(new_roids[1])


        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit() 
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        # call tick and calculate dt
        dt = clock.tick(60) / 1000.0
    


if __name__ == "__main__":
    main()