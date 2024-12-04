import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from gameutils import *


def draw_text(screen, text, size, color, x, y):
    """Utility function to draw text on the screen."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def render_start_screen(screen, draw_text, player_name, highest_score, highest_scorer):
    """Render the start screen."""
    screen.fill((0, 0, 0))  # Fill the screen with black
    draw_text(screen, "ASTEROID GAME", 80, "white", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    draw_text(screen, f"Enter your name: {player_name}", 40, "white", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    draw_text(screen, "Press ENTER to start", 30, "white", SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.75)
    draw_text(screen, f"Highest Score: {highest_score} by {highest_scorer}", 30, "yellow", SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.85)

# Inside render_play_screen function
def render_play_screen(screen, draw_text, updatable, drawable, player, asteroids, shots, dt, score, player_name, highest_score, highest_scorer):
    """Render the play screen."""
    # Update all objects in the updatable group
    for obj in updatable:
        obj.update(dt)

    # Check for collisions between player and asteroids
    for asteroid in asteroids:
        if player.check_collision(asteroid):
            return "GAME_OVER", score

    # Check for collisions between bullets and asteroids
    for asteroid in asteroids:
        for shot in shots:
            if asteroid.rect.colliderect(shot.rect):  # Collision check
                asteroid.split()  # Handle asteroid split
                shot.kill()       # Remove the bullet
                print(f"Before shoot: {score}")
                score += 10       # Increment the score
                print(f"After shoot: {score}")

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Draw all objects in the drawable group
    for obj in drawable:
        obj.draw(screen)

    # Display score, player name, and highest score
    draw_text(screen, f"Score: {score}", 30, "white", 100, 30)
    draw_text(screen, f"Player: {player_name}", 30, "white", SCREEN_WIDTH - 150, 30)
    draw_text(screen, f"High Score: {highest_score} by {highest_scorer}", 30, "white", SCREEN_WIDTH / 2, 30)

    return "PLAY", score




def render_pause_screen(screen, draw_text):
    """Render the pause screen."""
    screen.fill((0, 0, 0))  # Fill the screen with black
    draw_text(screen, "GAME PAUSED", 50, "white", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    draw_text(screen, "Press 'P' to Resume", 30, "white", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)

def render_game_over_screen(screen, draw_text, score, player_name, highest_score, highest_scorer):
    """Render the game over screen with the high score and player name."""
    # Update the highest score if necessary
    if score > highest_score:
        highest_score = score
        highest_scorer = player_name
        save_highest_score(highest_score, highest_scorer)

    screen.fill((0, 0, 0))  # Fill the screen with black
    draw_text(screen, "GAME OVER", 50, "red", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50)
    draw_text(screen, f"Final Score: {score}", 40, "white", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    draw_text(screen, f"High Score: {highest_score} by {highest_scorer}", 40, "white", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)
    draw_text(screen, "Press 'R' to Restart", 30, "white", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100)

    return highest_score, highest_scorer
