"""!
@file
@brief class for SoccerField (main action on Soccerfield)
"""

import pygame
from Actions.Images import loadAndScaleImage
from Constants import Const


class SoccerField:
    """!
    @brief A class that creates a 'playing flied'.
    """

    def __init__(
        self,
        status: int,
        width: int,
        height: int,
        playTimeInMinutes: int,
        imagePath: str,
    ):
        """!
        @brief Constructor for Soccerfield class.
        Initializes the most necessary data
        """
        # prevention of circular imports
        from Classes.SoccerRobot import SoccerRobot
        from Classes import Ball

        self.status: int = status
        self.width: int = width
        self.height: int = height
        self.playTimeInMinutes: int = playTimeInMinutes
        self.team1Score: int = 0
        self.team2Score: int = 0
        self.team1GoalStatus: int = 0
        self.team2GoalStatus: int = 0

        self.players: list[SoccerRobot] = []
        self.ball: Ball = None
        self.image = loadAndScaleImage(imagePath, self.width, self.height)

    def returnTeamScore(self):
        return [self.team1Score, self.team2Score]

    def changeScore(self):
        if self.team1Score is None:
            self.team1Score = 0
        elif self.team2Score is None:
            self.team2Score = 0
        elif self.team1Score is not None and self.team2Score is not None:
            pass

    def endGame(self):
        pass
