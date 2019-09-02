"""
Main python file of game
"""

import platform

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# import data
import print_func as pf
import game_manager as GM

import sprites

if platform.system() == 'Windows':
    import input_manager_win as IM
elif platform.system() == 'Linux':
    import input_manager_linux as IM


# set font
FONT_CAVIAR_DREAM = ImageFont.truetype("../resources/fonts/CaviarDreams.ttf", 15)

currentTextY = 0

GAME_MANAGER = GM.GameManager.instance()
# printManager = pf.PrintManager(gameManager)
display = GAME_MANAGER.display
#draw = GAME_MANAGER.draw

# keyboard = IM.Keyboard()
button = IM.Keyboard()


# initialize display
"""
def init_display():
    display.begin()
    display.clear()

    display.image(game_manager.image)
"""

def init_game():
    GAME_MANAGER.initGame()

#PLAYER = Sprites.Player()

LOGO_IMAGE = Image.open('../resources/logo/PlaneteLogo.ppm').convert('1')
LOGO_IMAGE.resize((128, 64))

def main():
    # draw.text((2, 2), "Hello, Wolrd!", font=font_caviar_dream, fill=255)
    # display.clear()
    while True:
        with 

        GAME_MANAGER.levelRender()
        
        GAME_MANAGER.playerRender()
        
        button_state = button.get_button_state()
        
        #PLAYER.update()

        #display.image(game_manager.image)
        # display.image(logo_image)
        
        # display.display()


if __name__ == "__main__":
    # init_display()
    init_game()
    main()
