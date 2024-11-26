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
