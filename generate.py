from random import randrange

from PIL import Image, ImageOps, ImageDraw, ImageFont


def save(i):
    numstr = str(i + 1).zfill(4)

    img_index = randrange(26)

    background = Image.new('RGBA', (512, 512), '#81b29a')
    img = Image.open(f'./{img_index}.png')
    background.paste(img, (0, 0), img)
    img = background

    new_img = Image.new('RGBA', (512, 600), (255, 255, 255))
    new_img.paste(img, (0, 0, 512, 512), img)
    img = new_img

    font = ImageFont.truetype("bigblue.ttf", size=42)
    font2 = ImageFont.truetype("Gilroy.ttf", size=42)
    font3 = ImageFont.truetype("Gilroy.ttf", size=84)

    draw = ImageDraw.ImageDraw(img)
    draw.line((0, 512, 512, 512), fill=256)
    draw.text((10, 520), "IRENEDAO", font=font, align="left", fill="black")
    draw.text((2, 568), "TRIBE PASS", font=font2, align="left", fill="#ced4da")
    draw.text((6, 564), "TRIBE PASS", font=font2, align="left", fill="#6c757d")
    draw.text((10, 560), "TRIBE PASS", font=font2, align="left", fill="black")
    draw.text((290, 524), numstr, font=font3, align="right", fill="black")

    img = ImageOps.expand(img, border=5, fill="black")

    img.save(f'./outs/{i}.png')

for i in range(10):
    print(i)
    save(i)
