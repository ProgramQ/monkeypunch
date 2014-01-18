#
# Pygame Starter Kit
# Copyright 2014, AlveyLabs Inc
# 
# Version 0.2.2
# 

import sys
import pygame
from source import game
from source.update import update
from source.draw import draw

def init():
    pygame.mouse.set_visible(False)
    game.punch_sound = pygame.mixer.Sound("resources/punch.wav")
    game.punch_sound.set_volume(0.1)

def main():
    """
    Main game initilization code
    """

    pygame.init()
    game.screen = pygame.display.set_mode(game.window_size, pygame.DOUBLEBUF)
    keys = set()
    mouse = set()

    # Set up game
    init()

    # Perform game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN: keys.add(event.key)
            if event.type == pygame.KEYUP: keys.discard(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN: mouse.add(event.button)
            if event.type == pygame.MOUSEBUTTONUP: mouse.discard(event.button)

        update(keys, mouse)
        draw()

    return

if __name__ == "__main__":
    main()