from Classes.SoccerField import SoccerField
from Constants import Const


class SoccerRobot:
    """
    A SoccerRobot is the main actor on the SoccerField
    """

    # constructor / attributes
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

    # Methods
    def move(self, direction: int, step: float):
        margin = 20
        match direction:
            case Const.NORTH_DIRECTION:
                if self.positionY > margin:
                    self.positionY -= step
            case Const.NORTH_EAST_DIRECTION:
                pass
            case Const.EAST_DIRECTION:
                if self.positionX < self.field.width - self.playerSize - margin:
                    self.positionX += step
            case Const.SOUTH_EAST_DIRECTION:
                pass
            case Const.SOUTH_DIRECTION:
                if self.positionY < self.field.height - self.playerSize - margin:
                    self.positionY += step
            case Const.SOUTH_WEST_DIRECTION:
                pass
            case Const.WEST_DIRECTION:
                if self.positionX > margin:
                    self.positionX -= step
            case Const.NORTH_WEST_DIRECTION:
                pass
            case _:
                pass

    def shootBall(self):
        pass

    def orientation(self):
        pass
