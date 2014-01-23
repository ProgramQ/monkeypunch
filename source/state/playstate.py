import pygame
import random
import time
import sys
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
                    time.sleep(.1) # Prevents multiple punches per tick
                else:
                    score.multiplier = 1

        for key in args[0]:
            if key == pygame.K_ESCAPE: sys.exit()

    def draw_hud(self):
        """
        Draw the HUD (or anything else that needs to overlay the main stuff)
        """
        
        # Background rectangle
        graphics.draw_rect((game.window_size[1], 50), (0, 0, 0), (0, 0))

        # Display the score
        graphics.draw_text("Score: " + str(score.total) + "  Multiplier: x " + str(score.multiplier) + "  Monkeys Murdered: " + str(score.monkey_deaths), 
                          (255, 255, 255), 
                          (15, 15))

        # Draw this dude on top of everything
        game.fist.draw()

    def draw(self):
        """
        Main drawing function for this screen
        """

        game.screen.fill((41, 128, 185)) # this is _much_ more pretty

        # insert logic here
        game.chimp.draw()

        # Don't change these
        self.draw_hud()
        pygame.display.update()
        pygame.display.flip()

    def load(self):
        pygame.display.set_caption("MONKEY PUNCH!")