from Constants import Const


class SoccerField:
    """
    The main action happens on a SoccerField
    """

    def __init__(
        self,
        status: int,
        width: int,
        height: int,
        playTimeInMinutes: int,
        ballSize: int,
    ):
        from Classes.SoccerRobot import SoccerRobot  # prevention of circular imports

        self.status: int = status
        self.width: int = width
        self.height: int = height
        self.playTimeInMinutes: int = playTimeInMinutes
        self.ballSize: int = ballSize
        self.team1Score: int = 0
        self.team2Score: int = 0
        self.team1GoalStatus: int = 0
        self.team2GoalStatus: int = 0
        self.ballStatus: int = 0
        self.ballPositionX: int = int(width / 2.07)
        self.ballPositionY: int = int(height / 2.09)
        self.players: list[SoccerRobot] = []

    # Methods
    def returnTeamScore(self):
        return [self.team1Score, self.team2Score]

    def changeScore(self):
        if self.team1Score is None:
            self.team1Score = 0
        elif self.team2Score is None:
            self.team2Score = 0
        elif self.team1Score is not None and self.team2Score is not None:
            pass

    def getBallPosition(self):
        pass

    def moveBall(self, direction: int, step: float):
        margin = 20
        match direction:
            case Const.NORTH_DIRECTION:
                if self.ballPositionY > margin:
                    self.ballPositionY -= step
            case Const.NORTH_EAST_DIRECTION:
                pass
            case Const.EAST_DIRECTION:
                if self.ballPositionX < self.width - self.ballSize - margin:
                    self.ballPositionX += step
            case Const.SOUTH_EAST_DIRECTION:
                pass
            case Const.SOUTH_DIRECTION:
                if self.ballPositionY < self.height - self.ballSize + margin:
                    self.ballPositionY += step
            case Const.SOUTH_WEST_DIRECTION:
                pass
            case Const.WEST_DIRECTION:
                if self.ballPositionX > margin:
                    self.ballPositionX -= step
            case Const.NORTH_WEST_DIRECTION:
                pass
            case _:
                pass

    def endGame(self):
        pass