import random
import sys

import pygame
print(pygame.ver)

# classes from the folders
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot
from Constants import Const

# get clock for pygame (defined as a global variable)
clock = pygame.time.Clock()

if __name__ == "__main__":
    from Actions.GameActions import gameIsRunning

    # init pygame
    pygame.init()

    # title, icon
    pygame.display.set_caption("SoccerRobots Simulation")
    displayIcon = pygame.image.load("resources/SoccerRobotDisplay.png")
    pygame.display.set_icon(displayIcon)

    # window size
    screenWidth, screenHeight = 800, 600

    # scale the player image to the desired size (New width and height)
    ballSize = 35
    playerSize: int = 55
    playerSteps = 2

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
    running = True
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

    # quit Pygame
    pygame.quit()
    sys.exit()
