"""!
@file
@brief functions for collision actions 
"""

import pygame


from Actions.Movement import playerCollideMove
from Classes.Ball import Ball
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


def ballMovementsThroughPlayerCollision(players: list[SoccerRobot], ball: Ball):
    """!
    @brief move the ball depending on collision and ballMovements
    the player wants to kick the ball in front of him

    @param players list of SoccerRobots to check for collision
    @param ball the ball Object to be moved

    @return void This function does not return a value.
    """
    from Actions.Movement import ballMovement

    for player in players:
        # playerRectangles.append(player.rectangle)

        collisionDetect = ball.rectangle.colliderect(player.rectangle)
        if collisionDetect:
            # print(f"ball: X {ball.positionX} and Y {ball.positionY}")
            # the "keys" have to be processed further in the Movement method
            ballMovement(ball, player)


def playerCollideWithPlayer(players: list[SoccerRobot]):
    """!
    @brief prevention of players walking 'over' each other
    if players collide, they are not allowed to cross each other

    @param players a list of soccerRobots

    @return void This function does not return a value.
    """
    # print(f"players {players}")
    # Loop through each player and check for collision with others
    for player in players:
        # Check for collision with other players
        for otherPlayer in players:
            # Don't check for collision with itself
            if player != otherPlayer:
                # in case of collision, reset position of player
                if player.rectangle.colliderect(otherPlayer.rectangle):
                    # print(f"player {player} and otherPlayer {otherPlayer}")
                    # If collision detected, reset position to original one
                    playerCollideMove(player)
                    # Exit the loop after correcting position
                    break
