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


def get_apple_location(top_left, field_size, step_size):
    max_felder_x = (field_size[0]/step_size) - 1
    max_felder_y = (field_size[1]/step_size) - 1
    random_field_x = randint(0, max_felder_x)
    random_field_y = randint(0, max_felder_y)
    x_coord = random_field_x * step_size + top_left[0]
    y_coord = random_field_y * step_size + top_left[1]
    location = (x_coord, y_coord)
    return location


if __name__ == "__main__":
    print(get_apple_location((100, 100), (800, 600), 20))