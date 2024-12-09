"""!
@file
@brief functions for drawing rectangles/images on screen
"""

import pygame

from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot


def drawRectangleOnScreen(
    displayScreen: pygame.Surface, rectangle: pygame.Rect, image: pygame.image
):
    """!
    @brief draw ball on screen
    create a rectangle and draw it on screen with an image on it

    @param displayScreen on what surface to draw the objects (pygame.Surface)
    @param image a pygame.image to draw on the surface
    """
    displayScreen.blit(image, rectangle)


def drawAllPlayers(displayScreen: pygame.Surface, playerList: list[SoccerRobot]):
    """!
    @brief draw all players on screen
    uses other function drawPlayer(...) to draw all players (for-loop)
    @see drawPlayer

    @param displayScreen on what surface to draw the objects (pygame.Surface)
    @param playerList list with all players to be drawn
    """

    # draw all the player on the field and append the created rectangle into array
    for player in playerList:
        drawRectangleOnScreen(displayScreen, player.rectangle, player.image)
