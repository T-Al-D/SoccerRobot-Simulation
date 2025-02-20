"""!
@file
@brief functions for drawing rectangles/images on screen
"""

import pygame

from Classes.Goal import Goal
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot


def drawText(text: str):
    """!
    @brief create label

    @param text input string

    @return labelImg text renderd in image
    """
    textColor = (255, 255, 255)
    font = pygame.font.SysFont("Jokerman", 35)
    labelImg = font.render(text, True, textColor)
    return labelImg


def drawRectangleOnScreen(
    surface: pygame.Surface, rectangle: pygame.Rect, image: pygame.image
):
    """!
    @brief draw ball on screen
    create a rectangle and draw it on screen with an image on it

    @param surface on what surface to draw the objects (pygame.Surface)
    @param image a pygame.image to draw on the surface

    @return void
    """
    surface.blit(image, rectangle)


def drawGoalsInScreen(surface: pygame.Surface, goals: list[Goal], color: tuple[int]):
    """!
    @brief draw the goals onto the screen/surface
    create a rectangle, but only with border

    @param surface on what surface to draw the objects (pygame.Surface)
    @param goals list of goals to be drawn

    @return void
    """
    for goal in goals:
        pygame.draw.rect(
            surface,
            color,
            (goal.positionX, goal.positionY, goal.width, goal.height),
            width=5,
        )


def drawAllPlayers(surface: pygame.Surface, playerList: list[SoccerRobot]):
    """!
    @brief draw all players on screen
    uses other function drawPlayer(...) to draw all players (for-loop)
    @see drawPlayer

    @param surface on what surface to draw the objects (pygame.Surface)
    @param playerList list with all players to be drawn

    @return void
    """

    # draw all the player on the field and append the created rectangle into array
    for player in playerList:
        drawRectangleOnScreen(surface, player.rectangle, player.image)
