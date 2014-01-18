import pygame
import game

def update(*args):
    """
    Update game world here
    """

    game.fist.rect.x = (pygame.mouse.get_pos()[0] - game.fist.rect.width / 2)
    game.fist.rect.y = (pygame.mouse.get_pos()[1] - game.fist.rect.height / 2)

    for button in args[1]:
        if button == 1:
            if game.fist.rect.colliderect(game.chimp.rect):
                game.punch_sound.play()

    return