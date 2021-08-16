import numpy as np
from operator import itemgetter
from PIL import Image
from numba import jit

@jit(nopython=True)
def power_law_transformation(img, gamma):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j][2] = int(100 * (img[i][j][2]/100)**gamma)
    return img

@jit(nopython=True)
def log_transformation(img, max_int):
    const = 99/(np.log(1 + max_int))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j][2] = int(const * np.log(1+img[i][j][2]))
    return img


