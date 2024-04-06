import math
import cv2
import numpy as np

original = cv2.imread("image.png")
contrast = cv2.imread("receiver_picture/profile-picture-2.PNG")

def psnr(img1, img2):
    mse = np.mean(np.square(np.subtract(img1.astype(np.int16), img2.astype(np.int16))))
    if mse == 0:
        return np.Inf
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX) - 10 * math.log10(mse)  

d = psnr(original, contrast)
print(d)