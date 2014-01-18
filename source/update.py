import pygame
import game
import random
import score

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
            if game.fist.rect.colliderect(game.chimp.sprite.rect):
                if random.randint(0, 10) == 1:
                    game.chimp.health -= 15
                    print("Critical hit")
                    score.total += (500 * score.multiplier) # add percent bonus in somehow
                else:
                    game.chimp.health -= 5
                    game.punch_sound.play()
                    score.total += (100 * score.multiplier) # ^ same

    return