import pygame
from .. import score
from .. import graphics
from .. import game
from .. import fist
from ..sprite import Sprite
from gamestate import GameState

class ShopState(GameState):
    def __init__(self):
        pass

    def update(self, *args):
        """
        main function for shop screen
        """
        # change fist sprite to mouse sprite

        game.cursor.rect.x = (pygame.mouse.get_pos()[0] - game.fist.sprite.rect.width / 2)
        game.cursor.rect.y = (pygame.mouse.get_pos()[1] - game.fist.sprite.rect.height / 2)

    def draw(self):
        game.screen.fill((44, 44, 44))
        game.cursor.draw()