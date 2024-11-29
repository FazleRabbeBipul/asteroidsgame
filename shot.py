import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        # Initialize the CircleShape with a small radius for the shot
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Draw the shot as a filled circle
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        # Update the position of the shot based on its velocity
        self.position += self.velocity * dt
