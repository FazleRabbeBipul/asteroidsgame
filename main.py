import pygame
from constants import *  

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Initialize clock and dt
    clock = pygame.time.Clock()
    dt = 0  # Delta time variable to track time between frames
    
    running = True
    while running:
        # Fill the screen with black color
        screen.fill((0, 0, 0))
        
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # End the game loop
        
        # Refresh the screen
        pygame.display.flip()
        
        # Limit to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
    
    pygame.quit()  # Clean up and close the pygame window

if __name__ == "__main__":
    main()
