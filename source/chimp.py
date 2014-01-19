from sprite import Sprite

class Chimp:
    def __init__(self):
        self.sprite = Sprite("chimp.png", (500, 150))
        self.health = 100
        self.alive = True

    def set_health(self, value):
        self.health += value
        if self.health == 0:
            print("Monkey dead")
            self.alive = False
    
    def draw(self):
        self.sprite.draw()