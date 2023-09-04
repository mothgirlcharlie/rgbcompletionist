import sys
import struct
from PIL import Image
from PIL import ImageDraw

def int_to_rgb(num):
    out = ()
    return out


pic = Image.open("allcolors.png")
painter = ImageDraw.Draw(pic)
color = 0x0
for x in range(pic.size[0]):
    for y in range(pic.size[1]):
        painter.point((x,y), color)
        color += 0x1

pic.save("allcolors.png", "PNG")