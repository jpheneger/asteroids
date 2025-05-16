import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(MIN_DEGREES, MAX_DEGREES)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        
        self.radius = self.radius - ASTEROID_MIN_RADIUS
        
        a1 = Asteroid(self.position.x, self.position.y, self.radius)
        a2 = Asteroid(self.position.x, self.position.y, self.radius)
        
        a1.velocity = vector1 * 1.2
        a2.velocity = vector2 * 1.2