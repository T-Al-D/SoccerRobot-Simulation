"""!
@file
@brief class for SoccerRobot (main-actor on Soccerfield)
"""

import pygame
from Actions.Images import loadAndScaleImage
from Classes.SoccerField import SoccerField
from Constants import Const


class SoccerRobot:
    """!
    @brief SoccerRobots kick the ball on the field (main-actors on the field)
    """

    def __init__(
        self,
        id: int,
        team: int,
        size: int,
        step: float,
        positionX: int,
        positionY: int,
        imagePath: str,
        field: SoccerField,
    ):
        """!
        @brief Constructor for SoccerRobot class.
        Initializes the most necessary data
        """
        self._id: int = id
        self._team: int = team
        self._positionX: int = positionX
        self._positionY: int = positionY
        self._size: int = size
        self._step: float = step
        self._status: int = 0
        self._currentDirection: int = Const.STANDING_STILL
        self._speed: float = 0
        self._errorNotification: int = 0
        self._message: str = None
        self._collision: bool = False
        self._field: SoccerField = field

        # create the rectangle object
        self._rectangle = pygame.Rect(self._positionX, self._positionY, size, size)
        # load image for rectangle
        self._image = loadAndScaleImage(imagePath, self.size, self.size)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

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
    def size(self):
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value: float):
        self._step = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: int):
        self._status = value

    @property
    def currentDirection(self):
        return self._currentDirection

    @currentDirection.setter
    def currentDirection(self, value: int):
        self._currentDirection = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value: float):
        self._speed = value

    @property
    def errorNotification(self):
        return self._errorNotification

    @errorNotification.setter
    def errorNotification(self, value: int):
        self._errorNotification = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

    @property
    def collision(self):
        return self._collision

    @collision.setter
    def collision(self, value: bool):
        self._collision = value

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, value):
        self._field: SoccerField = value

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

    def move(self, direction: int, extraSteps: float = 1.0):
        """!
        @brief moves the x or y position of the robot on the field
        after that it sets the internal rectangle

        @param direction the direction in which the robot should be moved

        @return void This function does not return a value.
        """
        self.currentDirection = direction
        match direction:
            case Const.NORTH_DIRECTION:
                if self.positionY > (Const.OUTER_PADDING + Const.TOP_MARGIN):
                    self.positionY -= int(self.step * extraSteps)
            case Const.EAST_DIRECTION:
                if self.positionX < (
                    self.field.width - self.size - Const.OUTER_PADDING
                ):
                    self.positionX += self.step * extraSteps
            case Const.SOUTH_DIRECTION:
                if self.positionY < (self.field.height - Const.OUTER_PADDING - 5):
                    self.positionY += int(self.step * extraSteps)
            case Const.WEST_DIRECTION:
                if self.positionX > Const.OUTER_PADDING:
                    self.positionX -= int(self.step * extraSteps)
            case _:
                pass

        # after each change of x or y, set the internal rectangle
        self.rectangle.x = self.positionX
        self.rectangle.y = self.positionY

    def resetDirection(self):
        self.currentDirection = Const.STANDING_STILL
