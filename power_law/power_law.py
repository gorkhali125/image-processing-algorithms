from __future__ import division
from PIL import Image

img = Image.open("fractured_spine.tif") #use gamma = 0.1, 0.2, 0.3, 0.4, 0.5,..
gamma = 0.4

# img = Image.open("washed_out_aerial_image.tif")  # use gamma = 2,3,4,5,..
# gamma = 2

img.show()  # Show the original Image
width, height = img.size
print(width)
print(height)
print(img.mode)

for i in range(0, img.width):
    for j in range(0, img.height):
        thisPixel = img.getpixel((i, j))
        normalized_ratio = thisPixel/255
        img_applied = normalized_ratio**gamma
        changedPixel = int(img_applied*255)
        img.putpixel((i, j), changedPixel)

img.show()
