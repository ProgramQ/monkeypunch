#
# Pygame Starter Kit
# Copyright 2014, AlveyLabs Inc
# 
# Version 666
# 

import sys
import pygame
from source import game
from source.update import update
from source.draw import draw
from source.chimp import Chimp
from source.fist import Fist
from source.sprite import Sprite
from source.state.gamestate import GameState
from source.state.playstate import PlayState

def init():
    pygame.init()

    game.screen = pygame.display.set_mode(game.window_size, pygame.DOUBLEBUF)
    pygame.mouse.set_visible(False)
    
    game.punch_sound = pygame.mixer.Sound("resources/punch.wav")
    game.chimp = Chimp()
    game.fist = Fist()
    game.cursor = Sprite("cursor.png", (50, 50))

    game.main_font = pygame.font.Font("resources/main_font.ttf", 18)

    pygame.mixer.music.load("resources/theme.ogg")
    pygame.mixer.music.play()

    # Switch to the playing state
    game.current_state = PlayState()

def main():
    """
    Main game initilization code
    """

    keys = set()
    mouse = set()
    old_mouse = set()

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
        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()