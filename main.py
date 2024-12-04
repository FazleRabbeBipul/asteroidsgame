import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from gamerender import *
from gameutils import load_highest_score, save_highest_score  


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create two groups
    updatable = pygame.sprite.Group()  # Objects that need to be updated
    drawable = pygame.sprite.Group()   # Objects that need to be drawn
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers for game objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Add Player class to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()  # Create asteroid field (if applicable)

    # Game state variables
    game_state = "START"  # Game states: START, PLAY, PAUSE, GAME_OVER
    score = 0  # Player's score
    player_name = ""  # Player's name
    dt = 0  # Delta time for frame updates
    running = True

    # Load the highest score and scorer name
    highest_score, highest_scorer = load_highest_score()

    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # Start screen input handling
            if game_state == "START" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_name:  # Start the game if name is entered
                    game_state = "PLAY"
                elif event.key == pygame.K_BACKSPACE:  # Remove last character from name
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode  # Append entered character to name

            # Pause/Resume the game
            if game_state == "PLAY" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_state = "PAUSE"
            elif game_state == "PAUSE" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_state = "PLAY"
 
            # Restart game from GAME_OVER state
            if game_state == "GAME_OVER" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Update the highest score if the current score is higher
                    if score > highest_score:
                        highest_score = score
                        highest_scorer = player_name  # Update the highest scorer
                        # Save the highest score and player name
                        save_highest_score(highest_score, highest_scorer)
                    return main()

        # Update and render based on game state
        if game_state == "START":
            highest_score, highest_scorer = load_highest_score()
            render_start_screen(screen, draw_text, player_name, highest_score, highest_scorer)
           

        elif game_state == "PLAY":
            game_state, score = render_play_screen(
                screen, draw_text, updatable, drawable, player, asteroids, shots, dt, score, player_name, highest_score, highest_scorer
            )
            #screen.fill((0, 0, 0))
        elif game_state == "PAUSE":
            render_pause_screen(screen, draw_text)

        elif game_state == "GAME_OVER":
            highest_score, highest_scorer = render_game_over_screen(screen, draw_text, score, player_name, highest_score, highest_scorer)

        # Refresh the screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Limit the frame rate and calculate delta time

pygame.quit()  # Clean up and close the pygame window


if __name__ == "__main__":
    main()
