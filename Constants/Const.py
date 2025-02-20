"""!
@file
@brief contants for the project
variables that only need to be declared once
"""

from typing import Final

import pygame

# basic directions
STANDING_STILL: Final[int] = 0
NORTH_DIRECTION: Final[int] = 1
EAST_DIRECTION: Final[int] = 3
SOUTH_DIRECTION: Final[int] = 5
WEST_DIRECTION: Final[int] = 7
ALL_BASIC_DIRECTIONS = [
    NORTH_DIRECTION,
    EAST_DIRECTION,
    SOUTH_DIRECTION,
    WEST_DIRECTION,
]

# horizontal / vertical
HORIZONTAL_MOVEMENT = [WEST_DIRECTION, EAST_DIRECTION]
VERTICAL_MOVEMENT = [NORTH_DIRECTION, SOUTH_DIRECTION]

# inbetween directions
NORTH_EAST_DIRECTION: Final[int] = 2
SOUTH_EAST_DIRECTION: Final[int] = 4
SOUTH_WEST_DIRECTION: Final[int] = 6
NORTH_WEST_DIRECTION: Final[int] = 8

# basic arrow keys for direction
ALL_BASIC_ARROWKEYS = [pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT]

# Margin for the "outside" of the field
OUTER_PADDING: Final[int] = 20

# Top-Margin for label
TOP_MARGIN: Final[int] = 45

# divisor, to make sure the players and ball are in the middle of the y axis
Y_DIVISOR: Final[float] = 2.25
