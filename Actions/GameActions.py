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
    from Actions.Collision import ballMovementsThroughCollision
    from Actions.Drawing import drawPlayer
    from Actions.Movement import playerMovement

    # Import the clock from main.py
    from main import clock

    # limit frame rate
    clock.tick(fps)

    # get the key that are currently pressed
    keys = pygame.key.get_pressed()

    # movement for player1 (soccerRobots)
    playerMovement(keys, player1)

    # random choice for movement for player2
    randomMove = random.choice(Const.allBasicDirections)
    player2.move(randomMove, player2.playerSteps)

    # draw the background image
    displayScreen.blit(backgroundImg, (0, 0))

    # draw the ball and assign rectangle to it
    ballRect = pygame.Rect(
        field.ballPositionX, field.ballPositionY, field.ballSize, field.ballSize
    )
    displayScreen.blit(ballImg, ballRect)

    # playerRectangles for collision detection
    playerRectangles = []

    # draw all the player on the field
    for player in field.players:
        playerRect = drawPlayer(displayScreen, player, playerImg)
        playerRectangles.append(playerRect)

    # collision
    ballMovementsThroughCollision(keys, playerRectangles, ballRect, field)

    # Update the display
    pygame.display.flip()
