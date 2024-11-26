import pygame
from Classes.SoccerField import SoccerField
from Classes.SoccerRobot import SoccerRobot
from Constants import Const


# Move the player based on key pressed
def playerMovement(keys: pygame.key, player: SoccerRobot):
    if keys[pygame.K_LEFT]:
        player.move(Const.WEST_DIRECTION, player.playerSteps)
    elif keys[pygame.K_RIGHT]:
        player.move(Const.EAST_DIRECTION, player.playerSteps)
    elif keys[pygame.K_UP]:
        player.move(Const.NORTH_DIRECTION, player.playerSteps)
    elif keys[pygame.K_DOWN]:
        player.move(Const.SOUTH_DIRECTION, player.playerSteps)


def ballMovement(keys: pygame.key, field: SoccerField, ballSteps: int):
    if keys[pygame.K_LEFT]:
        field.moveBall(Const.WEST_DIRECTION, ballSteps)
    elif keys[pygame.K_RIGHT]:
        field.moveBall(Const.EAST_DIRECTION, ballSteps)
    elif keys[pygame.K_UP]:
        field.moveBall(Const.NORTH_DIRECTION, ballSteps)
    elif keys[pygame.K_DOWN]:
        field.moveBall(Const.SOUTH_DIRECTION, ballSteps)
