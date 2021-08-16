# To convert RGB to HSL and vice-versa 
from numba import jit
import numpy as np

@jit(nopython=True)
def RGBtoHSL(r, g, b):
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
    lightness = abs(int(lightness*100))
    
    return hue, saturation, lightness

@jit(nopython=True)
def HSLtoRGB(h, s, l):
    s, l = s/100, l/100
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

@jit(nopython=True)
def to_grayscale(img):
    new_img = np.zeros(img.shape, dtype='int')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r, g, b = img[i][j]
            gray = 0.299*r + 0.587*g + 0.114*b
            new_img[i][j][0], new_img[i][j][1], new_img[i][j][2] = gray, gray, gray


    return new_img




