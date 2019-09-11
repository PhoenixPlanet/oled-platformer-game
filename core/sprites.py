import platform

from PIL import Image

import game_manager
from renderer import Renderer
import data

if platform.system() == 'Windows':
    import input_manager_win as IM
elif platform.system() == 'Linux':
    import input_manager_linux as IM

class SpriteBase:
    def __init__(self):
        self.gameManager = game_manager.GameManager.instance()
        self.renderer = Renderer.instance()

        self.input = IM.Keyboard(1)
        self.buttonState = {}

        self.size = (1, 1)

        self.x = 0
        self.y = data.groundY - self.size[1]
        self.set_center()

        self.vel = dict(x=0, y=0)
        self.acc = dict(x=0, y=0)

        self.jumpState = 0

    def move(self, dx, dy=0):
        self.x += dx
        self.y += dy
        self.set_center()

    def go_to(self, x, y):
        self.x = x
        self.y = y
        
    def set_center(self):
        self.centerx = self.x + self.size[0] / 2
        self.centery = self.y + self.size[1] / 2

    def get_button_input(self):
        self.buttonState = self.input.get_button_state()

    def draw(self, kind, args, outline="white", fill="white"):
        self.renderer.add(kind, args, _outline=outline, _fill=fill)

    def update(self):
        self.vel["x"] += self.acc["x"]
        self.vel["y"] += self.acc["y"]
        
        self.move(self.vel["x"], self.vel["y"])


class SpriteUnderGravity(SpriteBase):
    def __init__(self):
        super().__init__()
    
    def check_ground(self):
        if self.y < data.groundY - self.size[1] - 1:
            self.vel["y"] += 1
        else:
            self.vel["y"] = 0
            self.go_to(self.x, data.groundY - self.size[1] - 1)
            self.jumpState = 0

    def update(self):
        super().update()

        self.check_ground()


class Player(SpriteUnderGravity):
    def __init__(self):
        super().__init__()
        
        self.size = data.player_size

        self.LOGO_IMAGE = Image.open('../resources/logo/PlaneteLogo.png')
        self.LOGO_IMAGE = self.LOGO_IMAGE.resize(self.size)

    def update(self):
        super().update()
        
        self.get_button_input()

        # self.check_ground()
        
        if self.buttonState['jump']:
            if self.jumpState == 0:
                self.move(0, -1)
                self.vel["y"] = data.jumpF
                self.jumpState = 1

        if self.buttonState["right"] and self.x < self.gameManager.s_width - self.size[0]:
            self.vel["x"] = 2

        elif self.buttonState["left"] and self.x > 0:
            self.vel["x"] = -2

        else:
            self.vel["x"] = 0
        
        self.draw("bitmap", ((self.x, self.y), self.LOGO_IMAGE), fill="white")

