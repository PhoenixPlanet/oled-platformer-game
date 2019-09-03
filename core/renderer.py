from PIL import Image, ImageDraw, ImageFont
from luma.core.render import canvas

import data
import print_func as pf
from algorithms import DesignPattern
from demo_opts import get_device

class Renderer(DesignPattern.SingletonInstance):
    def __init__(self):
        self.draw_funcs = []
        self.draw_args = []
        self.draw_colors = []
        
        # get display
        self.display = get_device()

    def init_renderer(self):
        self.draw_funcs = []
        self.draw_args = []
        self.draw_colors = []

    def add(self, func, args, _outline="white", _fill="white"):
        self.draw_funcs.append(func)
        self.draw_args.append(args)
        self.draw_colors.append(dict(outline=_outline, fill=_fill))
        
    def render(self):
        with canvas(self.display) as draw:
            for i, func in enumerate(self.draw_funcs):
                if func == "rectangle":
                    draw.rectangle(self.draw_args[i], outline=self.draw_colors[i]["outline"], fill=self.draw_colors[i]["fill"])
                elif func == "line":
                    draw.line(self.draw_args[i], fill=self.draw_colors[i]["fill"])
                    