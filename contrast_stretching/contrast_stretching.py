from __future__ import division
from PIL import Image, ImageDraw
import math

def getPixelVals(img):
	for i in range(0,width):
		for j in range(0,height):
			thisPixel = img.getpixel((i,j))
			OrgImagevalues[thisPixel] = thisPixel
			
def contrastStretch(img):
	minVal = min(i for i in OrgImagevalues if i > 0)
	maxVal = max(OrgImagevalues)
	difference = maxVal - minVal
	
	for i in range(0,width):
			for j in range(0,height):
				thisPixel = img.getpixel((i,j))
				OrgHistogramImagevalues[thisPixel] += 1
				newPixVal = ((thisPixel - minVal)/difference) * 255
				newPixVal = int(round(newPixVal))
				convertedImagevalues[newPixVal] += 1
				img.putpixel((i,j), newPixVal)

def showHistogram(pixelValues):
	#Outline of the Rectangular Box Begins    
	h = int(math.floor(max(pixelValues) / 10) + 10)
	histogram = Image.new('L', (1285, h))
	draw = ImageDraw.Draw(histogram)
	draw.rectangle(((0,0), (1285, h)), fill=255)
	#Outline of the Rectangular Box Ends

	#Histogram Drawing begins with the value points
	x = 0
	for v in pixelValues:
		height = int(math.floor(v / 10))
		draw.rectangle(((x, 5), (x+5, height+5)), fill=0)
		x += 5		
	#Histogram Drawing ends
	
	#Co-ordinates in Image Processing are upside down. Hence image is rotated by 180 degrees
	histogram.transpose(Image.FLIP_TOP_BOTTOM).show()


img = Image.open("beans-black.tif")
#img = Image.open("einstein low contrast.tif")

img.show() #Show the original Image
width, height =  img.size
print(width)
print(height)
print(img.mode)

#Values will be used to store histogram data for the image
OrgImagevalues = [0] * 256 #Original Image values
OrgHistogramImagevalues = [0] * 256 #Original Image values
convertedImagevalues = [0] * 256 #Converted Image values

getPixelVals(img) #get the pixel values for contrast stretching

contrastStretch(img) #contrast stretch the image
img.show() #Show the converted Image

showHistogram(OrgHistogramImagevalues) #Show the histogram for original image
showHistogram(convertedImagevalues) #Show the histogram for converted image




