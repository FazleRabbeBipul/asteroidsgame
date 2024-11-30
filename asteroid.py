import pygame
import random
from player import CircleShape  # Import CircleShape from player.py
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * 100  # Set random initial velocity
        self.rect = pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.topleft = self.position - pygame.Vector2(self.radius, self.radius)  # Update rect position

    def split(self):
        # If the asteroid is too small to split, just kill it
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        # Kill the current asteroid (it will be destroyed)
        self.kill()

        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Generate random angles for the split
        random_angle = random.uniform(20, 50)

        # Calculate new velocities (rotate by random_angle and -random_angle)
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Scale velocity up for the new asteroid
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Create two new asteroids with the new radius and velocities
        Asteroid(self.rect.centerx, self.rect.centery, new_radius).velocity = velocity1
        Asteroid(self.rect.centerx, self.rect.centery, new_radius).velocity = velocity2
