# image_similarity_exercise.py
# STUDENT'S EXERCISE FILE

"""
Exercise:
Implement a function `compare_images(i1, i2)` that receives two grayscale images
represented as NumPy arrays (2D arrays of shape (H, W)) and returns a dictionary with the following metrics:

1. Mean Squared Error (MSE)
2. Peak Signal-to-Noise Ratio (PSNR)
3. Structural Similarity Index (SSIM) - simplified version without using external libraries
4. Normalized Pearson Correlation Coefficient (NPCC)

You must implement these functions yourself using only NumPy (no OpenCV, skimage, etc).

Each function should be implemented as a helper function and called inside `compare_images(i1, i2)`.

Function signature:
    def compare_images(i1: np.ndarray, i2: np.ndarray) -> dict:

The return value should be like:
{
    "mse": float,
    "psnr": float,
    "ssim": float,
    "npcc": float
}

Assume that i1 and i2 are normalized grayscale images (values between 0 and 1).
"""

import numpy as np

def compare_images(i1: np.ndarray, i2: np.ndarray) -> dict:
    if i1.shape != i2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho")

    mse = np.mean((i1 - i2) ** 2)

    if mse == 0:
        psnr = float('inf')
    else:
        max_pixel = 1.0
        psnr = 20 * np.log10(max_pixel / np.sqrt(mse))

    c1 = (0.01) ** 2
    c2 = (0.03) ** 2
    mu1 = np.mean(i1)
    mu2 = np.mean(i2)
    sigma1_sq = np.mean((i1 - mu1) ** 2)
    sigma2_sq = np.mean((i2 - mu2) ** 2)
    sigma12 = np.mean((i1 - mu1) * (i2 - mu2))
    ssim = ((2 * mu1 * mu2 + c1) * (2 * sigma12 + c2)) / \
           ((mu1 ** 2 + mu2 ** 2 + c1) * (sigma1_sq + sigma2_sq + c2))

    numerator = np.sum((i1 - mu1) * (i2 - mu2))
    denominator = np.sqrt(np.sum((i1 - mu1) ** 2) * np.sum((i2 - mu2) ** 2))
    npcc = numerator / denominator if denominator != 0 else 0.0

    return {
        "mse": mse,
        "psnr": psnr,
        "ssim": ssim,
        "npcc": npcc
    }