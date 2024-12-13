"""!
@file
@brief all game logic is executed here in abstract form
"""

import random
import pygame


from Actions.Collision import ballMovementsThroughPlayerCollision
from Actions.Drawing import drawRectangleOnScreen, drawText
from Classes.Ball import Ball
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


# secondary "main" function, all gamelogic is defined here
# local imports in the method to prevent circular imports!
def gameIsRunning(
    fps: int,
    displayScreen: pygame.Surface,
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
    @param field The `SoccerField` object representing the game/simulation field.
    @param ball the ball object
    @param player1 The `SoccerRobot` object representing the first player.
    @param player2 The `SoccerRobot` object representing the second player.

    @return void This function does not return a value.
    """
    # local import of functions (prevention of circular imports)
    from Actions.Drawing import drawAllPlayers
    from Actions.Movement import playerMovement
    from Actions.Collision import playerCollideWithPlayer

    # Import the (global variable) clock from main.py
    from main import clock

    # limit frame rate
    clock.tick(fps)

    ################# DRAWING ##################
    # "draw" the label on screen
    labelImage = drawText('Time duration:')
    displayScreen.blit(labelImage, (0, 0))

    # draw the background image , leaving out the top - margin for the label
    displayScreen.blit(field.image, (0, Const.TOP_MARGIN))

    # draw the ball and assign rectangle to it
    drawRectangleOnScreen(displayScreen, ball.rectangle, ball.image)

    # playerRectangles for collision detection
    drawAllPlayers(displayScreen, field.players)

    ################# KEYS #################
    # get the key that are currently pressed
    keys = pygame.key.get_pressed()

    ################# COLLISION ################
    ballMovementsThroughPlayerCollision(keys, field.players, ball)
    # playerCollideWithPlayer(keys, playerRectangles)

    ################# MOVEMENT #################
    # movement for player1 (soccerRobots)
    playerMovement(keys, player1)

    # random choice for movement for player2
    randomMove = random.choice(Const.allBasicDirections)
    player2.move(randomMove)

    # Update the display
    pygame.display.flip()
