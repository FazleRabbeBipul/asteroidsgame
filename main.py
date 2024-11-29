
import pygame
from constants import *  # Import all constants from constants.py

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    running = True
    while running:
        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Refresh the screen
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
      

   

if __name__ == "__main__":
    main()
