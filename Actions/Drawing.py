import pygame

from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot


# draw the ball on surface
def drawBall(displayScreen: pygame.Surface, field: SoccerField, ballImg):
    ballRect = pygame.Rect(
        field.ballPositionX, field.ballPositionY, field.ballSize, field.ballSize
    )
    displayScreen.blit(ballImg, ballRect)
    return ballRect


# draw the player on surface
def drawPlayer(displayScreen: pygame.Surface, playerRobot: SoccerRobot, img):
    # create a playerRectangle
    playerRect = pygame.Rect(
        playerRobot.positionX,
        playerRobot.positionY,
        playerRobot.playerSize,
        playerRobot.playerSize,
    )
    # assign the playerRectangle to a specific image and position, then draw the rect
    displayScreen.blit(img, playerRect)
    return playerRect


# draw all players
def drawAllPlayers(displayScreen: pygame.Surface, field: SoccerField, playerImg):
    playerRectangles = []

    # draw all the player on the field and append the created rectangle into array
    for player in field.players:
        playerRect = drawPlayer(displayScreen, player, playerImg)
        playerRectangles.append(playerRect)

    # return playerRectangles for collision detection
    return playerRectangles
