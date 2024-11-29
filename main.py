"""!
@file 
@brief "main" file in the project: Code starts here.
@author BluMay, EN-AK, T-Al-D
"""

import sys
import os
import pygame

# classes from the folders
from Classes.Ball import Ball
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot

# pygame sound not use real sound hardware
os.environ["SDL_AUDIODRIVER"] = "dummy"  # Disables audio

# get clock for pygame (defined as a global variable)
clock = pygame.time.Clock()


# "main" function, all objects are defined here
def runSimulation(runForDuration: bool = False, durationInMs: int = 0):
    """!
    @brief executes the logic, can me run for limited time (in tests)

    @param runForDuration tells the function if it has to run for limited time
    @param durationInMs int value for amount of ms

    @return void This function does not return a value.
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
    ballStep: int = int(ballSize / 2)
    playerSize: int = 55
    playerSteps: int = 2

    # create a screen (width, height)
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    # objects
    soccerField = SoccerField(
        0, screenWidth, screenHeight, 15, "resources/SoccerFieldBackground2.jpg"
    )
    ball = Ball(ballSize, ballStep, "resources/Ball2.png", soccerField)
    soccerRobot1 = SoccerRobot(
        1,
        1,
        playerSize,
        playerSteps,
        int(screenWidth * 0.82),
        int(screenHeight / 2.15),
        "resources/SoccerRobotPlayer.png",
        soccerField,
    )
    soccerRobot2 = SoccerRobot(
        2,
        2,
        playerSize,
        playerSteps,
        int(screenWidth * 0.1),
        int(screenHeight / 2.15),
        "resources/SoccerRobotPlayer.png",
        soccerField,
    )
    soccerField.players.append(soccerRobot1)
    soccerField.players.append(soccerRobot2)

    # if the value of running is changed, the application stops
    running: bool = True
    # Track when the loop starts
    startTicks = pygame.time.get_ticks()

    while running:
        # if we only want to run our simulation for a short time during the tests
        if runForDuration is True:
            # if we've run for the duration time, stop
            if (pygame.time.get_ticks() - startTicks) >= durationInMs:
                running = False

        # to react to every event, we scan all possible events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # all game logic is in here
        gameIsRunning(75, screen, soccerField, ball, soccerRobot1, soccerRobot2)
        # Ensure the window gets updated
        pygame.display.update()

    pygame.quit()


# "main" function, all objects are defined here
if __name__ == "__main__":
    """!
    @brief Initializes all needed information for the programm/simulation
    simulation runs in endless while-loop, until exit
    """
    runSimulation()
    sys.exit()
