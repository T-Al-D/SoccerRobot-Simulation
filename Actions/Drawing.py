import pygame

from Classes.SoccerRobot import SoccerRobot


# draw the player
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

    # return playerRectangle for collision detection
    return playerRect
