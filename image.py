from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

path = '.'
pathOut = './editedImgs'

if not os.path.exists(pathOut):
    os.makedirs(pathOut)


for filename in os.listdir(path):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert("RGB")  # "L"- grey
    edit2 = edit.resize((2000, 1300))
    edit3 = edit.filter(ImageFilter.EDGE_ENHANCE)
    clean_name = os.path.splitext(filename)[0]

    draw = ImageDraw.Draw(edit3)
    draw.text((10,10),"Sabrina",fill=(0, 0, 255))
    edit3.save(f"{pathOut}/{clean_name}_edited.jpg")
