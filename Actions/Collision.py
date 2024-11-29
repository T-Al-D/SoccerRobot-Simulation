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
    # Loop through each player and check for potential collision
    for i, playerRect in enumerate(playerRectangles):
        # Check for collision with every other player (except itself)
        for j, otherRect in enumerate(playerRectangles):
            if i != j:  # Prevent self-collision
                if playerRect.colliderect(otherRect):
                    # Calculate the difference in position (delta) between the two players
                    deltaX = playerRect.centerx - otherRect.centerx
                    deltaY = playerRect.centery - otherRect.centery

                    print(f"Collision between {deltaX} and {deltaY} !")
                    # Move player in the opposite direction of the collision by a fixed amount
                    step = 20
                    if abs(deltaX) < abs(deltaY):
                        # perdendicular movement
                        if deltaY > 0:
                            playerRect.y += step  # Move down
                        else:
                            playerRect.y -= step  # Move up
                    else:
                        # horizontal movement
                        if deltaX > 0:
                            playerRect.x += step  # Move right
                        else:
                            playerRect.x -= step  # Move left

                    # Prevent players from getting too close after collision
                    if playerRect.colliderect(otherRect):
                        playerRect.x, playerRect.y = (
                            playerRect.x - step,
                            playerRect.y - step,
                        )

                    # Exit after one collision check
                    break
