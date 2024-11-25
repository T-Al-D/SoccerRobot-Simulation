import random
import sys

import pygame

# classes from the folders
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


# draw the player
def drawPlayer(displayScreen: pygame.Surface, playerRobot: SoccerRobot, img):
    # create a playerRectangle
    playerRect = pygame.Rect(playerRobot.positionX, playerRobot.positionY, playerRobot.playerSize, playerSize)
    # assign the playerRectangle to a specific image and position, then draw the rect
    displayScreen.blit(img, playerRect.topleft)
    # Optional: Draw a border around the rectangle (for visualization)
    pygame.draw.rect(screen, (0, 0, 0), playerRect, 1)


# complete game logic
def gameIsRunning(displayScreen: pygame.Surface, field: SoccerField, player1: SoccerRobot, player2: SoccerRobot,
                  playerImg):
    # import global variable
    global frames, clock
    frames += 1

    # limit frame rate
    clock.tick(75)

    # get the key that are currently pressed
    keys = pygame.key.get_pressed()

    # Move the player based on key presses
    if keys[pygame.K_LEFT]:
        player1.move(Const.WEST_DIRECTION, playerSteps)
    if keys[pygame.K_RIGHT]:
        player1.move(Const.EAST_DIRECTION, playerSteps)
    if keys[pygame.K_UP]:
        player1.move(Const.NORTH_DIRECTION, playerSteps)
    if keys[pygame.K_DOWN]:
        player1.move(Const.SOUTH_DIRECTION, playerSteps)

    # ball movement through collision
    if (player1.positionX - (player1.playerSize / 2) < field.ballPositionX < player1.positionX + (
            player1.playerSize / 2)) and (
            player1.positionY < field.ballPositionY < player1.positionY + player1.playerSize):
        print(f"player1: X {player1.positionX} and Y {player1.positionY}")
        print(f"ball: X {field.ballPositionX} and Y {field.ballPositionY}")
        if keys[pygame.K_LEFT]:
            field.moveBall(Const.WEST_DIRECTION, playerSteps * 3)
        if keys[pygame.K_RIGHT]:
            field.moveBall(Const.EAST_DIRECTION, playerSteps * 3)

    # random choice for movement for player2
    randomMove = random.choice(Const.allBasicDirections)
    player2.move(randomMove, player2.playerSteps)

    # draw the background image
    displayScreen.blit(backgroundImg, (0, 0))

    # draw the ball and assign rectangle to it
    ballRect = pygame.Rect(field.ballPositionX, field.ballPositionY, field.ballSize, field.ballSize)
    displayScreen.blit(ballImg, ballRect.topleft)
    pygame.draw.rect(screen, (0, 0, 0), ballRect, 1)

    # draw all the player on the field
    for player in soccerField.players:
        drawPlayer(displayScreen, player, playerImg)

    # Update the display
    pygame.display.flip()


if __name__ == "__main__":
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

    # load images
    backgroundImg = pygame.image.load("resources/SoccerFieldBackground2.jpg")
    backgroundImg = pygame.transform.scale(backgroundImg, (screenWidth, screenHeight))  # Scale to fit the window
    soccerRobotImg = pygame.image.load("resources/SoccerRobotPlayer.png")
    soccerRobotImg = pygame.transform.scale(soccerRobotImg, (playerSize, playerSize))
    ballImg = pygame.image.load("resources/Ball2.png")
    ballImg = pygame.transform.scale(ballImg, (ballSize, ballSize))

    # objects
    soccerField = SoccerField(0, screenWidth, screenHeight, 1, ballSize)
    soccerRobot1 = SoccerRobot(1, 1, playerSize, playerSteps, int(screenWidth * 0.82), int(screenHeight / 2.15),
                               soccerField)
    soccerRobot2 = SoccerRobot(2, 2, playerSize, playerSteps, int(screenWidth * 0.1), int(screenHeight / 2.15),
                               soccerField)
    soccerField.players.append(soccerRobot1)
    soccerField.players.append(soccerRobot2)

    # counts the frames during the simulation (if needed)
    frames = 0

    # get clock for pygame
    clock = pygame.time.Clock()

    # define all needed rectangles

    # if the value of running is changed, the application stops
    running = True
    while running:
        # to react to every event, we scan all possible events
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                running = False

        # all game logic is in here
        gameIsRunning(screen, soccerField, soccerRobot1, soccerRobot2, soccerRobotImg)

    # quit Pygame
    pygame.quit()
    sys.exit()
