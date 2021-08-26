import numpy as np
from operator import itemgetter
from PIL import Image
from Scripts.image_conversion import colorsys_RGB2HSV, colorsys_HSV2RGB

def power_law_transformation(img, gamma):
    h, s, v, a = colorsys_RGB2HSV(img)
    v = (255 * ((v.astype(np.float32) / 255) ** gamma)).astype(np.uint8)
    img_arr = colorsys_HSV2RGB(h, s, v, a)
    return img_arr


def log_transformation(img):
    h, s, v, a = colorsys_RGB2HSV(img)
    max_int = np.max(v)
    v = ((255/np.log(1+max_int)) * np.log(1 + v.astype(np.float32))).astype(np.uint8)
    img_arr = colorsys_HSV2RGB(h, s, v, a)
    return img_arr
