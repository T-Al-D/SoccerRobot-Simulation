"""!
@file
@brief all the logic that is needed during a Pause in the Game
"""

import pygame

from Actions.Drawing import drawPausePopUp
from Constants.Const import TOP_MARGIN

def pauseGame(running: bool, screen: pygame.Surface, surface: pygame.Surface) -> bool:
    """!
    @brief pause the game temporary

    @param running bool from main.py wether to stop the programm or not

    @return runnig bool
    """
    pause = True
    while pause:
        drawPausePopUp(surface)
        for event in pygame.event.get():
            # break the pause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pause = False

            # quit the game if needed
            if event.type == pygame.QUIT:
                pause = False
                running = False

        # draw pop up on surface
        drawPausePopUp(surface)

        screen.blit(surface, (0, TOP_MARGIN))

        pygame.display.update()
        # wait a bit to make popup visible
        pygame.time.delay(50)
        
    return running
