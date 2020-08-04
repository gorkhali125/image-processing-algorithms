from PIL import Image, ImageDraw

img = Image.open("100-dollars.tif")

img.show() #Show the original Image
width, height =  img.size
print(width)
print(height)

bit_mask = [128,64,32,16,8,4,2,1]
bit = [0] * 8
for i in range(0,8):
    bit[i] = Image.new(img.mode,img.size)

for i in range(0,width):
    for j in range(0,height):
        thisPixel = img.getpixel((i,j))
        for k in range(0,8):
            thisBit = (thisPixel&bit_mask[k])
            if thisBit>0:
                thisBit = 255
            else:
                thisBit = 0
            bit[k].putpixel((i,j),thisBit)


for i in range(0,8):
    bit[i].show()
