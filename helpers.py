import colors
import pygame


# Zeichnet ein Gittermuster im Spielfeld. Das Fenster ist die Variable screen. Das Spielfeld wird durch top_left
# field_size beschrieben. Die Schrittweite für das Gitter ist die Variable step.
def draw_grid(screen, top_left: tuple, field_size: tuple, step: int):
    for y in range(top_left[1] + step, top_left[1] + field_size[1], step):
        pygame.draw.line(screen, colors.BLACK, (top_left[0], y), (top_left[0] + field_size[0], y))

    for x in range(top_left[0] + step, top_left[0] + field_size[0], step):
        pygame.draw.line(screen, colors.BLACK, (x, top_left[1]), (x, top_left[1] + field_size[1]))