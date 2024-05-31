# import os 
from wand.image import Image
path = r"C:\Users\iniad\python\cs_exercise"

# os.makedirs(path + "\converted")
with Image(filename = path + "\practice-6-3-4-image\00-apple.png") as img:
    img.rotate(90)
    img.save(filename = path + "\converted\00-apple.png")