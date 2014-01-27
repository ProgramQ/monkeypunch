import pygame
from .. import score
from .. import graphics
from .. import game
from .. import fist
from ..sprite import Sprite
from gamestate import GameState

class ShopState(GameState):
    def __init__(self):
        
        display = [
            ["0","0","0","0","0","0","0","0"]
            ["0","0","1","0","0","0","0","0"]
            ["0","0","0","0","0","0","0","0"]
            ["0","0","0","0","0","0","0","0"]
            ["0","0","0","0","0","0","0","0"]
            ["0","0","0","0","0","0","0","0"]
            ["0","0","0","0","0","0","0","0"]
            ["0","0","0","0","0","0","0","0"]
        ]

        buttonList = []
        for y in range(0,len(display)):
            for x in range(0,len(display[y])):
                buttonList.append(Sprite("base button.png",(x*96, y*96)))   


    def update(self, *args):
        """
        main function for shop screen
        """
        # change fist sprite to mouse sprite

        game.cursor.rect.x = (pygame.mouse.get_pos()[0] - game.fist.sprite.rect.width / 2)
        game.cursor.rect.y = (pygame.mouse.get_pos()[1] - game.fist.sprite.rect.height / 2)

    def draw_hud(self):
        """
        Draw the HUD (or anything else that needs to overlay the main stuff)
        """
        
        # Background rectangle
        graphics.draw_rect((game.window_size[1], 50), (0, 0, 0), (0, 0))

        # Display the score
        graphics.draw_text("PUNCH POINT SHOP     PUNCH POINTS: " + str(score.total) , (255, 255, 255),(15, 15))        

    def draw(self):
        game.screen.fill((41, 128, 185))
        self.draw_hud()
        game.cursor.draw()
    
