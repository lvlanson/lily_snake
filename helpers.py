import colors
import pygame
from random import randint


# Zeichnet ein Gittermuster im Spielfeld. Das Fenster ist die Variable screen. Das Spielfeld wird durch top_left
# field_size beschrieben. Die Schrittweite für das Gitter ist die Variable step.
def draw_grid(screen, top_left: tuple, field_size: tuple, step: int):
    for y in range(top_left[1] + step, top_left[1] + field_size[1], step):
        pygame.draw.line(screen, colors.BLACK, (top_left[0], y), (top_left[0] + field_size[0], y))

    for x in range(top_left[0] + step, top_left[0] + field_size[0], step):
        pygame.draw.line(screen, colors.BLACK, (x, top_left[1]), (x, top_left[1] + field_size[1]))


def check_boundaries(top_left, field_size, snake_head, step_size):

    print(snake_head)
    #wenn schlange links drüber ist
    if snake_head[0] <= top_left[0]:
        return False
    #wenn schlange rechts drüber ist
    elif snake_head[0] >= top_left[0] + field_size[0] - step_size:
        return False
    #wenn schlange oben drüber ist
    elif snake_head[1] <= top_left[1]:
        return False
    #wenn schlange untern drüber ist
    elif snake_head[1] >= top_left[1] + field_size[1] - step_size:
        return False
    return True


def get_apple_location(tep_left, field_size, step_size):
    location = (0, 0)

    return location


if __name__ == "__main__":
    print(get_apple_location((100, 100), (800, 600), 20))