from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import convolution as conv
from filters import laplacian_3x3, gaussian_filter
from image_conversion import colorsys_RGB2HSV, colorsys_HSV2RGB 

def scale(img, min=0, max=255):
    extent = np.max(img) - np.min(img)
    new_img = (img - np.min(img)) / extent
    return (new_img * (max - min) + min).astype(np.uint8)

def subtract_images(img1, img2):
    new_img = img1 - img2
    new_img = scale(new_img)
    return new_img

def add_images(img1, img2):
    new_img = img1 + img2
    new_img = scale(new_img)
    return new_img


img = Image.open('Images/um2.png').convert("RGBA")
img_arr = np.array(img, dtype='int')

filter = gaussian_filter(5)
new_img = conv.convolution_sharpen(img_arr, filter, 0.7).astype(np.uint8)
fig, ax = plt.subplots(1, 2)
ax[0].imshow(img_arr)
ax[1].imshow(new_img)
print(img_arr - new_img)
plt.show()