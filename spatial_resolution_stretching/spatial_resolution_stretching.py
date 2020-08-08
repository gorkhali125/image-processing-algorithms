from __future__ import division
from PIL import Image, ImageDraw

img = Image.open("rose1024.tif")

img.show() #Show the original Image
width, height =  img.size
print(width)
print(height)


def decrease_by(image,ratio):
	image_new = Image.new(image.mode,(int(image.width/ratio),int(image.height/ratio)))
	for i in range(0,image_new.width):
		for j in range(0,image_new.height):
			image_new.putpixel((i,j),image.getpixel((i*ratio,j*ratio)))
	return image_new


def increase_by(image,ratio):
	image_new = Image.new(image.mode,(int(image.width*ratio),int(image.height*ratio)))
	for i in range(0,image_new.width):
		for j in range(0,image_new.height):
			image_new.putpixel((i,j),image.getpixel((int(i/ratio),int(j/ratio))))
	return image_new

img256 = decrease_by(img,4)
img256.show()

image1024 = increase_by(img256,4)
image1024.show()
