# image_geometry_exercise.py
# STUDENT'S EXERCISE FILE

"""
Exercise:
Implement a function `apply_geometric_transformations(img)` that receives a grayscale image
represented as a NumPy array (2D array) and returns a dictionary with the following transformations:

1. Translated image (shift right and down)
2. Rotated image (90 degrees clockwise)
3. Horizontally stretched image (scale width by 1.5)
4. Horizontally mirrored image (flip along vertical axis)
5. Barrel distorted image (simple distortion using a radial function)

You must use only NumPy to implement these transformations. Do NOT use OpenCV, PIL, skimage or similar libraries.

Function signature:
    def apply_geometric_transformations(img: np.ndarray) -> dict:

The return value should be like:
{
    "translated": np.ndarray,
    "rotated": np.ndarray,
    "stretched": np.ndarray,
    "mirrored": np.ndarray,
    "distorted": np.ndarray
}
"""

import numpy as np

def apply_geometric_transformations(img: np.ndarray) -> dict:
    H, W = img.shape
    shift_x, shift_y = 50, 50
    translated = np.zeros_like(img)
    for y in range(H):
        for x in range(W):
            new_x = x - shift_x
            new_y = y - shift_y
            if 0 <= new_x < W and 0 <= new_y < H:
                translated[y, x] = img[new_y, new_x]
    rotated = np.zeros((W, H))
    for y in range(H):
        for x in range(W):
            rotated[x, H - 1 - y] = img[y, x]
    new_width = int(W * 1.5)
    stretched = np.zeros((H, new_width))
    for y in range(H):
        for x in range(new_width):
            orig_x = int(x / 1.5)
            if orig_x < W:
                stretched[y, x] = img[y, orig_x]
    mirrored = np.zeros_like(img)
    for y in range(H):
        for x in range(W):
            mirrored[y, W - 1 - x] = img[y, x]
    distorted = np.zeros_like(img)
    center_y, center_x = H / 2, W / 2
    k = 0.0001
    for y in range(H):
        for x in range(W):
            dy = y - center_y
            dx = x - center_x
            r = np.sqrt(dx ** 2 + dy ** 2)
            factor = 1 + k * r ** 2
            new_x = int(center_x + dx / factor)
            new_y = int(center_y + dy / factor)
            if 0 <= new_x < W and 0 <= new_y < H:
                distorted[y, x] = img[new_y, new_x]
    return {
        "translated": translated,
        "rotated": rotated,
        "stretched": stretched,
        "mirrored": mirrored,
        "distorted": distorted
    }