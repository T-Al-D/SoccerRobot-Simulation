"""!
@file
@brief functions for collision actions 
"""

import pygame


from Actions.Movement import playerCollideMove
from Classes.Ball import Ball
from Classes.Goal import Goal
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


def ballMoveOnPlayerCollision(players: list[SoccerRobot], ball: Ball):
    """!
    @brief move the ball depending on collision and ballMovements
    the player wants to kick the ball in front of him

    @param players list of SoccerRobots to check for collision
    @param ball the ball Object to be moved

    @return void This function does not return a value.
    """
    for player in players:
        collisionDetect = ball.rectangle.colliderect(player.rectangle)
        if collisionDetect:
            # print(f"ball: X {ball.positionX} and Y {ball.positionY}")
            # the "keys" have to be processed further in the Movement method
            ball.currentDirection = player.currentDirection
            ball.move()


def playerCollideWithPlayer(players: list[SoccerRobot]):
    """!
    @brief prevention of players walking 'over' each other
    if players collide, they are not allowed to cross each other

    @param players a list of soccerRobots

    @return void This function does not return a value.
    """
    # Loop through each player and check for collision with others
    for player in players:
        # Check for collision with other players
        for otherPlayer in players:
            # Don't check for collision with itself
            if player != otherPlayer:
                # in case of collision, reset position of player
                if player.rectangle.colliderect(otherPlayer.rectangle):
                    # If collision detected, reset position to original one
                    playerCollideMove(player)
                    # Exit the loop after correcting position
                    break


def checkBallCollisionWithGoal(ball: Ball, goals: list[Goal]):
    """!
    @brief if the ball as any collision with any goal,
    reset ball position and give Team Points

    @param ball the soccer-ball object

    @return void This function does not return a value.
    """
    # Loop through each goal and check for collision
    for goal in goals:
        if ball.rectangle.colliderect(goal.rectangle):
            print("GOAL!!!")
            ball.resetBallToMiddle()
