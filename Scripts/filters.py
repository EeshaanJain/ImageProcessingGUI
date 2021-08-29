import numpy as np

def gaussian_filter(size, sigma=None):
    """
    Function to return gaussian filter given size and sigma
    """
    if sigma is None:
        sigma = np.sqrt(size)
    kernel1 = np.linspace(-1*(size//2), size//2, size) # 1d kernel
    kernel1 /= np.sqrt(2)*sigma # divide by constant
    kernel1 = kernel1**2 # Square
    kernel2 = np.exp(-kernel1[:, None] - kernel1[None, :]) # 2d kernel as outer product
    return kernel2/kernel2.sum() # Normalize


def average_filter(size):
    kernel1 = np.ones([size, size], dtype=int) 
    return kernel1/(size*size) # [1_{ij}] kernel normalized

