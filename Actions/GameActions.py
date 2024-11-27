# complete game logic
import random
import pygame


from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


# secondary "main" function, all gamelogic is defined here
# local imports in the method to prevent circular imports!
def gameIsRunning(
    fps: int,
    displayScreen: pygame.Surface,
    field: SoccerField,
    player1: SoccerRobot,
    player2: SoccerRobot,
    playerImg,
    ballImg,
    backgroundImg,
):
    # local import of functions
    from Actions.Drawing import drawBall
    from Actions.Drawing import drawAllPlayers
    from Actions.Movement import playerMovement
    from Actions.Collision import playerCollideWithPlayer
    from Actions.Collision import ballMovementsThroughCollision

    # Import the (global variable) clock from main.py
    from main import clock

    # limit frame rate
    clock.tick(fps)

    ################# DRAWING ##################
    # draw the background image
    displayScreen.blit(backgroundImg, (0, 0))

    # draw the ball and assign rectangle to it
    ballRect = drawBall(displayScreen, field, ballImg)

    # playerRectangles for collision detection
    playerRectangles = drawAllPlayers(displayScreen, field, playerImg)

    ################# MOVEMENT #################
    # get the key that are currently pressed
    keys = pygame.key.get_pressed()

    # movement for player1 (soccerRobots)
    playerMovement(keys, player1)

    # random choice for movement for player2
    randomMove = random.choice(Const.allBasicDirections)
    player2.move(randomMove, player2.playerSteps)

    ################# COLLISION ################
    ballMovementsThroughCollision(keys, playerRectangles, ballRect, field)
    playerCollideWithPlayer(keys, playerRectangles)

    # Update the display
    pygame.display.flip()
