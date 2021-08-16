import numpy as np
def hist_equalization(img, rows, cols):
    hist = [0] * 100
    hist_new = [0] * 100
    new_levels = [0] * 100
    for i in range(rows):
        for j in range(cols):
            hist[img[i][j][2]] += 1

    pixels = rows * cols
    current = 0
    for i in range(100):
        current += hist[i]
        new_levels[i] = int((current * 99) / pixels)

    for i in range(rows):
        for j in range(cols):
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




