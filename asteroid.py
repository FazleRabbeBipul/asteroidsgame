import pygame
from player import CircleShape  # Import CircleShape from player.py

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity as a vector

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line
        self.position += self.velocity * dt
