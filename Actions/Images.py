"""!
@file 
@brief all methods related to images
"""

import pygame


def loadAndScaleImage(filePath: str, width: int, height: int) -> pygame.image:
    """!
    @brief load an image from a path and scale it depending on width and height
    this function has try-except to asses, if the image was loaded correctly

    @param filePath the string-path to the resource (in resources)
    @param width The 'width' of the future rectangle
    @param field The 'height' of the future rectangle

    @return pygame.image object
    """
    try:
        image = pygame.image.load(filePath)
        if image == None:
            print(f"Failed to load image: {filePath}")
        else:
            scaledImage = pygame.transform.scale(image, (width, height))
        return scaledImage
    except pygame.error as e:
        print(f"Error loading image: {e}")
        return None
