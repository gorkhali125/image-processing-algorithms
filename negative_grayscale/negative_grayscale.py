import math
from PIL import Image, ImageDraw

def negative_grayscale(img):
	for i in range(0,width):
		for j in range(0,height):
			thisPixel = img.getpixel((i,j))
			#If the current pixel has pixel value, increment the pixel value by 1 and set the pixel value. For Original Image
			OrgImagevalues[thisPixel] += 1
			img.putpixel((i,j), 255 - thisPixel)
			#If the current pixel has pixel value, increment the pixel value by 1 and set the pixel value. For Converted Image
			convertedImagevalues[255 - thisPixel] += 1

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


img = Image.open("lena512.bmp")
img.show('Lena Original') #Show the original Image
width, height =  img.size
print(width)
print(height)
print(img.mode)

#Values will be used to store histogram data for the image
OrgImagevalues = [0] * 256 #Original Image values
convertedImagevalues = [0] * 256 #Converted Image values

negative_grayscale(img) #convert the image to it's negative
img.show('Lena Negative') #Show the converted Image

showHistogram(OrgImagevalues) #Show the histogram for original image
showHistogram(convertedImagevalues) #Show the histogram for converted image




