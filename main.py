from PIL import Image
import output


if __name__ == '__main__':


    imagename = input("Image file name: ")

    outset = set()
    pic = Image.open(imagename)
    print("Loading image...")
    for xpixel in range(pic.size[0]):
        for ypixel in range(pic.size[1]):
            outset.add(pic.getpixel((xpixel, ypixel)))
    print("Image loaded.")

    output.generate_file(outset, input("File type: \ntxt/png\n"))

    print(f"image size: {pic.size[0]}x{pic.size[1]} ({pic.size[0] * pic.size[1]:,d} total pixels.)")
    print(f"{len(outset):,d} / {256**3:,d} rgb values ({round((len(outset) / 256**3) * 100, 2)}% completion)")