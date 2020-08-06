from __future__ import division
from PIL import Image, ImageDraw
from datetime import datetime

img = Image.open("test_pattern_blurring_orig.tif")

img.show() #Show the original Image
width, height = img.size
print(width)
print(height)

def generateBlankMatrix(matrix_size, default = 0):
	bm = [None]*matrix_size
	for i in range(matrix_size):
		bm[i] = [default] * matrix_size
	return bm

matrix_size = 3 #Use odd numbers here like 3,5,7
bit_mask = generateBlankMatrix(matrix_size,1/(matrix_size*matrix_size))

def multiply_rectangles(rect1,rect2):
	theSum = 0
	for i in range(0,len(rect1)):
		for j in range(0,len(rect1)):
			theSum = theSum + rect1[i][j] * rect2[i][j]
	return theSum

def get_rectangle(img,i,j):
	rect = generateBlankMatrix(len(bit_mask))
	length = len(rect)
	mid = int((length - 1)/2)
	for k in range(-1*mid,mid+1):
		for l in range(-1*mid,mid+1):
			try:
				rect[k+mid][l+mid] = img.getpixel((i+k,j+l))
			except IndexError:
				# we just ignore and let it be 0 as there is no pixel
				pass
	return rect


tStart = datetime.now()
for i in range(0,width):
    for j in range(0,height):
        thisRectangle = get_rectangle(img,i,j)
        newPixelValue = multiply_rectangles(thisRectangle,bit_mask)
        img.putpixel((i,j), int(newPixelValue))
tEnd = datetime.now()
dif = tEnd - tStart
print("Total Time taken: {0}".format(dif.total_seconds()))
img.show()
