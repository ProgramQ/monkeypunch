import pygame
from sprite import Sprite

# Game display
screen      = None

# Window size
window_size = (1280, 720)

# Resources path
rpath       = "resources/"

chimp = Sprite("chimp.bmp", (500, 150))
fist = Sprite("fist.bmp", (25, 25))
punch_sound = None