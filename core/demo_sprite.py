import PIL

import sprites

class DemoPlayer(sprites.SpriteUnderGravity):
    def __init__(self):
        super().__init__()

        self.size = 