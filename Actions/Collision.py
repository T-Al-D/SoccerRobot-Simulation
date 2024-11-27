import pygame


from Classes.SoccerField import SoccerField
from Constants import Const


# depending on the collision with the ball
def ballMovementsThroughCollision(
    keys: pygame.key,
    playerRectangles: pygame.Rect,
    ballRect: pygame.Rect,
    field: SoccerField,
):
    from Actions.Movement import ballMovement

    collisionDetect = ballRect.collidelist(playerRectangles)
    if collisionDetect >= 0:
        # print(f"ball: X {field.ballPositionX} and Y {field.ballPositionY}")
        # print(collisionDetect)
        ballSteps = ballRect.width / 2
        ballMovement(keys, field, ballSteps)


# if players collide, they are not allowed to cross each other
def playerCollideWithPlayer(keys: pygame.key, playerRectangles: pygame.Rect):
    for playerRect in playerRectangles:
        collisionDetect = playerRect.collidelist(playerRectangles)
        if collisionDetect >= 0:
            print(f"playerRect: {playerRect}, collisionDetect{collisionDetect}")
