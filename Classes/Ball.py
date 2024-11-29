# from Classes.SoccerField import SoccerField


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
        self.size: int = size
        self.step: int = step
        self.field: SoccerField = field
        self.positionX: int = int(field.width / 2.07)
        self.positionY: int = int(field.width / 2.07)
        self.ballStatus: int = 0
        self.field.ball = self

        # create the rectangle object
        self.rectangle = pygame.Rect(self.positionX, self.positionY, size, size)
        # load image for rectangle
        self.image = loadAndScaleImage(imagePath, self.size, self.size)

    def move(self, direction: int):
        """!
        @brief moves the x or y position of the ball on the field

        @param direction the direction in which the ball should be moved
        @param step in what steps should the ball be moved

        @return void This function does not return a value.
        """
        match direction:
            case Const.NORTH_DIRECTION:
                if self.positionY > Const.OUTER_MARGIN:
                    self.positionY -= self.step
            case Const.EAST_DIRECTION:
                if self.positionX < (self.field.width - self.size - Const.OUTER_MARGIN):
                    self.positionX += self.step
            case Const.SOUTH_DIRECTION:
                if self.positionY < (self.field.width - self.size - Const.OUTER_MARGIN):
                    self.positionY += self.step
            case Const.WEST_DIRECTION:
                if self.positionX > Const.OUTER_MARGIN:
                    self.positionX -= self.step
            case _:
                pass
