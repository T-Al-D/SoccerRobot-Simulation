"""!
@file 
@brief all methods related to images
"""

import pygame


def loadAndScaleImage(filePath: str, width: int, height: int) -> pygame.image:
    """!
    @brief load an image from a path and scale it depending on width and height

    @param filePath the string-path to the resource (in resources)
    @param width The 'width' of the future rectangle
    @param field The 'height' of the future rectangle

    @return pygame.image object
    """
    image = pygame.image.load(filePath)
    scaledImage = pygame.transform.scale(image, (width, height))
    return scaledImage
