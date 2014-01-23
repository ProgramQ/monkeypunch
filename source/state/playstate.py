import pygame
import random
import time
from .. import score
from .. import graphics
from .. import game
from ..sprite import Sprite
from gamestate import GameState

class PlayState(GameState):
    def __init__(self):
        pass

    def update(self, *args):
        """
        Main update function for this screen
        """

        # Set fist location to center around mouse location
        game.fist.sprite.rect.x = (pygame.mouse.get_pos()[0] - game.fist.sprite.rect.width / 2)
        game.fist.sprite.rect.y = (pygame.mouse.get_pos()[1] - game.fist.sprite.rect.height / 2)

        # Check for hit
        for button in args[1]:
            if button == 1:
                game.fist.sprite.rect.y -= 15
                if game.fist.sprite.rect.colliderect(game.chimp.sprite.rect):
                    if random.randint(0, 50) == 1:
                        game.chimp.set_health(-15)
                        # we need a critical hit sound!
                        print("Critical hit")
                        score.total += (5 * score.multiplier) * score.upgrade_percent
                        print("Punch Points: %d" % score.total) # for debugging purposes
                        if score.multiplier < 30: # implemented better multiplier max
                            score.multiplier += 1
                        print("multiplier: %d" % score.multiplier) # more debugging purposes                   
                    else:
                        game.chimp.set_health(-5)
                        game.punch_sound.play()
                        score.total += (1 * score.multiplier) * score.upgrade_percent 
                        print("Punch Points: %d" % score.total)
                        if score.multiplier < 30:
                            score.multiplier += 1
                        print("multiplier: %d" % score.multiplier)
                    time.sleep(.2) # Prevents multiple punches per tick
                else:
                    score.multiplier = 1

    def draw_hud(self):
        """
        Draw the HUD (or anything else that needs to overlay the main stuff)
        """
        
        graphics.draw_text("Score: " + str(score.total), (255, 255, 255), (15, 15))

    def draw(self):
        """
        Main drawing function for this screen
        """

        game.screen.fill((41, 128, 185)) # this is _much_ more pretty

        # insert logic here
        game.chimp.draw()
        game.fist.draw()

        # Don't change these
        self.draw_hud()
        pygame.display.update()
        pygame.display.flip()

    def load(self):
        pygame.display.set_caption("MONKEY PUNCH!")