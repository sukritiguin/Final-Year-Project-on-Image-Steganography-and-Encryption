from PIL import Image
import numpy as np

def calculate_image_difference(image1_path, image2_path):
    # Open the images
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Convert images to numpy arrays
    img1_array = np.array(img1)
    img2_array = np.array(img2)

    # Compute absolute difference between the two images
    diff_array = np.abs(img1_array - img2_array)

    # Sum the differences along the RGB channels
    diff_sum = np.sum(diff_array, axis=2)

    # Calculate the total difference (sum of differences in all channels)
    total_diff = np.sum(diff_sum)

    return total_diff

# Example usage
image1_path = "page_1.png"
image2_path = "page_1 copy 2.png"
difference = calculate_image_difference(image1_path, image2_path)
print("Pixel-level difference between the images in RGB:", difference)


