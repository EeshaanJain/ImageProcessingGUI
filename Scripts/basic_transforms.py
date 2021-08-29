

from scipy import ndimage

def rotate_clockwise(img):
    """ 
    Function to rotate image clockwise
    """
    return ndimage.rotate(img, -90)

def rotate_anticlockwise(img):
    """ 
    Function to rotate image anticlockwise
    """
    return ndimage.rotate(img, 90)

def rotate_arbitrary(img, deg):
    """ 
    Function to rotate image arbitrarily
    """
    return ndimage.rotate(img, deg)

def horizontal_flip(img):
    """ 
    Function to flip image horizontally
    """
    return img[:, ::-1]

def vertical_flip(img):
    """ 
    Function to flip image vertically
    """
    return img[::-1, :]

def diagonal_flip(img):
    """ 
    Function to flip image diagonally
    """
    return img[::-1, ::-1]