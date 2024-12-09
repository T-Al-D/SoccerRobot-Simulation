import pygame

from Classes.SoccerField import SoccerField
from Constants import Const

goal_counter = 0

def checkBallPosition(ballRect: pygame.Rect, goal_counter: int):

    ballRect: pygame.Rect
    field: SoccerField

    if field.ballPositionX > 750 or field.ballPositionX < 20:
        goal_counter += 1
        print(f"Tor-Ereignis! Neuer Stand: {goal_counter}")
    return goal_counter

