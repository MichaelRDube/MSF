#put program entry stuff here
from monsters.goblin import Goblin
from game import Game
import time
import sys
import pygame


# Initialize Pygame
pygame.init()


# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Create a resizable display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# Set the window title
pygame.display.set_caption("Monster Slap Fight")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Clock to control the frame rate
clock = pygame.time.Clock()
last_update = pygame.time.get_ticks()

game = Game(screen, clock)
game.run_game()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check for quit event
            running = False
        elif event.type == pygame.VIDEORESIZE:  # Handle window resizing
            continue
        elif event.type == pygame.KEYDOWN:
            continue
            """
            if event.key == pygame.K_LSHIFT:
                field1._text_align = "left"
            elif event.key == pygame.K_RSHIFT:
                field1._text_align = "right"
            elif event.key == pygame.K_SPACE:
                field1._text_align = "center"
            else:
                field1.add_letter(event.unicode)
            """
        elif event.type == pygame.MOUSEBUTTONDOWN:
            continue

    # Game logic (e.g., updating positions) goes here

    # Drawing code
    screen.fill(WHITE)  # Clear the screen with a white background
    game.render()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()