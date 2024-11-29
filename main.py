import pygame
from constants import *  # Import constants
from player import Player  # Import Player class

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Initialize clock and dt
    clock = pygame.time.Clock()
    dt = 0
    
    # Create player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    running = True
    while running:
        # Fill the screen with black color
        screen.fill((0, 0, 0))
        
        # Call the player's update method
        dt = clock.tick(60) / 1000  # Delta time in seconds
        player.update(dt)

        # Draw player on screen
        player.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()  # Clean up and close the pygame window

if __name__ == "__main__":
    main()
