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

## Masking

Masking is a method to create a small mask (patch of image, say 3*3 matrix as a patch) and moving that patch throughout the image to modify the whole image. It is an image enhancement technique and this is the main process underneath a lot of image processing methods including blurring, sharpening, edge detection etc.

### Blurring

Blurring is a type of masking and is used to make an image smooth in which edges are not observed. For blurring, a low pass filter is used since it allows the low frequency to allow and stop high frequency.

Go to the'blurring_masking' directory and run:
```
python3 blurring_masking.py
```

### Sharpening

Sharpening is another type of masking which is used to enhance any image such that edges are highlighted and fine details of image is seen.

Go to the'sharpening_masking' directory and run:
```
python3 sharpening_masking.py
```