#
# Pygame Starter Kit
# Copyright 2014, AlveyLabs Inc
# 
# Version 
# 

import sys
import pygame
from source import game
from source.update import update
from source.draw import draw
from source.chimp import Chimp
from source.fist import Fist
from source.state.gamestate import GameState
from source.state.playstate import PlayState

def init():
    pygame.init()

    game.screen = pygame.display.set_mode(game.window_size, pygame.DOUBLEBUF)
    pygame.mouse.set_visible(False)
    
    game.punch_sound = pygame.mixer.Sound("resources/punch.wav")

    game.chimp = Chimp()
    game.fist = Fist()

    # Switch to the playing state
    game.current_state = PlayState()

def main():
    """
    Main game initilization code
    """

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
            
        game.update_context(keys, mouse)
        game.draw_context()

    return

if __name__ == "__main__":
    main()