# gameutils.py
import pygame

def load_highest_score(filename="highscore.txt"):
    """
    Load the highest score and player name from a file.
    Returns a tuple: (highest_score, player_name).
    """
    try:
        with open(filename, "r") as file:
            data = file.readline().strip()
            if data:
                score, name = data.split(",")
                return int(score), name
    except FileNotFoundError:
        pass
    return 0, "Anonymous"  # Default score and name if the file doesn't exist


def save_highest_score(score, name, filename="highscore.txt"):
    """
    Save the highest score and player name to a file.
    """
    with open(filename, "w") as file:
        file.write(f"{score},{name}")
