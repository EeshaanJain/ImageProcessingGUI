import numpy as np
from Scripts.image_conversion import colorsys_RGB2HSV, colorsys_HSV2RGB
def hist_equalization(img):
    hist_new = [0] * 256
    new_levels = [0] * 256
    h, s, v, a = colorsys_RGB2HSV(img)
    hist = np.histogram(v, bins=256)

    pixels = img.shape[0] * img.shape[1]
    current = 0
    for i in range(256):
        current += hist[i]
        new_levels[i] = int((current * 255) / pixels)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j][2] = new_levels[img[i][j][2]]
            hist_new[img[i][j][2]] += 1

    return (img.astype(np.uint8), hist, hist_new)

def hist_equalization_gray(img, rows, cols):
    hist_old = [0] * 100
    hist_new = [0] * 100
    new_levels = [0] * 100
    for i in range(rows):
        for j in range(cols):
            print(img[i][j])
            hist_old[img[i][j]] += 1

    pixels = rows * cols
    current = 0
    for i in range(100):
        current += hist_old[i]
        new_levels[i] = int((current * 99) / pixels)

    for i in range(rows):
        for j in range(cols):
            img[i][j] = new_levels[img[i][j]]
            hist_new[img[i][j]] += 1

    return (img, hist_old, hist_new)




