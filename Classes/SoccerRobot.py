"""!
@file
@brief class for SoccerRobot (main-actor on Soccerfield)
"""

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
        playerSize: int,
        playerSteps: float,
        positionX: int,
        positionY: int,
        field: SoccerField,
    ):
        """!
        @brief Constructor for SoccerRobot class.
        Initializes the most necessary data
        """
        from Classes.SoccerField import SoccerField  # prevention of circular imports

        self.id: int = id
        self.team: int = team
        self.positionX: int = positionX
        self.positionY: int = positionY
        self.playerSize: int = playerSize
        self.playerSteps: float = playerSteps
        self.status: int = 0
        self.currentDirection: int = None
        self.speed: float = 0
        self.errorNotification: int = 0
        self.message: str = None
        self.collision: bool = False
        self.field: SoccerField = field

    def move(self, direction: int, step: float):
        """!
        @brief moves the x or y position of the robot on the field

        @param direction the direction in which the robot should be moved
        @param step in what steps should the robot be moved

        @return void This function does not return a value.
        """
        margin = 20
        match direction:
            case Const.NORTH_DIRECTION:
                if self.positionY > margin:
                    self.positionY -= step
            case Const.EAST_DIRECTION:
                if self.positionX < (self.field.width - self.playerSize - margin):
                    self.positionX += step
            case Const.SOUTH_DIRECTION:
                if self.positionY < (self.field.height - self.playerSize - margin):
                    self.positionY += step
            case Const.WEST_DIRECTION:
                if self.positionX > margin:
                    self.positionX -= step
            case _:
                pass

    def shootBall(self):
        pass

    def orientation(self):
        pass
