from PIL import Image, ImageEnhance, ImageFilter
import os

path = '.'
pathOut = './editedImgs'

if not os.path.exists(pathOut):
    os.makedirs(pathOut)


for filename in os.listdir(path):
    if not filename.lower().endswith(('.jpg', '.jpeg', 'png')):
        continue
    
    img = Image.open(f"{path}/{filename}")
    edit= img.filter(ImageFilter.SHARPEN).convert("L")
    
    clean_name= os.path.splitext(filename)[0]
    edit.save(f"{pathOut}/{clean_name}_edited.jpg")
