"""!
@file
@brief functions for collision actions 
"""

import pygame


from Classes.SoccerField import SoccerField
from Constants import Const


def ballMovementsThroughCollision(
    keys: pygame.key,
    playerRectangles: pygame.Rect,
    ballRect: pygame.Rect,
    field: SoccerField,
):
    """!
    @brief move the ball depending on collision and ballMovements
    the player wants to kick the ball in front of him

    @param keys the key events that got pressed
    @param playerRectangles array with player reactangles to check for collision
    @param ballRect the rectangle which gets checked for collision
    @param field needed later on to chenge the position of the ball

    @return void This function does not return a value.
    """
    from Actions.Movement import ballMovement

    collisionDetect = ballRect.collidelist(playerRectangles)
    if collisionDetect >= 0:
        # print(f"ball: X {field.ballPositionX} and Y {field.ballPositionY}")
        # print(collisionDetect)
        ballSteps = ballRect.width / 2
        ballMovement(keys, field, ballSteps)


def playerCollideWithPlayer(keys: pygame.key, playerRectangles: pygame.Rect):
    """!
    @brief prevention of players walking 'over' each other
    if players collide, they are not allowed to cross each other

    @param keys the key events that got pressed
    @param playerRectangles array with player reactangles to check for collision

    @return void This function does not return a value.
    """
    for playerRect in playerRectangles:
        collisionDetect = playerRect.collidelist(playerRectangles)
        if collisionDetect >= 0:
            # print(f"playerRect: {playerRect}, collisionDetect{collisionDetect}")
            pass
