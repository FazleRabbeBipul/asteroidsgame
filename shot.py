import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.topleft = self.position - pygame.Vector2(self.radius, self.radius)  # Update rect position
