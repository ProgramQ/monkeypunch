from sprite import Sprite

class Button:		# use "image" and (x,y)
	def __init__(self, image, position):
		self.image = Sprite(image,position)

	def draw(self):
		self.sprite.draw()