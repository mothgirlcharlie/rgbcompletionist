from PIL import Image
from PIL import ImageDraw
import math
def pixeltohexvalue(px_tuple):
    out = 0
    out += px_tuple[2]
    out += px_tuple[1] * 16 ** 2
    out += px_tuple[0] * 16 ** 4
    return hex(out)

def generate_file(outset: set, file_type: str = "txt"):

    if file_type.lower() == "txt":
        converted_outset = set()
        print("Generating txt file...")
        for item in outset:
            converted_outset.add(pixeltohexvalue(item))
        delete_list = ("0x", "'", ",", "{", "}")
        with open("output.txt", "w") as outfile:
            outfile.write(str(converted_outset))
        with open("output.txt", "r") as outfile:
            data = outfile.read()
            for item in delete_list:
                data = data.replace(item, "")
        with open("output.txt", "w") as outfile:
            outfile.write(data)


    elif file_type.lower() == "png":
        print("Generating png file...")
        pic = Image.new(mode = "RGB", size = (math.isqrt(len(outset)) + 1, math.isqrt(len(outset)) + 1))
        painter = ImageDraw.Draw(pic)
        outlist = list(outset)

        i = 0
        for x in range(pic.size[0]):
            for y in range(pic.size[1]):
                if i < len(outset):
                    painter.point((x,y), outlist[i])
                    i += 1
                else:
                    break
        pic.save("output.png", "PNG")

    else:
        print("invalid file type. file will not generate.")
