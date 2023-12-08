import pygame
import time
import random
from pathlib import Path

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship")

this_file = Path(__file__).resolve()
bg_path = this_file.parent / "images/background3.jpg"
BG = pygame.transform.scale(pygame.image.load(bg_path), (WIDTH, HEIGHT))


def draw():
    """
    Draws the game screen where the game board is.
    :return: N/A
    """
    WIN.blit(BG, (0, 0))
    pygame.display.update()


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()

    pygame.quit()


if __name__ == "__main__":
    main()
