from PIL import Image, ImageDraw, ImageFont
from luma.core.render import canvas

import data
import print_func as pf
from algorithms import DesignPattern
from demo_opts import get_device

from renderer import Renderer


class GameManager(DesignPattern.SingletonInstance):
    def __init__(self):

        # pin configuration (for raspberry pi i2c)
        self.RST = 24

        self.renderer = Renderer.instance()

        self.display = self.renderer.display
        
        self.s_width = self.display.width
        self.s_height = self.display.height
        self.screen = (self.s_width, self.s_height)
        
        # get drawing object
        self.draw_func = []
        self.draw_args = []
        
        # game data
        self.nemo_pos = [data.DEFAULT_X, data.DEFAULT_Y]

        self.player_size = data.player_size
        self.playerYVel = 0

        self.gravity = data.gravity

        self.score = 0
        self.level = 1

        self.print_manager = pf.PrintManager(self) 

    def gameover(self):
        self.print_manager.print_text("Game Over!", 20, align=2, font="./fonts/KenneyMiniSquare.ttf", start_y=-2)
        self.print_manager.print_text("Press 'R' to Restart", 10, align=2, \
                font="./fonts/KenneyMiniSquare.ttf")
        self.print_manager.print_text("Score: "+str(self.score), 16, align=2, \
                font="./fonts/KenneyMiniSquare.ttf")

    def initGame(self):
        self.score = 0
        self.level = 0
        
        self.nemo_pos = [data.DEFAULT_X, data.DEFAULT_Y]

        self.player_size = data.player_size
        self.playerYVel = 0

        self.gravity = data.gravity
        
        self.jumpState = 0

    def levelRender(self):
        self.renderer.add("line", ([(0, data.groundY), (self.s_width, data.groundY)]), _fill="white")

    def playerRender(self):
        self.renderer.add("rectangle", (self.nemo_pos[0]-data.player_size[0]/2, self.nemo_pos[1]-data.player_size[1]/2, \
                    self.nemo_pos[0]+data.player_size[0]/2, self.nemo_pos[1]+data.player_size[1]/2), _outline="white", _fill="white")
    
    def init_canvas(self):
        self.renderer.init_renderer()

    def render(self):
        self.renderer.render()

    def clear(self):
        self.display.clear()