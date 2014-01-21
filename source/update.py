import pygame
import game
import random
import score
import time

def update(*args):
    """
    Update game world here
    """

    # Set fist location to center around mouse location
    game.fist.rect.x = (pygame.mouse.get_pos()[0] - game.fist.rect.width / 2)
    game.fist.rect.y = (pygame.mouse.get_pos()[1] - game.fist.rect.height / 2)

    # Check for hit
    for button in args[1]:
        if button == 1:
            game.fist.rect.y -= 15 
            if game.fist.rect.colliderect(game.chimp.sprite.rect):
                if random.randint(0, 50) == 1:
                    game.chimp.set_health(-15)
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
                time.sleep(.1)
            else:
                score.multiplier = 1
    return