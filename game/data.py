"""
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306 as SSD

from PIL import Image, ImageDraw, ImageFont

# pin configuration
RST = 24
# followings are only used with SPI
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128X64 I2C display
display = SSD.SSD1306_128_64(rst=RST)

s_width = display.width
s_height = display.height
screen = (s_width, s_height)

# set mode '1' (1-bit color)
image = Image.new('1', screen)
# get drawing object
draw = ImageDraw.Draw(image)
"""

DEFAULT_Y = 47
DEFAULT_X = 64

playerSize = (4, 4)
gravity = 2
jumpF = -5

groundY = 50
