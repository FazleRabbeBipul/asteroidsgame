import pygame
from constants import *
from shot import Shot
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Call parent class constructor
        self.rotation = 0  # Initialize rotation to 0
        self.shot_timer = 0  # Timer for controlling shot cooldown

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

    def shoot(self):
        # Prevent shooting if the shot_timer is greater than 0 (cooldown in effect)
        if self.shot_timer > 0:
            return
        
        # Create a new shot at the player's position
        shot = Shot(self.position.x, self.position.y)
        # Set the shot's velocity based on the player's rotation
        shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation + 180) * PLAYER_SHOOT_SPEED
        
        # Reset shot_timer after shooting
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Rotate right
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Move forward
            self.move(-1, dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Move backward
            self.move(1, dt)

        
        # Wrap around the screen
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        
        # Handle shooting
        self.shot_timer -= dt
        if keys[pygame.K_SPACE] and self.shot_timer <= 0:
            self.shoot()
            self.shot_timer = PLAYER_SHOOT_COOLDOWN  # Reset the shooting timer

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  # Draw triangle with white color and width 2
