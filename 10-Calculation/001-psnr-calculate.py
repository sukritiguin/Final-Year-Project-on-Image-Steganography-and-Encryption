import cv2
import numpy as np

def calculate_ssim(image1, image2, k1=0.01, k2=0.03, L=255):
    # Convert images to float32
    image1 = image1.astype(np.float32)
    image2 = image2.astype(np.float32)

    # Constants for stability
    C1 = (k1 * L) ** 2
    C2 = (k2 * L) ** 2

    # Calculate means
    mu1 = cv2.GaussianBlur(image1, (11, 11), sigmaX=1.5)
    mu2 = cv2.GaussianBlur(image2, (11, 11), sigmaX=1.5)

    # Calculate variances
    mu1_sq = mu1 ** 2
    mu2_sq = mu2 ** 2
    mu1_mu2 = mu1 * mu2

    sigma1_sq = cv2.GaussianBlur(image1 ** 2, (11, 11), sigmaX=1.5) - mu1_sq
    sigma2_sq = cv2.GaussianBlur(image2 ** 2, (11, 11), sigmaX=1.5) - mu2_sq
    sigma12 = cv2.GaussianBlur(image1 * image2, (11, 11), sigmaX=1.5) - mu1_mu2

    # Calculate SSIM
    numerator = (2 * mu1_mu2 + C1) * (2 * sigma12 + C2)
    denominator = (mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2)

    ssim_map = numerator / denominator

    # Return the mean SSIM value
    return np.mean(ssim_map)

def calculate_metrics(image1_path, image2_path):
    # Read images
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    
    # Calculate Mean Squared Error (MSE)
    mse = np.mean((image1 - image2) ** 2)
    
    # Calculate Peak Signal-to-Noise Ratio (PSNR)
    max_pixel = 255.0
    psnr = 10 * np.log10((max_pixel ** 2) / mse)
    
    # Calculate Structural Similarity Index (SSIM)
    ssim_index = calculate_ssim(image1, image2)
    
    # Calculate Mean Absolute Error (MAE)
    mae = np.abs(image1 - image2).mean()
    
    return mse, psnr, ssim_index, mae

# Example usage:
image_path = r'D:\Image Steganography and Encryption\10-Calculation\image.png'
lsb_image_path = r'D:\Image Steganography and Encryption\10-Calculation\encoded_image.png'
modified_lsb_image_path = r'D:\Image Steganography and Encryption\10-Calculation\sSWj9D-image.png'

mse1, psnr1, ssim1, mae1 = calculate_metrics(image_path, lsb_image_path)
mse2, psnr2, ssim2, mae2 = calculate_metrics(image_path, modified_lsb_image_path)

print("Metrics for image vs. LSB image:")
print("MSE:", mse1)
print("PSNR:", psnr1)
print("SSIM:", ssim1)
print("MAE:", mae1)
print()
print("Metrics for image vs. modified LSB image:")
print("MSE:", mse2)
print("PSNR:", psnr2)
print("SSIM:", ssim2)
print("MAE:", mae2)
