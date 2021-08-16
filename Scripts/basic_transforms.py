import numpy as np
from PIL import Image
from scipy import ndimage

def rotate_clockwise(img):
    return ndimage.rotate(img, 90)

def rotate_anticlockwise(img):
    return ndimage.rotate(img, -90)

def rotate_arbitrary(img, deg):
    return ndimage.rotate(img, deg)

def horizontal_flip(img):
    return img[:, ::-1]

def vertical_flip(img):
    return img[::-1, :]

def diagonal_flip(img):
    return img[::-1, ::-1]