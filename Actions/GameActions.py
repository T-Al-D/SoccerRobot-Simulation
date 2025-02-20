"""!
@file
@brief all game logic is executed here in abstract form
"""

import pygame

from Actions.Collision import (
    ballMoveOnPlayerCollision,
    playerCollideWithPlayer,
)
from Actions.Drawing import drawGoalsInScreen, drawRectangleOnScreen, drawText
from Actions.Movement import playerManualMove
from Actions.RobotChoice import playersNextChoice
from Classes.Ball import Ball
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


# secondary "main" function, all gamelogic is defined here
# local imports in the method to prevent circular imports!
def gameIsRunning(
    fps: int,
    displayScreen: pygame.Surface,
    surfaceLayer: pygame.Surface,
    field: SoccerField,
    ball: Ball,
    player1: SoccerRobot,
    player2: SoccerRobot,
):
    """!
    @brief Executes the game logic, updating the game state.

    This function manages the core game logic, handling actions for all players, updating the soccer field,
    and rendering the appropriate images for players, ball, and background

    @param fps frame rate limit
    @param displayScreen the screen where everything is shown
    @param surfaceLayer a "layer" ontop the screen -> accepts alpha argument
    @param field The `SoccerField` object representing the game/simulation field.
    @param ball the ball object
    @param player1 The `SoccerRobot` object representing the first player.
    @param player2 The `SoccerRobot` object representing the second player.

    @return void This function does not return a value.
    """
    # local import of functions (prevention of circular imports)
    from Actions.Drawing import drawAllPlayers

    # Import the (global variable) clock from main.py
    from main import clock

    # limit frame rate
    clock.tick(fps)

    ################# DRAWING ##################
    # "draw" the label on screen
    labelImage = drawText("Time duration:")

    # draw the labelImage
    displayScreen.blit(labelImage, (0, 0))

    # draw the background image , leaving out the top - margin for the label
    surfaceLayer.blit(field.image, (0, 0))

    # draw the ball and assign rectangle to it
    drawRectangleOnScreen(surfaceLayer, ball.rectangle, ball.image)

    # draw the goals to make them obvious
    drawGoalsInScreen(surfaceLayer, [field.team1Goal, field.team2Goal], (255, 255, 225))

    # playerRectangles for collision detection
    drawAllPlayers(surfaceLayer, field.players)

    # draw "second surface/layer"
    displayScreen.blit(surfaceLayer, (0, Const.TOP_MARGIN))

    ################# KEYS #################
    # get the key that are currently pressed
    keys = pygame.key.get_pressed()

    ################# MOVEMENT #################
    # movement for player1 (soccerRobots)
    playerManualMove(keys, player1)
    # function for giving robots "AI-intelligence"
    playersNextChoice(player2, player1, ball)

    ################# COLLISION ################
    # check collision with ball
    ballMoveOnPlayerCollision(field.players, ball)
    # check collision between players
    playerCollideWithPlayer(field.players)

    ################# RESET #####################
    for player in field.players:
        player.resetDirection()
    ball.standingStill()

    # Update the display
    pygame.display.flip()
