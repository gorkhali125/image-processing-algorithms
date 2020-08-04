# Image Processing Algorithms

Image processing is a method to perform some operations on an image, in order to get an enhanced image or to extract some useful information from it. Various image processing algorithms are implemented in python3 from scratch. Standard images are used for the implementation.

# Requirement

1. Python3
2. Pillow

# Installation

Install PILLOW using pip3
``` 
pip3 install pillow
```

# Running Algorithms

To run the algorithms, navigate to the corresponding directory and run the file. Example:

```
python3 algorithm.py
```

# Algorithms

## Negative of Image

Negative of an image is a total inversion of original image calculated by simply subtracting each pixel value of an image from the maximum pixel value. For grayscale images, only one band calculation is necessary while for color images, three different bands "R", "G" and "B" needs to be separately negated.

Go to the 'negative_grayscale' or 'negative_color' directory and run:
```
python3 negative_grayscale.py OR python3 negative_color.py
```

## Bit Plane Slicing

Every pixel of an image has certain gray level represented in bits. For 8-bit image, 0 is represented by 00000000 and 255 by 11111111. The bit in the leftmost side is referred as the MSB (most significant bit) and the one in the rightmost side is referred as the LSB (least significant bit). MSB carries most significant part of the image while LSB has least information of the image.

Go to the 'bit_plane_slicing' directory and run:
```
python3 bit_plane_slicing.py
```

## Contrast Stretching 

Contrast Stretching also known as Normalization is a method to correct the contrast of an image by stretching the range of contrast values in that image. An image might have gray levels accumulated at some ranges between 0-255, suppose say 40-150 and thus the image doesn't have all the dynamic ranges needed to look sharp. Contrast Stretching aims to stretch those gray level to the whole range 0-255 and the image will look much better.

Go to the 'contrast_stretching' directory and run:
```
python3 contrast_stretching.py
```
To check another image, comment line 45 and uncomment line 46 of the file contrast_stretching.py