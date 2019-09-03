import platform

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

        self.input = IM.Keyboard()
        self.buttonState = {}

        self.size = (1, 1)

        self.x = 20
        self.y = data.groundY - self.size[1]
        self.set_center()

        self.xvel = 0
        self.yvel = 0
        self.xacc = 0
        self.yacc = 0

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

    def draw(self, outline="white", fill="white"):
        self.renderer.add("rectangle", (self.x, self.y, self.x + self.size[0], self.y + self.size[1]), \
                _outline=outline, _fill=fill)

    def update(self):
        self.xvel += self.xacc
        self.yvel += self.yacc
        
        self.move(self.xvel, self.yvel)


class SpriteUnderGravity(SpriteBase):
    def __init__(self):
        super().__init__()
    
    def check_ground(self):
        if self.y < data.groundY - self.size[1] - 1:
            self.yvel += 1
        else:
            self.yvel = 0
            self.go_to(self.x, data.groundY - self.size[1] - 1)
            self.jumpState = 0

    def update(self):
        super().update()

        self.check_ground()


class Player(SpriteUnderGravity):
    def __init__(self):
        super().__init__()
        
        self.size = data.player_size

    def update(self):
        super().update()
        
        self.get_button_input()

        # self.check_ground()
        
        if self.buttonState['jump']:
            if self.jumpState == 0:
                self.move(0, -1)
                self.yvel = data.jumpF
                self.jumpState = 1

        if self.buttonState["right"] and self.x < self.gameManager.s_width - self.size[0]:
            self.xvel = 2

        elif self.buttonState["left"] and self.x > 0:
            self.xvel = -2

        else:
            self.xvel = 0
        
        self.draw()

