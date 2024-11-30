import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Create two groups
    updatable = pygame.sprite.Group()  # Objects that need to be updated
    drawable = pygame.sprite.Group()   # Objects that need to be drawn
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Add Player class to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()  # Create asteroid field (if applicable)

    running = True
    dt = 0
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                return
            
        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.rect.colliderect(shot.rect):  # Collision check
                    asteroid.split()  # Remove the asteroid
                    shot.kill()      # Remove the bullet

        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)

        # Refresh the screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    #pygame.quit()  # Clean up and close the pygame window

if __name__ == "__main__":
    main()
