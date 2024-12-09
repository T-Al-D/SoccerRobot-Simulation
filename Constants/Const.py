"""!
@file
@brief contants for the project
variables that only need to be declared once
"""

from typing import Final

# CONSTANTS
NORTH_DIRECTION: Final[int] = 1
NORTH_EAST_DIRECTION: Final[int] = 2
EAST_DIRECTION: Final[int] = 3
SOUTH_EAST_DIRECTION: Final[int] = 4
SOUTH_DIRECTION: Final[int] = 5
SOUTH_WEST_DIRECTION: Final[int] = 6
WEST_DIRECTION: Final[int] = 7
NORTH_WEST_DIRECTION: Final[int] = 8

allBasicDirections = [NORTH_DIRECTION, EAST_DIRECTION, SOUTH_DIRECTION, WEST_DIRECTION]

# Margin for the "outside" of the field
OUTER_PADDING: Final[int] = 20

# Top-Margin for label
TOP_MARGIN: Final[int] = 45

# divisor, to make sure the players and ball are in the middle of the y axis
Y_DIVISOR: Final[float] = 2.0
