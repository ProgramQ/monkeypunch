from sprite import Sprite

class Chimp:
    def __init__(self):
        self.sprite = Sprite("chimp.bmp", (500, 150))
        self.health = 100
    
    def draw(self):
        self.sprite.draw()