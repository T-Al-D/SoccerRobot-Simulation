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
        self.id: int = id
        self.team: int = team
        self.positionX: int = positionX
        self.positionY: int = positionY
        self.size: int = size
        self.step: float = step
        self.status: int = 0
        self.currentDirection: int = None
        self.speed: float = 0
        self.errorNotification: int = 0
        self.message: str = None
        self.collision: bool = False
        self.field: SoccerField = field

        # create the rectangle object
        self.rectangle = pygame.Rect(self.positionX, self.positionY, size, size)
        # load image for rectangle
        self.image = loadAndScaleImage(imagePath, self.size, self.size)

    def move(self, direction: int, extraSteps: float = 1.0):
        """!
        @brief moves the x or y position of the robot on the field
        after that it sets the internal rectangle

        @param direction the direction in which the robot should be moved

        @return void This function does not return a value.
        """
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
