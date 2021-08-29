"""
Convolution operations
"""

import numpy as np
from Scripts.image_conversion import colorsys_getRGBA, colorsys_RGB2HSV, colorsys_HSV2RGB
from Scripts.transforms import add_images, subtract_images
from Scripts.filters import gaussian_filter


def convolute_layer(layer, filter, rows, cols, frows, fcols):
    """
    Function to perform convolution on the v layer
    """
    output = np.zeros(layer.shape)
    padding_y = (fcols - 1) // 2 # Padding needed in y direction
    padding_x = (frows - 1) // 2 # Padding needed in x direction
    padded_img = np.zeros((rows + 2*padding_y, cols + 2*padding_x)) # Dimensions of padded image
    padded_img[padding_y:padded_img.shape[0]-padding_y, padding_x:padded_img.shape[1]-padding_x] = layer # Make center of padded image same as original

    for i in range(rows):
        for j in range(cols):
            output[i, j] = np.sum(filter * padded_img[i:i+frows, j:j+fcols]) # Perform element wise multiplication with filter to get resultant image

    return output


def convolution_rgb(img, filter):
    """
    Function to perform convolution in RGB domain (not used anywhere)
    """
    rows, cols = img.shape[0], img.shape[1] # Shape of image
    frows, fcols = filter.shape[0], filter.shape[1] # Shape of kernel
    r, g, b, a = colorsys_getRGBA(img) # Get r,g,b,a
    # Perform convolutions
    output_r = convolute_layer(r, filter, rows, cols, frows, fcols)
    output_g = convolute_layer(g, filter, rows, cols, frows, fcols)
    output_b = convolute_layer(b, filter, rows, cols, frows, fcols)
    # Stack layers back together
    img_arr = np.dstack((output_r, output_g, output_b, a))
    return img_arr
        

def convolution_hsv(img, filter):
    """
    Function to perform convolution in HSV domain on V layer
    """
    rows, cols = img.shape[0], img.shape[1]
    frows, fcols = filter.shape[0], filter.shape[1]
    h, s, v, a = colorsys_RGB2HSV(img) # Get h, s, v, a
    v = convolute_layer(v, filter, rows, cols, frows, fcols) # Convolve
    new_img = colorsys_HSV2RGB(h, s, v, a) # Get RGBA image back
    return new_img

def convolution_sharpen(img, alpha=0.5):
    """
    Function to perform convolution for sharpening
    """
    rows, cols = img.shape[0], img.shape[1]
    filter = gaussian_filter(5) # Get gaussian filter of size = 5 and sigma = sqrt(5)
    frows, fcols = filter.shape[0], filter.shape[1]
    h, s, v, a = colorsys_RGB2HSV(img) # Get h, s, v, a
    v_smooth = convolute_layer(v, filter, rows, cols, frows, fcols) # Convolve
    v_mask = subtract_images(v, v_smooth) # Subtract smooth image from original
    v_new = add_images(v, alpha*v_mask) # Add alpha*masked_image to original
    new_img = colorsys_HSV2RGB(h, s, v_new, a) # get RGBA image back
    return new_img    

                