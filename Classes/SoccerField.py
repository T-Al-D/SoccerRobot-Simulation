"""!
@file
@brief class for SoccerField (main action on Soccerfield)
"""

import pygame
from Actions.Images import loadAndScaleImage
from Classes import Goal


class SoccerField:
    """!
    @brief A class that creates a 'playing flied'.
    """

    def __init__(
        self,
        status: int,
        width: int,
        height: int,
        team1Goal: Goal,
        team2Goal: Goal,
        playTimeInMinutes: int,
        imagePath: str,
    ):
        """!
        @brief Constructor for Soccerfield class.
        Initializes the most necessary data
        """
        # prevention of circular imports
        from Classes.SoccerRobot import SoccerRobot
        from Classes.Ball import Ball

        self._status: int = status
        self._width: int = width
        self._height: int = height
        self._playTimeInMinutes: int = playTimeInMinutes
        self._team1Goal: int = team1Goal
        self._team2Goal: int = team2Goal
        self._players: list[SoccerRobot] = []
        self._ball: Ball = None
        self._image: pygame.image = loadAndScaleImage(
            imagePath, self._width, self.height
        )

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: int):
        self._status = value

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
    def playTimeInMinutes(self):
        return self._playTimeInMinutes

    @playTimeInMinutes.setter
    def playTimeInMinutes(self, value: int):
        self._playTimeInMinutes: int = value

    @property
    def team1Goal(self):
        return self._team1Goal

    @team1Goal.setter
    def team1Goal(self, value: int):
        self._team1Goal = value

    @property
    def team2Goal(self):
        return self._team2Goal

    @team2Goal.setter
    def team2Goal(self, value: int):
        self._team2Goal = value

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value: list):
        self._players = value

    @property
    def ball(self):
        return self._ball

    @ball.setter
    def ball(self, value):
        self._ball = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image: pygame.image = value

    def returnTeamScore(self):
        return [self._team1Score, self._team2Score]

    def changeScore(self):
        if self._team1Score is None:
            self._team1Score = 0
        elif self._team2Score is None:
            self._team2Score = 0
        elif self._team1Score is not None and self._team2Score is not None:
            pass

    def endGame(self):
        pass
