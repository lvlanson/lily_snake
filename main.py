# Simple pygame program

# Import and initialize the pygame library
import pygame
import colors
from helpers import draw_grid, check_boundaries

pygame.init()

# Set up the drawing window
WIDTH  = 1000
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Spielfeld
#                   x ,  y
TOP_LEFT        = (100, 100)
FIELD_SIZE      = (800, 600)
STEP_SIZE       = 20
game_field      = pygame.Rect(TOP_LEFT, FIELD_SIZE)

# Schlange
snake_pos       = (TOP_LEFT[0] + FIELD_SIZE[0] / 2, TOP_LEFT[1] + FIELD_SIZE[1] / 2)
snake_head      = pygame.Rect(snake_pos, (STEP_SIZE, STEP_SIZE))

# Apfel
apple_pos       = (TOP_LEFT[0] + FIELD_SIZE[0] / 4, TOP_LEFT[1] + FIELD_SIZE[1] / 4)
apple           = pygame.Rect(apple_pos, (STEP_SIZE, STEP_SIZE))

# Timer
clock = pygame.time.Clock()

# Richtung
GO_UP      = False
GO_DOWN    = False
GO_LEFT    = False
GO_RIGHT   = True

# Run until the user asks to quit
running = True

# Schlange ist noch aktiv
snake_active = True
while running:

    ### VORBEREITUNG SPIELFELD ###
    # Fill the background with white
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0, 0), game_field, 5, border_radius=10)
    #draw_grid(screen, TOP_LEFT, FIELD_SIZE, STEP_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not GO_DOWN:
                    GO_UP = True
                    GO_DOWN = False
                    GO_LEFT = False
                    GO_RIGHT = False
            elif event.key == pygame.K_DOWN:
                if not GO_UP:
                    GO_UP = False
                    GO_DOWN = True
                    GO_LEFT = False
                    GO_RIGHT = False
            elif event.key == pygame.K_LEFT:
                if not GO_RIGHT:
                    GO_UP = False
                    GO_DOWN = False
                    GO_LEFT = True
                    GO_RIGHT = False
            elif event.key == pygame.K_RIGHT:
                if not GO_LEFT:
                    GO_UP = False
                    GO_DOWN = False
                    GO_LEFT = False
                    GO_RIGHT = True

    if snake_active:
        # Did the user click the window close button?

        # Position der Schlange berechnen
        if check_boundaries(TOP_LEFT, FIELD_SIZE, snake_head, STEP_SIZE):
            if GO_UP:
                snake_pos = (snake_pos[0], snake_pos[1] - STEP_SIZE)
            elif GO_DOWN:
                snake_pos = (snake_pos[0], snake_pos[1] + STEP_SIZE)
            elif GO_LEFT:
                snake_pos = (snake_pos[0] - STEP_SIZE, snake_pos[1])
            elif GO_RIGHT:
                snake_pos = (snake_pos[0] + STEP_SIZE, snake_pos[1])
        else:
            print("ENDE")
            snake_active = False
        snake_head = pygame.Rect(snake_pos, (STEP_SIZE, STEP_SIZE))
    pygame.draw.rect(screen, colors.SNAKE_GREEN, snake_head)
    pygame.draw.rect(screen, colors.RED, apple)
    # Flip the display
    pygame.display.flip()
    clock.tick(10)
# Done! Time to quit.
pygame.quit()
