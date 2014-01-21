from sprite import Sprite
import score

class Fist:
    def __init__(self):
        self.sprite = Sprite("fist.png", (25, 25))
        self.level = 1
        print("Level 1 fist created") # for debugging

    def draw(self):
        self.sprite.draw()