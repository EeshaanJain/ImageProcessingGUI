import numpy as np
from Scripts.image_conversion import colorsys_RGB2HSV, colorsys_HSV2RGB, colorsys_getRGBA

def power_law_transformation(img, gamma):
    """
    Function to perform gamma correction vectorized
    """
    h, s, v, a = colorsys_RGB2HSV(img) # Get h, s, v, a
    v = (255 * ((v.astype(np.float32) / 255) ** gamma)).astype(np.uint8) # Perform operation with appropriate scaling
    img_arr = colorsys_HSV2RGB(h, s, v, a)
    return img_arr

def log_transformation(img):
    """
    Function to perform log transform vectorized
    """
    h, s, v, a = colorsys_RGB2HSV(img) # Get h, s, v, a
    max_int = np.max(v) # Get max intensity
    v = ((255/np.log(1+max_int)) * np.log(1 + v.astype(np.float32))).astype(np.uint8) # Perform operation with appropriate scaling
    img_arr = colorsys_HSV2RGB(h, s, v, a)
    return img_arr

def invert(img):
    """
    Function to invert colors of an image
    """
    r, g, b, a = colorsys_getRGBA(img) # Get r, g, b, a
    r, g, b = 255 - r, 255 - g, 255 - b # Invert all colors
    img_arr = np.dstack((r, g, b, a))
    return img_arr

def scale(img, min=0, max=255):
    """
    Function to scale pixel values of image to [0, 255]
    """
    extent = np.max(img) - np.min(img) # Get range
    new_img = (img - np.min(img)) / extent # subtract min and divide by range
    new_img = (new_img * (max - min) + min).astype(np.uint8) # Scale appropriately
    return new_img

def subtract_images(img1, img2):
    """
    Function to subtract 2 images and preserve scaling
    """
    new_img = img1 - img2
    new_img = scale(new_img)
    return new_img

def add_images(img1, img2):
    """
    Function to add 2 images and preserve scaling
    """
    new_img = img1 + img2
    new_img = scale(new_img)
    return new_img