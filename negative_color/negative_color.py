import math
from PIL import Image, ImageDraw

def negative_color(img):
	for i in range(0,width):
		for j in range(0,height):
			thisPixel = img.getpixel((i,j))
			#If the current pixel has pixel value, increment the pixel value by 1 and set the pixel value. For Original Image
			OrgImagevalues[0][thisPixel[0]] += 1
			OrgImagevalues[1][thisPixel[1]] += 1
			OrgImagevalues[2][thisPixel[2]] += 1
			img.putpixel((i,j), (255 - thisPixel[0],255 - thisPixel[1],255 - thisPixel[2]))
			#If the current pixel has pixel value, increment the pixel value by 1 and set the pixel value. For Converted Image
			convertedImagevalues[0][255 - thisPixel[0]] += 1
			convertedImagevalues[1][255 - thisPixel[1]] += 1
			convertedImagevalues[2][255 - thisPixel[2]] += 1

def showHistogram(pixelValues):
	#Outline of the Rectangular Box Begins    
	hR = int(math.floor(max(pixelValues[0]) / 10) + 10)
	hG = int(math.floor(max(pixelValues[1]) / 10) + 10)
	hB = int(math.floor(max(pixelValues[2]) / 10) + 10)
	histogram = Image.new('RGB', (1285, hR+hG+hB))
	draw = ImageDraw.Draw(histogram)
	draw.rectangle(((0,0), (1285, hR)), fill=(255,255,255))
	draw.rectangle(((0,hR), (1285, hR+hG)), fill=(255,255,255))
	draw.rectangle(((0,hR+hG), (1285, hR+hG+hB)), fill=(255,255,255))
	#Outline of the Rectangular Box Ends

	#Histogram Drawing begins with the value points
	x = 0
	for v in pixelValues[0]:
		height = int(math.floor(v / 10))
		draw.rectangle(((x, 5), (x+5, height+5)), fill=(255,0,0))
		x += 5		
	x = 0
	for v in pixelValues[1]:
		height = int(math.floor(v / 10))
		draw.rectangle(((x, hR + 5), (x+5, hR + height+5)), fill=(0,255,0))
		x += 5		
	x = 0
	for v in pixelValues[2]:
		height = int(math.floor(v / 10))
		draw.rectangle(((x, hR + hG + 5), (x+5, hR + hG + height+5)), fill=(0,0,255))
		x += 5		
	#Histogram Drawing ends
	
	#Co-ordinates in Image Processing are upside down. Hence image is rotated by 180 degrees
	histogram.transpose(Image.FLIP_TOP_BOTTOM).show()


img = Image.open("lena512color.tiff")
img.show() #Show the original Image
width, height =  img.size
print(width)
print(height)
print(img.mode)

#Values will be used to store histogram data for the image
OrgImagevalues = [[0] * 256, [0] * 256, [0] * 256] #Original Image values
convertedImagevalues = [[0] * 256,[0] * 256,[0] * 256] #Converted Image values

negative_color(img) #convert the image to it's negative
img.show() #Show the converted Image

showHistogram(OrgImagevalues) #Show the histogram for original image
showHistogram(convertedImagevalues) #Show the histogram for converted image




