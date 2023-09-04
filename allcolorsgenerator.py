import sys
import struct
from PIL import Image
from PIL import ImageDraw

def int_to_rgb(num):
    out = [0,0,0]
    out[0] = num // 0x10000
    out[1] = (num - (num // 0x10000) * 0x10000) // 0x100
    out[2] = num - (out[0] * 0x10000) - (out[1] * 0x100)
    print(hex(num), out)
    return tuple(out)

with Image.new("RGB", (4096,4096)) as pic:
    painter = ImageDraw.Draw(pic)
    color = 0x0
    px = pic.load()
    print(type(px))

    for x in range(pic.size[0]):
        for y in range(pic.size[1]):
            pic.putpixel((x,y), int_to_rgb(color))
            color += 0x1



pic.save("allcolors.png", "PNG")