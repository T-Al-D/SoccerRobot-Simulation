"""!
@file
@brief class for Goal
"""

import pygame


class Goal:
    """!
    @brief A class that activates if a goal is scored
    """

    def __init__(
        self,
        positionX: int,
        positionY: int,
        width: int,
        height: int,
    ):
        """!
        @brief Constructor for Goal class.
        Initializes the most necessary data
        """
        self._positionX: int = positionX
        self._positionY: int = positionY
        self._width: int = width
        self._height: int = height
        self._status: int = 0
        self._score: int = 0

        self._rectangle = pygame.Rect(positionX, positionY, width, height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    @property
    def positionX(self):
        return self._positionX

    @positionX.setter
    def positionX(self, value: int):
        self._positionX = value

    @property
    def positionY(self):
        return self._positionY

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: int):
        self._status = value

    @property
    def rectangle(self):
        return self._rectangle

    @status.setter
    def rectangle(self, value: int):
        self._rectangle = value
