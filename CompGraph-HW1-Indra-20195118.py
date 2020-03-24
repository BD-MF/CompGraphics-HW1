import pygame
from sys import exit
import numpy as np
import math

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in np.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in np.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("CompGraphics-HW1-Indra-20195118")

# Define the colors we will use in RGB format
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

old_pt = np.array([0, 0])
cur_pt = np.array([0, 0])
old_rect_pt = np.array([0, 0])
cur_rect_pt = np.array([0, 0])

screen.fill(WHITE)

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False
pressed = -1
margin = 6
while not done:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = 1
        elif event.type == pygame.MOUSEMOTION:
            pressed = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 2
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = -1

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    cur_pt = np.array([x, y])
    if old_pt[0] != 0 and old_pt[1] != 0:
        draw_dashed_line(screen, RED, old_pt, cur_pt, 1)

    if pressed == 1:
        if button1 == 1:
            pygame.draw.rect(screen, BLUE, (cur_pt[0] - margin, cur_pt[1] - margin, 2 * margin, 2 * margin), 5)
            cur_rect_pt = np.array([x,y])

            if old_rect_pt[0] == 0 and old_rect_pt[1] == 0:
                old_rect_pt = cur_rect_pt

            pygame.draw.line(screen, GREEN, (old_rect_pt[0], old_rect_pt[1]),
                             (cur_rect_pt[0], cur_rect_pt[1]),5)

            old_rect_pt = cur_rect_pt

    print("mouse x:" + repr(x) + " y:" + repr(y) + " button:" + repr(button1) + " " + repr(button2) + " " + repr(
        button3) + " pressed:" + repr(pressed))
    old_pt = cur_pt

    pygame.display.update()

pygame.quit()