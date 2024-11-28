import pygame
import os

# classes from the folders
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot

# pygame sound not use real sound hardware
os.environ["SDL_AUDIODRIVER"] = "dummy"  # Disables audio

# get clock for pygame (defined as a global variable)
clock = pygame.time.Clock()


# "main" function, all objects are defined here
def runAlternateMainForDuration(durationInMs):
    """
    Runs the game for a specific amount of time (in milliseconds).
    """
    from Actions.Images import loadAndScaleImage
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

    # load and scale images
    backgroundImg = loadAndScaleImage(
        "resources/SoccerFieldBackground2.jpg", screenWidth, screenHeight
    )
    soccerRobotImg = loadAndScaleImage(
        "resources/SoccerRobotPlayer.png", playerSize, playerSize
    )
    ballImg = loadAndScaleImage("resources/Ball2.png", ballSize, ballSize)

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
    # Track when the loop starts
    startTicks = pygame.time.get_ticks()

    while running:
        # if we've run for the duration time, stop
        if (pygame.time.get_ticks() - startTicks) >= durationInMs:
            running = False

        # to react to every event, we scan all possible events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

    pygame.quit()
