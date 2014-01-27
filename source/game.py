import pygame
from sprite import Sprite

# Game display
screen      = None

# Window size
window_size = (768, 768)

# Resources path
rpath       = "resources/"

punch_sound = None

# State management
def switch_context(state):
    current_state = state
    current_state.load()

def update_context(*args):
    current_state.update(args[0], args[1])

def draw_context():
    current_state.draw()