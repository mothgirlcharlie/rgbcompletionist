from PIL import Image

def pixeltohexvalue(pixtuple):
    out = 0
    out += pixtuple[2]
    out += pixtuple[1] * 16**2
    out += pixtuple[0] * 16**4
    return hex(out)

def generate_file():
    delete_list = ("0x", "'", ",", "{", "}")
    with open("output.txt", "w") as outfile:
        outfile.write(str(outset))
    with open("output.txt", "r") as outfile:
        data = outfile.read()
        for item in delete_list:
            data = data.replace(item, "")
    with open("output.txt", "w") as outfile:
        outfile.write(data)

if __name__ == '__main__':
    genfile = False

    getinput = input("Generate file? Y/N\n")
    if(getinput.lower == "y"):
        genfile = True

    imagename = input("Image file name: ")

    outset = set()
    pic = Image.open(imagename)

    for xpixel in range(pic.size[0]):
        for ypixel in range(pic.size[1]):
            outset.add(pixeltohexvalue( pic.getpixel( (xpixel,ypixel) )))
    if(genfile):
        generate_file()

    print(f"image size: {pic.size[0]}x{pic.size[1]} ({pic.size[0] * pic.size[1]:,d} total pixels.)")
    print(f"{len(outset):,d} / {255**3:,d} rgb values")