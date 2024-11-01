import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        
    def draw(self, surface):
        position = self.position
        radius = self.radius
        pygame.draw.circle(surface, "white", position, radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vector1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            new_vector2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            self.kill()
            new_asteroid1 = Asteroid(self.position.x, self.position.y, (old_radius - ASTEROID_MIN_RADIUS))
            new_asteroid2 = Asteroid(self.position.x, self.position.y, (old_radius - ASTEROID_MIN_RADIUS))
            new_asteroid1.velocity = new_vector1 * 1.2
            new_asteroid2.velocity = new_vector2 * 1.2
            return new_asteroid1, new_asteroid2