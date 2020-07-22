from PIL import Image
import os

file_list = os.listdir("images")

for file in file_list:
    im = Image.open("images/" + file)
    final_image = im.rotate(90).resize((128,128)).convert("RGB").save("/opt/icons/" + file, "JPEG")
    print(file)