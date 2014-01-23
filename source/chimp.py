from sprite import Sprite
import graphics
import score

class Chimp:
    def __init__(self):
        self.sprite = Sprite("chimp.png", (350, 350))
        self.health = 100
        self.alive = True

    def set_health(self, value):
        self.health += value
        if self.health <= 0:
            print("Monkey dead") 
            score.total += 100
            score.monkey_deaths += 1
            self.alive = False
    
    def draw(self):
        self.sprite.draw()