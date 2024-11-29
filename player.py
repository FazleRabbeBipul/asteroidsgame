import pygame
from constants import *

class CircleShape:
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Call parent class constructor
        self.rotation = 0  # Initialize rotation to 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, direction, dt):
        # Calculate the forward vector based on the current rotation
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        # Update the player's position
        self.position += forward * direction * PLAYER_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Rotate right
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Rotate up
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Move forward
            self.move(1, dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Move backward
            self.move(-1, dt)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  # Draw triangle with white color and width 2
