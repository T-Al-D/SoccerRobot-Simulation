"""!
@file
@brief computer generated next move for the robot
"""

from Classes.Ball import Ball
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


def playersNextChoice(player: SoccerRobot, otherPlayer: SoccerRobot, ball: Ball):
    """!
    @brief generated the next possible move for the soccerRobot

    @param player one soccerRobot
    @param otherPlayer the soccerRobot to consider
    @param ball ball-object

    @return void no value return
    """
    # calc the differences in position x/y between the player and the ball
    distanceXToBall = ball.positionX - player.positionX
    distanceYToBall = ball.positionY - player.positionY

    # calc the differences in position between the player and the otherPlayer
    distanceXToOtherPlayer = otherPlayer.positionX - player.positionX
    distanceYToOtherPlayer = otherPlayer.positionY - player.positionY

    # start acting at this distance
    actingDistance: int = int(player.size * 1.2)

    playersNextMove: int = 0
    # Determine the movement direction based on the differences between player and ball
    if abs(distanceXToBall) > abs(distanceYToBall):
        # Move horizontally
        if distanceXToBall > 0:
            # ball is to the right, move east
            playersNextMove = Const.EAST_DIRECTION
        else:
            # ball is to the left, move west
            playersNextMove = Const.WEST_DIRECTION
    else:
        # Move vertically
        if distanceYToBall > 0:
            # ball is below, move south
            playersNextMove = Const.SOUTH_DIRECTION
        else:
            # ball is above, move north
            playersNextMove = Const.NORTH_DIRECTION

    # now consider the position of (otherPlayer) and adjust
    if (
        abs(distanceXToOtherPlayer) < actingDistance
        and abs(distanceYToOtherPlayer) < actingDistance
    ):
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

    # print(f"playersNextMove {playersNextMove} ")
    player.currentDirection = playersNextMove
    player.move()
    # playersNextMove = random.choice(Const.ALL_BASIC_ARROWKEYS)
    # playerMovement(playersNextMove, player)
