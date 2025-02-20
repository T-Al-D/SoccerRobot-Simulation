"""!
@file
@brief class for the Ball
"""

import pygame
from Actions.Images import loadAndScaleImage
from Classes.SoccerField import SoccerField
from Constants import Const


class Ball:
    """!
    @brief Constructor for Ball class.
    Initializes the most necessary data
    """

    def __init__(self, size: int, step: int, imagePath: str, field: SoccerField):
        self._size: int = size
        self._step: int = step
        self._field: SoccerField = field
        self._currentDirection: int = Const.STANDING_STILL
        self._positionX: int = int(field.width / 2.07)
        self._positionY: int = int(field.height / (Const.Y_DIVISOR - 0.1))
        self._ballStatus: int = 0
        self._field.ball = self

        # create the rectangle object
        self._rectangle = pygame.Rect(self._positionX, self._positionY, size, size)
        # load image for rectangle
        self._image: pygame.image = loadAndScaleImage(imagePath, self._size, self._size)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value: int):
        self._step = value

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, value):
        self._field: SoccerField = value

    @property
    def currentDirection(self):
        return self._currentDirection

    @currentDirection.setter
    def currentDirection(self, value: int):
        self._currentDirection = value

    @property
    def positionX(self):
        return self._positionX

    @positionX.setter
    def positionX(self, value: int):
        self._positionX = value

    @property
    def positionY(self):
        return self._positionY

    @positionY.setter
    def positionY(self, value: int):
        self._positionY = value

    @property
    def ballStatus(self):
        return self._ballStatus

    @ballStatus.setter
    def ballStatus(self, value: int):
        self._ballStatus = value

    @property
    def rectangle(self):
        return self._rectangle

    @rectangle.setter
    def rectangle(self, value):
        self._rectangle: pygame.Rect = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image: pygame.image = value

    def move(self):
        """!
        @brief moves the x or y position of the ball on the field
        after that it sets the internal rectangle

        @param direction the direction in which the ball should be moved

        @return void This function does not return a value.
        """
        match self.currentDirection:
            case Const.NORTH_DIRECTION:
                if self.positionY > (Const.OUTER_PADDING):
                    self.positionY -= self.step
                else:
                    self.positionY += self.size
            case Const.EAST_DIRECTION:
                if self.positionX < (
                    self.field.width - self.size - Const.OUTER_PADDING
                ):
                    self.positionX += self.step
                else:
                    self.positionX -= self.size
            case Const.SOUTH_DIRECTION:
                if self.positionY < (
                    self.field.height - Const.OUTER_PADDING - self.size
                ):
                    self.positionY += self.step
                else:
                    self.positionY -= self.size
            case Const.WEST_DIRECTION:
                if self.positionX > Const.OUTER_PADDING:
                    self.positionX -= self.step
                else:
                    self.positionX += self.size
            case _:
                pass

        # after each change of x or y, set the internal rectangle
        self.rectangle.x = self.positionX
        self.rectangle.y = self.positionY

    def resetBallToMiddle(self):
        self.positionX = int(self.field.width / 2.07)
        self.positionY = int(self.field.height / (Const.Y_DIVISOR - 0.1))
        
        # after each change of x or y, set the internal rectangle
        self.rectangle.x = self.positionX
        self.rectangle.y = self.positionY

    def standingStill(self):
        self.currentDirection = Const.STANDING_STILL
