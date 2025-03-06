"""!
@file
@brief computer generated next move for the robot
"""

from Classes.Ball import Ball
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


def kickBall(distanceXPlayerToBall: int, distanceYPlayerToBall: int) -> int:
    """!
    @brief kick the ball in one direction

    @param distanceXPlayerToBall the x distance betwwen player and ball
    @param distanceYPlayerToBall the y distance betwwen player and ball

    @return nextPossibleMove CONST-integer for the next move
    """
    nextPossibleMove = 0
    # Move horizontally
    if abs(distanceXPlayerToBall) > abs(distanceYPlayerToBall):
        # Move horizontally
        if distanceXPlayerToBall > 0:
            # ball is to the right, move east
            nextPossibleMove = Const.EAST_DIRECTION
        else:
            # ball is to the left, move west
            nextPossibleMove = Const.WEST_DIRECTION
    else:
        # Move vertically
        if distanceYPlayerToBall > 0:
            #
            nextPossibleMove = Const.SOUTH_DIRECTION
        else:
            nextPossibleMove = Const.NORTH_DIRECTION
    return nextPossibleMove


def goAroundBall(player: SoccerRobot, ball: Ball) -> int:
    """!
    @brief go around the ball befor kicking it

    @param player one soccerRobot
    @param ball ball-object

    @return nextPossibleMove CONST-integer for the next move
    """
    nextPossibleMove: int = 0
    # to move around the ball you have to be either “higher” or “lower” than the ball
    # decide based, if ball higher or lower than half

    # ball in upper "half"
    if (ball.field.height / 2) > ball.positionY:
        # ball "lower" than player AND further away from goal
        if ball.positionY + player.size < player.positionY:
            if player.assignedGoal == 1:
                nextPossibleMove = Const.EAST_DIRECTION
            else:
                nextPossibleMove = Const.WEST_DIRECTION
        else:
            nextPossibleMove = Const.SOUTH_DIRECTION

    # ball in lower half
    else:
        # ball "higher" than player AND further away from goal
        if ball.positionY + player.size > player.positionY:
            if player.assignedGoal == 1:
                nextPossibleMove = Const.EAST_DIRECTION
            else:
                nextPossibleMove = Const.WEST_DIRECTION
        else:
            nextPossibleMove = Const.NORTH_DIRECTION

    return nextPossibleMove


def evadeOtherPlayer(distanceXToOtherPlayer: int, distanceYToOtherPlayer: int) -> int:
    """!
    @brief generate move to evade otherPlayer

    @param player one soccerRobot
    @param otherPlayer the soccerRobot to consider

    @return nextPossibleMove as int
    """
    playersNextMove: int = 0
    # If Player 1 is too close, avoid collision
    # Move away from Player 1
    if distanceXToOtherPlayer > 0:
        # Player 1 is to the right, move left
        playersNextMove = Const.WEST_DIRECTION
    elif distanceXToOtherPlayer < 0:
        # Player 1 is to the left, move right
        playersNextMove = Const.EAST_DIRECTION

    if distanceYToOtherPlayer > 0:
        # Player 1 is below, move up
        playersNextMove = Const.NORTH_DIRECTION
    elif distanceYToOtherPlayer < 0:
        # Player 1 is above, move down
        playersNextMove = Const.SOUTH_DIRECTION
    return playersNextMove


def playersNextChoice(player: SoccerRobot, otherPlayer: SoccerRobot, ball: Ball) -> int:
    """!
    @brief generate the next possible move for the soccerRobot

    @param player one soccerRobot
    @param otherPlayer the soccerRobot to consider
    @param ball ball-object

    @return void no value return
    """
    # calculate distance between player and other objects
    distanceXPlayerToBall = ball.positionX - player.positionX
    distanceYPlayerToBall = ball.positionY - player.positionY

    distanceXToOtherPlayer = otherPlayer.positionX - player.positionX
    distanceYToOtherPlayer = otherPlayer.positionY - player.positionY

    distanceXPlayerToGoal = player.assignedGoal.x - player.positionX
    distanceYPlayerToGoal = player.assignedGoal.y - player.positionY

    distanceXBallToGoal = player.assignedGoal.x - ball.positionX
    distanceYBallToGoal = player.assignedGoal.y - ball.positionY

    # start acting at this distance
    actingDistance: int = int(player.size * 1.4)

    playersNextMove: int = 0
    # Determine the movement direction based on the differences between player and ball
    if distanceXBallToGoal + (player.size / 1.68) < distanceXPlayerToGoal:
        playersNextMove = kickBall(distanceXPlayerToBall, distanceYPlayerToBall)
    else:
        playersNextMove = goAroundBall(player, ball)

    # now consider the position of (otherPlayer) and adjust
    if (
        abs(distanceXToOtherPlayer) < actingDistance
        and abs(distanceYToOtherPlayer) < actingDistance
    ):
        playersNextMove = evadeOtherPlayer(
            distanceXToOtherPlayer, distanceYToOtherPlayer
        )

    # print(f"playersNextMove {playersNextMove} ")
    player.currentDirection = playersNextMove
    player.move()
