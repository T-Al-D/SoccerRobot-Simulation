"""!
@file 
@brief "main" file in the project: Code starts here.
@author BluMay, EN-AK, T-Al-D
"""

import sys

import pygame


# classes from the folders
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot
from Constants import Const

# get clock for pygame (defined as a global variable)
clock = pygame.time.Clock()

# "main" function, all objects are defined here
if __name__ == "__main__":
    """!
    @brief Initializes all needed information for the programm/simulation
    simulation runs in endless while-loop, until exit
    """
    from Actions.GameActions import gameIsRunning

    # init pygame
    pygame.init()

    # title, icon
    pygame.display.set_caption("SoccerRobots Simulation")
    displayIcon = pygame.image.load("resources/SoccerRobotDisplay.png")
    pygame.display.set_icon(displayIcon)

    # window size
    screenWidth: int = 800
    screenHeight: int = 600

    # scale the player image to the desired size (New width and height)
    ballSize: int = 35
    playerSize: int = 55
    playerSteps: int = 2

    # create a screen (width, height)
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    # load images and scale
    backgroundImg = pygame.image.load("resources/SoccerFieldBackground2.jpg")
    backgroundImg = pygame.transform.scale(backgroundImg, (screenWidth, screenHeight))
    soccerRobotImg = pygame.image.load("resources/SoccerRobotPlayer.png")
    soccerRobotImg = pygame.transform.scale(soccerRobotImg, (playerSize, playerSize))
    ballImg = pygame.image.load("resources/Ball2.png")
    ballImg = pygame.transform.scale(ballImg, (ballSize, ballSize))

    # objects
    soccerField = SoccerField(0, screenWidth, screenHeight, 1, ballSize)
    soccerRobot1 = SoccerRobot(
        1,
        1,
        playerSize,
        playerSteps,
        int(screenWidth * 0.82),
        int(screenHeight / 2.15),
        soccerField,
    )
    soccerRobot2 = SoccerRobot(
        2,
        2,
        playerSize,
        playerSteps,
        int(screenWidth * 0.1),
        int(screenHeight / 2.15),
        soccerField,
    )
    soccerField.players.append(soccerRobot1)
    soccerField.players.append(soccerRobot2)

    # if the value of running is changed, the application stops
    running: bool = True
    while running:
        # to react to every event, we scan all possible events
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False

        # all game logic is in here
        gameIsRunning(
            75,
            screen,
            soccerField,
            soccerRobot1,
            soccerRobot2,
            soccerRobotImg,
            ballImg,
            backgroundImg,
        )

    # quit programm / pygame
    pygame.quit()
    sys.exit()
