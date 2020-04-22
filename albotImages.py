'''
    PIL
'''
from PIL import Image
import os, sys

img = Image.open("picture.jpg")
img.show()
path= os.path.splitext("picture.jpg")

img.save(path+".png")