from PIL import Image
import numpy as np
from transforms import log_transformation, power_law_transformation
from image_conversion import RGBtoHSL, HSLtoRGB, to_grayscale
import matplotlib.pyplot as plt
from hist_eq import hist_equalization

def _get_HSL(img, get_max_intensity=False):
    new_img = np.zeros(img.shape, dtype='int')
    if get_max_intensity:
        max_int = 0
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                new_img[i][j] = RGBtoHSL(*img[i][j])
                max_int = max(max_int, new_img[i][j][2])

        return (new_img, max_int)
    else:
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                new_img[i][j] = RGBtoHSL(*img[i][j])

        return new_img

def _get_RGB(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = HSLtoRGB(*img[i][j])

    return img

img = Image.open('Scripts/Sample.jpg')
img_arr = np.array(img, dtype='int')
new_img = to_grayscale(img_arr)
plt.imshow(new_img)
plt.show()


