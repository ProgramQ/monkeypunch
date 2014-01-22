import pygame
import graphics
import game
from sprite import Sprite

def draw():
    """
    Drawing logic
    """

    # Fill the screen with black
    game.screen.fill((0, 0, 220)) # much more pretty
    pygame.display.set_caption("MONKEY PUNCH!")
    # pygame.display.set_mode((640,480),pygame.FULLSCREEN) uncomment at your own risk!

    # insert logic here
    game.chimp.draw()
    game.fist.draw()

    # Don't change these
    pygame.display.update()
    pygame.display.flip()

    return