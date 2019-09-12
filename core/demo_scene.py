import platform
import pygame

from PIL import Image

import game_manager as GM
import sprites
from renderer import Renderer

RENDERER = Renderer.instance()

CLOCK = pygame.time.Clock()

GAME_MANAGER = GM.GameManager.instance()

def init_game():
    GAME_MANAGER.initGame()

PLAYER = sprites.Player()

LOGO_IMAGE = Image.open('../resources/logo/starwars.png')

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