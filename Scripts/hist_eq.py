import numpy as np
from Scripts.image_conversion import colorsys_RGB2HSV, colorsys_HSV2RGB
def hist_equalization(img):
    """
    Perform Histogram Equalization
    """
    h, s, v, a = colorsys_RGB2HSV(img)
    hist = np.histogram(v, 256, [0,256])[0] # Get original histogram

    dist = np.cumsum(hist) # Get cdf
    dist_mean = np.ma.masked_equal(dist, 0) # Mask all 0 values
    dist_mean = (dist_mean - np.min(dist_mean)) * 255/(np.max(dist_mean) - np.min(dist_mean)) # Scale
    dist_final = np.ma.filled(dist_mean, 0).astype(np.uint8) # Fill all 0 values
    v_new = dist_final[v] # Replace intensities with new levels
    hist_new = np.histogram(v_new, 256, [0, 256])[0] # Get new histogram
    img = colorsys_HSV2RGB(h, s, v_new, a)
    return img, hist, hist_new





