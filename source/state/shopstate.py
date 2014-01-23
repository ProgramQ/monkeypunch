from .. import score
from .. import graphics
from .. import game
from .. import fist
from ..sprite import Sprite
from gamestate import GameState

class shopstate(Gamestate):
	def __init__(self):
		pass

	def update(self, *args):
		"""
		main function for shop screen
		"""
        #change fist sprite to mouse sprite
        game.fist.sprite.rect.x = (pygame.mouse.get_pos()[0] - game.fist.sprite.rect.width / 2)
        game.fist.sprite.rect.y = (pygame.mouse.get_pos()[1] - game.fist.sprite.rect.height / 2)