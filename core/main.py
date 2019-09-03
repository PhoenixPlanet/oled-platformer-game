"""
Main python file of game
"""
import time
import pygame

import platform

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from luma.core.render import canvas

# import data
import print_func as pf
import game_manager as GM

import sprites


CLOCK = pygame.time.Clock()

# set font
FONT_CAVIAR_DREAM = ImageFont.truetype("../resources/fonts/CaviarDreams.ttf", 15)

GAME_MANAGER = GM.GameManager.instance()

def init_game():
    GAME_MANAGER.initGame()

PLAYER = sprites.Player()

LOGO_IMAGE = Image.open('../resources/logo/PlaneteLogo.ppm').convert('1')
LOGO_IMAGE.resize((128, 64))

def main():
    while True:
        if platform.system() == 'Windows':
            CLOCK.tick_busy_loop(30)

        GAME_MANAGER.init_canvas()

        GAME_MANAGER.levelRender()
        PLAYER.update()

        GAME_MANAGER.render()

if __name__ == "__main__":
    # init_display()
    init_game()
    main()
