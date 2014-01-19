import pygame
from sprite import Sprite

# Game display
screen      = None

# Window size
window_size = (1280, 720)

# Resources path
rpath       = "resources/"

fist = Sprite("fist.png", (25, 25))
punch_sound = None