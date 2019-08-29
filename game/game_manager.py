from PIL import Image, ImageDraw, ImageFont

import data
import printFunctions as pf
from algorithms import DesignPattern


class GameManager(DesignPattern.SingletonInstance):
    def __init__(self):

        # pin configuration
        self.RST = 24
        
        # 12864 I2C display
        self.display = SSD.SSD1306_128_64(rst=self.RST)
        
        self.s_width = self.display.width
        self.s_height = self.display.height
        self.screen = (self.s_width, self.s_height)
        
        # set mode '1' (1-bit color)
        self.image = Image.new('1', self.screen)
        # get drawing object
        self.draw = ImageDraw.Draw(self.image)
        
        # game data
        self.nemoX = data.DEFAULT_X
        self.nemoY = data.DEFAULT_Y

        self.playerSize = data.playerSize
        self.playerYVel = 0

        self.gravity = data.gravity

        self.score = 0
        self.level = 1

        self.printManager = pf.PrintManager(self) 

    def gameover(self):
        self.printManager.printText("Game Over!", 20, align=2, font="./fonts/KenneyMiniSquare.ttf", startY=-2)
        self.printManager.printText("Press 'R' to Restart", 10, align=2, \
                font="./fonts/KenneyMiniSquare.ttf")
        self.printManager.printText("Score: "+str(self.score), 16, align=2, \
                font="./fonts/KenneyMiniSquare.ttf")

    def initGame(self):
        self.score = 0
        self.level = 0
        
        self.nemoX = data.DEFAULT_X
        self.nemoY = data.DEFAULT_Y

        self.playerSize = data.playerSize
        self.playerYVel = 0

        self.gravity = data.gravity
        
        self.jumpState = 0

    def levelRender(self):
        self.draw.line([(0, data.groundY), (self.s_width, data.groundY)], width=1, fill=255)
        
    def playerRender(self):
        self.draw.rectangle((self.nemoX-data.playerSize[0]/2, self.nemoY-data.playerSize[1]/2, \
                self.nemoX+data.playerSize[0]/2, self.nemoY+data.playerSize[1]/2), outline=255, fill=255)

    def clear(self):
        self.draw.rectangle((0, 0, self.s_width, self.s_height), outline=0, fill=0)
    


