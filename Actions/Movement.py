"""!
@file 
@brief function for movement in simulation
"""

import pygame
from Classes.Ball import Ball
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


# Move the player based on key pressed
def playerMovement(keys: pygame.key, player: SoccerRobot):
    """!
    @brief player movements depending on what key is pressed

    @param keys the key events that got pressed
    @param player the soccer robot that is being moved / moves

    @return void This function does not return a value.
    """
    if keys[pygame.K_LEFT]:
        player.move(Const.WEST_DIRECTION)
    elif keys[pygame.K_RIGHT]:
        player.move(Const.EAST_DIRECTION)
    elif keys[pygame.K_UP]:
        player.move(Const.NORTH_DIRECTION)
    elif keys[pygame.K_DOWN]:
        player.move(Const.SOUTH_DIRECTION)


def ballMovement(keys: pygame.key, ball: Ball):
    """!
    @brief ball movements depending on what key is pressed

    @param keys the key events that got pressed
    @param ball the ball Object

    @return void This function does not return a value.
    """
    if keys[pygame.K_LEFT]:
        ball.move(Const.WEST_DIRECTION)
    elif keys[pygame.K_RIGHT]:
        ball.move(Const.EAST_DIRECTION)
    elif keys[pygame.K_UP]:
        ball.move(Const.NORTH_DIRECTION)
    elif keys[pygame.K_DOWN]:
        ball.move(Const.SOUTH_DIRECTION)
