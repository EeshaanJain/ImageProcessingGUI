# To convert RGB to HSL and vice-versa 
from numba import jit
import numpy as np
import colorsys

@jit(nopython=True)
def RGBtoHSL(r, g, b):
    """ 
    Function manually written to convert RGB to HSL (not used anywhere)
    """
    r, g, b = r / 255, g / 255, b / 255
    min_channel = min(r, g, b)
    max_channel = max(r, g, b)
    delta = max_channel - min_channel
    hue, saturation, lightness = 0, 0, 0

    # Calculating hue
    if delta == 0:
        hue = 0
    elif max_channel == r:
        hue = ((g - b) / delta) % 6
    elif max_channel == g:
        hue = (b - r) / delta + 2
    else:
        hue = (r-g) / delta + 4

    hue = int(hue * 60)
    if hue < 0:
        hue += 360

    # Calculating lightness
    lightness = (max_channel + min_channel) / 2

    # Calculating saturation
    if delta == 0:
        saturation = 0
    else:
        saturation = delta/(1 - abs(2*lightness - 1))
    
    saturation = abs(int(saturation*100))
    lightness = abs(int(lightness*256))
    
    return hue, saturation, lightness

@jit(nopython=True)
def HSLtoRGB(h, s, l):
    """ 
    Function manually written to convert HSL to RGB (not used anywhere)
    """
    s, l = s/100, l/255
    c = (1-abs(2*l - 1)) * s
    x = c * (1-abs((h/60) % 2 - 1))
    m = l - c/2
    red, green, blue = 0, 0, 0
    if 0 <= h < 60:
        red, green, blue = c, x, 0
    elif 60 <= h < 120:
        red, green, blue = x, c, 0
    elif 120 <= h < 180:
        red, green, blue = 0, c, x
    elif 180 <= h < 240:
        red, green, blue = 0, x, c
    elif 240 <= h < 300:
        red, green, blue = x, 0, c
    elif 300 <= h < 360:
        red, green, blue = c, 0, x

    red = int((red + m) * 255)
    blue = int((blue + m) * 255)
    green = int((green + m) * 255)
    return red, green, blue

def colorsys_RGB2HSV(img_arr):
    """
    Function to convert RGBA to HSV
    """
    rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv) # Vectorize the function for efficiency
    r, g, b, a = np.rollaxis(img_arr, axis=-1) # Get r, g, b, a 
    h, s, v = rgb_to_hsv(r, g, b) # Convert rgb to hsv
    return h, s, v, a # Return h, s, v, a


def colorsys_HSV2RGB(h, s, v, a):
    """
    Function to convert HSV to RGBA
    """
    hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb) # Vectorize the function for efficiency
    r, g, b = hsv_to_rgb(h, s, v) # Convert hsv to rgb
    img_arr = np.dstack((r, g, b, a)) # Stack
    return img_arr

def colorsys_getRGBA(img_arr):
    """
    Function to return r, g, b, a layers from RGBA image
    """
    r, g, b, a = np.rollaxis(img_arr, axis=-1)
    return r, g, b, a

def to_grayscale(img):
    """
    Function to convert RGBA image to grayscale
    """
    r, g, b, a = colorsys_getRGBA(img)
    gray = 0.299*r + 0.587*g + 0.114*b # NTSC convention
    new_img = np.dstack((gray, gray, gray, a))
    return new_img