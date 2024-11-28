"""!
@file
@brief functions for drawing rectangles/images on screen
"""

import pygame

from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot


def drawBall(
    displayScreen: pygame.Surface, field: SoccerField, ballImg: pygame.image
) -> pygame.rect:
    """!
    @brief draw ball on screen
    create a rectangle and draw it on screen with an image on it

    @param displayScreen on what surface to draw the ball (pygame.Surface)
    @param SoccerField information from the SoccerField are needed
    @param ballImg image with gets drawn onto the rectangle

    @return ball rectangle
    """
    ballRect = pygame.Rect(
        field.ballPositionX, field.ballPositionY, field.ballSize, field.ballSize
    )
    displayScreen.blit(ballImg, ballRect)
    return ballRect


def drawPlayer(
    displayScreen: pygame.Surface, playerRobot: SoccerRobot, playerImg: pygame.image
) -> pygame.rect:
    """!
    @brief draw player on screen
    create a rectangle and draw it on screen with an image on it

    @param displayScreen on what surface to draw the player (pygame.Surface)
    @param playerRobot information from the SoccerRobot are needed
    @param playerImg image with gets drawn onto the rectangle

    @return player rectangle
    """
    # create a playerRectangle
    playerRect = pygame.Rect(
        playerRobot.positionX,
        playerRobot.positionY,
        playerRobot.playerSize,
        playerRobot.playerSize,
    )
    # assign the playerRectangle to a specific image and position, then draw the rect
    displayScreen.blit(playerImg, playerRect)
    return playerRect


def drawAllPlayers(
    displayScreen: pygame.Surface, field: SoccerField, playerImg: pygame.image
):
    """!
    @brief draw all players on screen
    uses other function drawPlayer(...) to draw all players (for-loop)
    @see drawPlayer

    @param displayScreen on what surface to draw the objects (pygame.Surface)
    @param field information packed inside SoccerField
    @param playerImg image with gets drawn onto the rectangle

    @return Array of all player rectangels (for collision check)
    """
    playerRectangles = []

    # draw all the player on the field and append the created rectangle into array
    for player in field.players:
        playerRect = drawPlayer(displayScreen, player, playerImg)
        playerRectangles.append(playerRect)

    # return playerRectangles for collision detection
    return playerRectangles
